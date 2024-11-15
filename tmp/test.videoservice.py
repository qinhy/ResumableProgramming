"This model needs UUIDs to identify itself and related files."
"We also need to record the process to ensure the state can be restored."

from collections import deque
from functools import wraps
import os
from typing import Callable
import uuid
import cv2
import numpy as np  # Assuming you are using OpenCV to work with videos


import shelve,re

class ShelveStorage:
    def __init__(self, filename: str = 'storage.db'):
        """Create a storage connection to a Shelve database"""
        try:
            self.filename = filename
            self.db = shelve.open(filename, writeback=True)
        except Exception as e:
            print("Shelve open error:", e)
            self.db = None

    def exists(self, key: str) -> bool:
        return key in self.db

    def set(self, key: str, value: dict):
        try:
            self.db[f'{key}'] = value
            self.db.sync()  # Ensure the data is written to disk
        except Exception as e:
            print("Set error:", e)

    def get(self, key: str) -> dict:
        try:
            return self.db.get(f'{key}', None)
        except Exception as e:
            print("Get error:", e)
            return None

    def delete(self, key: str):
        key = f'{key}'
        try:
            if key in self.db:
                del self.db[key]
                self.db.sync()  # Ensure the data is written to disk
        except Exception as e:
            print("Delete error:", e)

    def keys(self, pattern: str = '*') -> list[str]:
        try:
            regex = '^' + pattern.replace('*', '.*')
            return [key for key in self.db.keys() if re.match(regex, key)]
        except Exception as e:
            print("Keys error:", e)
            return []
    
    def clean(self):
        for k in self.keys():self.delete(k)

    def close(self):
        if self.db: self.db.close()

# easy to change back end ShelveStorage or MongoDBStorage( need mongoDB )
class DBStorage(ShelveStorage):
    pass

class VideoConversionModel:
    
    def __init__(self, uuid = None, filename=None, 
                        converted_count = -1, state = None) -> None:
        # conversion_task_uuid
        self.uuid = uuid
        self.filename = filename    
        self.filesize = self.get_filesize(filename)  # Placeholder for actual file size calculation

        if self.filesize <= 0:
            raise ValueError('File size must be greater than 0')
        
        cap = cv2.VideoCapture(filename)
        if not cap.isOpened(): raise RuntimeError(f"Failed to open video file: {filename}")
        
        # Get frame width and height, adjust width up to 320 for thumbnail
        ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH)/320
        self.thumbnail_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/ratio)
        self.thumbnail_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/ratio)
        self.thumbnail_fps = cap.get(cv2.CAP_PROP_FPS)        
        
        self.thumbnail_bin_path = f'{self.filename}.thumbnail.bin'
        self.thumbnail_mp4_path = f'{self.filename}.thumbnail.mp4'

        # Attributes related to the task
        self.converted_count = converted_count if converted_count>0 else 0
        self.total_count = self.calculate_total_frames(filename)

        self.state = state if state else VideoConversionFSMsController.VideoConversionState.States.idle

    def get_filesize(self,filename):
        if not filename or not os.path.isfile(filename):
            raise FileNotFoundError(f"File '{filename}' does not exist.")
        return os.path.getsize(filename)

    def calculate_total_frames(self,filename):
        # Open the video file using OpenCV
        video_capture = cv2.VideoCapture(filename)        
        if not video_capture.isOpened():
            raise ValueError(f"Unable to open video file: {filename}")
        # Get the total frame count from the video
        total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))        
        # Release the video capture object
        video_capture.release()
        return total_frames

    def to_dict(self):
        return self.__dict__
    
    @staticmethod
    def from_dict(data):
        return VideoConversionModel(data['uuid'],
                                    data['filename'],
                                    data['converted_count'],
                                    data['state'],)

class VideoConversionFSMsController:
    
    class VideoConversionState:
        class States:
            idle = 'idle'
            all_stages = 'all_stages'
            error = 'error'
            complete = 'complete'

        _transitions = {
            States.idle:    [States.all_stages],
            States.all_stages:  [States.all_stages,States.error,States.complete],
            States.error:   [States.idle],
            States.complete:[],

        }
        _states = list(_transitions.keys())

        def __init__(self, controller:'VideoConversionFSMsController'):
            self.controller = controller
            self.model = self.controller.model
            self._state = self.model.state

        def set_state(self,state):
            self._state=state
            self.model.state=state
            self.controller.save_model()
        
        def handle_errors(func:Callable):
            @wraps(func)
            def wrapper(self:'VideoConversionFSMsController.VideoConversionState',
                        *args, **kwargs):
                valid_transitions = self._transitions[self._state]
                target_transition = func.__name__.replace('to_','')
                if target_transition not in valid_transitions:            
                    raise ValueError(f"Invalid transition from [{self._state}] -> [{target_transition}]")
                try:
                    return func(self, *args, **kwargs)
                except Exception as e:
                    print(f'[{self.__class__.__name__}]: {e}')
            return wrapper

        @handle_errors
        def to_idle(self):
            self.set_state(VideoConversionFSMsController.VideoConversionState.States.idle)
            self.controller.save_model()

        @handle_errors
        def to_all_stages(self):
            self.set_state(VideoConversionFSMsController.VideoConversionState.States.all_stages)
            self.controller.save_model()
            try:
                while self.model.converted_count < self.model.total_count:
                    # Transition to reading state
                    ret, frame = self.controller.cap.read()
                    if not ret:
                        raise RuntimeError(f"can not read frame.")
                    self.controller.save_model()

                    # Transition to resizing state
                    frame = cv2.resize(frame, (self.model.thumbnail_width, self.model.thumbnail_height))
                    self.controller.save_model()

                    # Transition to writing state
                    with open(self.model.thumbnail_bin_path,'ab') as f: f.write(frame.tobytes())
                    self.model.converted_count += 1
                    self.controller.save_model()
                        
            except Exception as e:
                self.to_error(f"{self.model.state} error [{self.model.filename}]: {e}")

        @handle_errors
        def to_error(self,e):
            self.set_state(VideoConversionFSMsController.VideoConversionState.States.error)
            self.controller.save_model()
            print(e)

        @handle_errors
        def to_complete(self):
            if self.model.converted_count >= self.model.total_count:
                # convert bin file into mp4
                out = cv2.VideoWriter(
                    self.model.thumbnail_mp4_path,
                    cv2.VideoWriter_fourcc(*'mp4v'),  # Codec for mp4 files
                    self.model.thumbnail_fps,
                    (self.model.thumbnail_width, self.model.thumbnail_height)
                )
                with open(self.model.thumbnail_bin_path, 'rb') as f: raw_data = f.read()
                # Read the frames data
                frames = np.frombuffer(raw_data, dtype=np.uint8).reshape(
                    (self.model.total_count, self.model.thumbnail_height, self.model.thumbnail_width, 3))
                for frame in frames: out.write(frame)
                out.release()

                self.set_state(VideoConversionFSMsController.VideoConversionState.States.complete)
                self.controller.save_model()
            else:
                self.to_all_stages()

        def find_path(self, transitions:dict, start_state, end_state):
            queue = deque([[start_state]])    
            visited = set()    
            while queue:
                path = queue.popleft()
                state = path[-1]        
                if state == end_state:
                    return path
                if state not in visited:
                    visited.add(state)            
                    next_states = transitions.get(state, [])
                    for next_state in next_states:
                        new_path = list(path)
                        new_path.append(next_state)
                        queue.append(new_path)
            return []
        
        def resume_state(self,target_state, max_attempts=100):
            print(f'Set target state: {target_state} ( current is {self._state})')
            def next_action(task:VideoConversionFSMsController.VideoConversionState
                            ,target_state):
                path = self.find_path(self._transitions, task._state, target_state)
                if len(path)<=1: return None
                return path[1]
                
            while self._state != target_state:
                cls = next_action(self,target_state)
                if cls is None:raise ValueError('no next acion! unreachable!')
                if max_attempts<0:raise ValueError(f'over max_attempts!')
                
                print(f'Current: {self._state}, try to_{cls}')
                getattr(self,f'to_{cls}')()
                max_attempts -= 1
            print(f'Success to target state: {self._state}')

    def __init__(self,model:VideoConversionModel) -> None:
        self.model = model
        self.state = VideoConversionFSMsController.VideoConversionState(self)
        
        # Open the video file
        self.cap = cv2.VideoCapture(self.model.filename)
        if not self.cap.isOpened():
            raise RuntimeError(f"Failed to open video file: {self.model.filename}")

        # self.total_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.model.converted_count)
        
    def save_model(self):
        # connect db
        DBStorage().set(self.model.uuid,self.model.to_dict())
        return self
    
    @staticmethod
    def new_video_conversion(filename):
        # new request for file conversion, hard operation
        model = VideoConversionModel(uuid.uuid4(),filename)
        return VideoConversionFSMsController(model).save_model()
    
    @staticmethod
    def find_video_conversion(uuid):
        model = DBStorage().get(uuid)
        if model is None:raise ValueError(f'no such data of {uuid}')
        return VideoConversionFSMsController(VideoConversionModel.from_dict(model))
    
    def do_conversion(self):
        state:VideoConversionFSMsController.VideoConversionState = self.state
        state.resume_state(VideoConversionFSMsController.VideoConversionState.States.complete)
