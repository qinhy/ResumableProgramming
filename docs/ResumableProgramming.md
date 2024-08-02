# Book Title: "Resumable Programming"

## Preface

### Introduction
- Discuss the evolution of programming practices with a focus on the need for resiliency and adaptability in modern software development.

### History of Resumable Programming
- Trace the origins from early computing systems to contemporary frameworks that support asynchrony and fault tolerance.

### Purpose of the Book
- Outline the book’s goals: educating developers on building more robust applications, and providing a toolkit for implementing resumable features in software projects.

---


## Chapter 1: Basic Python
### Introduction
- **Overview**: Introduce Python as a programming language, focusing on features that facilitate resumable programming.
- **Objective**: Equip readers with basic Python skills necessary to implement examples provided in the book.

### Section 1: Python Basics
- Cover Python syntax, control structures, functions, and modules.

### Section 2: Advanced Python Features
- Introduce more complex Python features such as decorators, generators, and context managers, which are crucial for writing resumable code.

### Conclusion
- **Summary**: Recap the Python basics and their relevance to resumable programming.
- **Future Outlook**: Discuss how these fundamentals will be used in subsequent chapters.

---

## Chapter 2: Understanding Resumability

### Introduction
- **Overview**: Define resumable programming as the ability of a process to pause at certain points and then continue from those points later, either after a failure or after a deliberate halt. This capability is crucial for developing robust and scalable applications in environments where interruptions are common or where tasks are long-running.
- **Objective**: Equip readers with a foundational understanding of concepts and applications. By the end of this chapter, readers should appreciate the critical role that resumability plays in modern software development, particularly in distributed systems, cloud applications, and complex data processing workflows.


### Section 0: Why We Need Resumability
In today’s technological landscape, applications are increasingly expected to operate continuously and handle a variety of interruptions—be they from system failures, planned downtime, or user-driven pauses. Resumable programming addresses these needs by ensuring that applications can maintain their functionality and data integrity under such circumstances. 

let's think a simple example without resumability.


```python
print('```')
def fibonacci(n):
    if n <= 1 : return n
    return fibonacci(n-1)+fibonacci(n-2)

# Example 
for i in range(37):
    %time print(f"\nFibonacci of {i} result: {fibonacci(i)}")
print('```')
```

    ```
    
    Fibonacci of 0 result: 0
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 1 result: 1
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 2 result: 1
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 3 result: 2
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 4 result: 3
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 5 result: 5
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 6 result: 8
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 7 result: 13
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 8 result: 21
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 9 result: 34
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 10 result: 55
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 11 result: 89
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 12 result: 144
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 13 result: 233
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 14 result: 377
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 15 result: 610
    CPU times: total: 0 ns
    Wall time: 1.01 ms
    
    Fibonacci of 16 result: 987
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 17 result: 1597
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 18 result: 2584
    CPU times: total: 0 ns
    Wall time: 1.02 ms
    
    Fibonacci of 19 result: 4181
    CPU times: total: 0 ns
    Wall time: 2.13 ms
    
    Fibonacci of 20 result: 6765
    CPU times: total: 0 ns
    Wall time: 3.01 ms
    
    Fibonacci of 21 result: 10946
    CPU times: total: 0 ns
    Wall time: 2.03 ms
    
    Fibonacci of 22 result: 17711
    CPU times: total: 15.6 ms
    Wall time: 4.33 ms
    
    Fibonacci of 23 result: 28657
    CPU times: total: 15.6 ms
    Wall time: 20 ms
    
    Fibonacci of 24 result: 46368
    CPU times: total: 15.6 ms
    Wall time: 40 ms
    
    Fibonacci of 25 result: 75025
    CPU times: total: 46.9 ms
    Wall time: 30 ms
    
    Fibonacci of 26 result: 121393
    CPU times: total: 15.6 ms
    Wall time: 24.5 ms
    
    Fibonacci of 27 result: 196418
    CPU times: total: 31.2 ms
    Wall time: 40 ms
    
    Fibonacci of 28 result: 317811
    CPU times: total: 46.9 ms
    Wall time: 64.5 ms
    
    Fibonacci of 29 result: 514229
    CPU times: total: 31.2 ms
    Wall time: 101 ms
    
    Fibonacci of 30 result: 832040
    CPU times: total: 125 ms
    Wall time: 179 ms
    
    Fibonacci of 31 result: 1346269
    CPU times: total: 109 ms
    Wall time: 274 ms
    
    Fibonacci of 32 result: 2178309
    CPU times: total: 219 ms
    Wall time: 436 ms
    
    Fibonacci of 33 result: 3524578
    CPU times: total: 406 ms
    Wall time: 701 ms
    
    Fibonacci of 34 result: 5702887
    CPU times: total: 719 ms
    Wall time: 1.15 s
    
    Fibonacci of 35 result: 9227465
    CPU times: total: 1.33 s
    Wall time: 1.89 s
    
    Fibonacci of 36 result: 14930352
    CPU times: total: 1.91 s
    Wall time: 3.07 s
    ```
    


Here are some key reasons why resumability is essential from the example:

- **Reliability and Robustness**: In this example, we find that it is very time-consuming and computationally expensive. Applications that can resume from the last known good state are inherently more reliable. In environments where service interruptions are costly, such as in financial systems or critical infrastructure, the ability to recover quickly and seamlessly from failures is invaluable.

- **User Experience**: For end-users, the ability to pause and resume processes can significantly enhance the user experience, especially in terms of responsiveness. This is particularly evident in consumer applications like video streaming, downloads, or large file uploads, where users expect the ability to pause and resume activities at their convenience.

- **Scalability**: As systems grow and handle more parallel processes, the ability to manage and maintain state across these processes becomes crucial. Resumable programming facilitates scaling by allowing individual components or services to be paused and resumed independently, thus supporting graceful scaling and reducing bottlenecks.

- **Long-Running Processes**: Certain applications involve processes that inherently take a long time to complete, such as scientific simulations, batch processing jobs, or media encoding tasks. Resumability ensures that these long-running processes can continue from where they left off in the event of interruptions, without the need to start over.


Here's how we can implement a resumable Fibonacci function in Python, using memoization with persistent storage:


```python
import shelve  # Used for simple key-value pair storage
def fibonacci(n, db_path='fibonacci_cache.db'):
   if n <= 1 : return n

   with shelve.open(db_path) as db:
      if str(n) in db : return db[str(n)]

      db[str(n)] = fibonacci(n-1)+fibonacci(n-2)
      return db[str(n)]

# Example will calc very fast
print('```')
for i in range(37):
    %time print(f"\nFibonacci of {i} result: {fibonacci(i)}")
print('```')
```

    ```
    
    Fibonacci of 0 result: 0
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 1 result: 1
    CPU times: total: 0 ns
    Wall time: 0 ns
    
    Fibonacci of 2 result: 1
    CPU times: total: 0 ns
    Wall time: 5.29 ms
    
    Fibonacci of 3 result: 2
    CPU times: total: 0 ns
    Wall time: 11.1 ms
    
    Fibonacci of 4 result: 3
    CPU times: total: 15.6 ms
    Wall time: 13.5 ms
    
    Fibonacci of 5 result: 5
    CPU times: total: 0 ns
    Wall time: 6 ms
    
    Fibonacci of 6 result: 8
    CPU times: total: 0 ns
    Wall time: 15 ms
    
    Fibonacci of 7 result: 13
    CPU times: total: 0 ns
    Wall time: 21 ms
    
    Fibonacci of 8 result: 21
    CPU times: total: 0 ns
    Wall time: 18.6 ms
    
    Fibonacci of 9 result: 34
    CPU times: total: 0 ns
    Wall time: 4.52 ms
    
    Fibonacci of 10 result: 55
    CPU times: total: 0 ns
    Wall time: 5 ms
    
    Fibonacci of 11 result: 89
    CPU times: total: 15.6 ms
    Wall time: 11 ms
    
    Fibonacci of 12 result: 144
    CPU times: total: 0 ns
    Wall time: 12 ms
    
    Fibonacci of 13 result: 233
    CPU times: total: 0 ns
    Wall time: 14 ms
    
    Fibonacci of 14 result: 377
    CPU times: total: 0 ns
    Wall time: 6 ms
    
    Fibonacci of 15 result: 610
    CPU times: total: 0 ns
    Wall time: 17 ms
    
    Fibonacci of 16 result: 987
    CPU times: total: 0 ns
    Wall time: 6 ms
    
    Fibonacci of 17 result: 1597
    CPU times: total: 0 ns
    Wall time: 14 ms
    
    Fibonacci of 18 result: 2584
    CPU times: total: 0 ns
    Wall time: 10.5 ms
    
    Fibonacci of 19 result: 4181
    CPU times: total: 0 ns
    Wall time: 12 ms
    
    Fibonacci of 20 result: 6765
    CPU times: total: 0 ns
    Wall time: 10 ms
    
    Fibonacci of 21 result: 10946
    CPU times: total: 0 ns
    Wall time: 10 ms
    
    Fibonacci of 22 result: 17711
    CPU times: total: 0 ns
    Wall time: 15 ms
    
    Fibonacci of 23 result: 28657
    CPU times: total: 0 ns
    Wall time: 10 ms
    
    Fibonacci of 24 result: 46368
    CPU times: total: 0 ns
    Wall time: 9.52 ms
    
    Fibonacci of 25 result: 75025
    CPU times: total: 0 ns
    Wall time: 11 ms
    
    Fibonacci of 26 result: 121393
    CPU times: total: 15.6 ms
    Wall time: 9.51 ms
    
    Fibonacci of 27 result: 196418
    CPU times: total: 0 ns
    Wall time: 12.9 ms
    
    Fibonacci of 28 result: 317811
    CPU times: total: 0 ns
    Wall time: 11.6 ms
    
    Fibonacci of 29 result: 514229
    CPU times: total: 0 ns
    Wall time: 11 ms
    
    Fibonacci of 30 result: 832040
    CPU times: total: 0 ns
    Wall time: 11 ms
    
    Fibonacci of 31 result: 1346269
    CPU times: total: 0 ns
    Wall time: 10 ms
    
    Fibonacci of 32 result: 2178309
    CPU times: total: 0 ns
    Wall time: 10 ms
    
    Fibonacci of 33 result: 3524578
    CPU times: total: 15.6 ms
    Wall time: 12 ms
    
    Fibonacci of 34 result: 5702887
    CPU times: total: 0 ns
    Wall time: 11 ms
    
    Fibonacci of 35 result: 9227465
    CPU times: total: 15.6 ms
    Wall time: 11.4 ms
    
    Fibonacci of 36 result: 14930352
    CPU times: total: 0 ns
    Wall time: 18.5 ms
    ```
    


#### Key Features of This Resumable Implementation:
- **Persistence**: The use of a `shelve` database (we will discuss more databases later), which is a simple persistent storage for Fibonacci integers, allows the function to get/set results. If the process is interrupted, the previously computed values of the sequence are saved (this is also very beneficial when the app crashes unexpectedly).
- **Performance**: By saving previously computed values, we avoid redundant calculations, thus minimizing re-computation. This drastically improves performance, especially for large `n`.

This approach illustrates a basic method to make the Fibonacci function resumable by using external storage for state. This can be extended to more complex algorithms and applications where resumability is crucial.

### Section 1: Core Concepts
To simplify "Resumability" in the first step for easier understanding, as in the above example, we can consider the following design pattern.


```python
def processA(args):
    # Perform the processing for A
    result = f'Result of A processing args: {args}'
    return result
    
def processB(args):
    # Perform the processing for B
    result = f'Result of B processing args: {args}'
    return result

def processC(args):
    # Perform the processing for C
    result = f'Result of C processing args: {args}'
    return result

# ... processN
```


- **Reproducibility**: As we know, certain function will return the same result if provided with the same arguments. This is called "reproducibility," which is important for "resumable implementation." We will not discuss functions that have randomness even when provided with the same arguments.

- **State**: In this example of "State"(We can also treat it as a "model", which we will discuss later), we can assume the arguments and results (In fact, this is not very accurate; we will discuss it later). To ensure an application has resumability, it is essential to maintain all the states information that allows the program to resume where it left off.

Now, let us move on to the second step of imagining a high-level abstraction. As we know from videos or some books, a robot or machine(or a controller) is designed to repeat certain actions or follow specific commands. In our example, this "reproducibility" can also be assumed to function like a machine(or a controller), similar to a ["finite-state machine"](https://en.wikipedia.org/wiki/Finite-state_machine).


```python
"A high-level Machine object abstraction"
class Machine:
    def __init__():
        pass

    def processA(args):
        # Perform the processing for A
        result = f'Result of A processing args: {args}'
        return result
        
    def processB(args):
        # Perform the processing for B
        result = f'Result of B processing args: {args}'
        return result

    def processC(args):
        # Perform the processing for C
        result = f'Result of C processing args: {args}'
        return result

    # ... processN
```


```python
"A Machine object actual moving implementation"
import math
import random
class MachineA:
    def __init__(self, initial_orientation=0, initial_position=(0, 0)):
        # Initialize the machine with orientation and position
        self.orientation = initial_orientation  # In degrees, 0 pointing east( x+ )
        self.position = list(initial_position)  # Position as a list [x, y]

    def turn_left(self, degrees):
        # Turn the machine left by a certain degree
        self.orientation = (self.orientation + degrees) % 360
        print(f"Turned left {degrees} degrees. New orientation: {self.orientation}")
        return self.random_crash()

    def turn_right(self, degrees):
        # Turn the machine right by a certain degree
        self.orientation = (self.orientation - degrees) % 360
        print(f"Turned right {degrees} degrees. New orientation: {self.orientation}")
        return self.random_crash()

    def move_forward(self, distance):
        # Move the machine forward in the direction of the current orientation
        radian = math.radians(self.orientation)
        self.position[0] += distance * math.cos(radian)  # x position changes
        self.position[1] += distance * math.sin(radian)  # y position changes
        print(f"Moved forward {distance} distance. New position: {self.position}")
        return self.random_crash()

    def move_backward(self, distance):
        # Move the machine backward opposite to the current orientation
        radian = math.radians(self.orientation)
        self.position[0] -= distance * math.cos(radian)  # x position changes
        self.position[1] -= distance * math.sin(radian)  # y position changes
        print(f"Reversed {distance} distance. New position: {self.position}")
        return self.random_crash()

    def get_machine_state(self):
        return self.orientation,self.position
    
    def random_crash(self):
        pass
        # if random.random() > 0.6:
        #     print('This machine crashed!')
        #     self.reset()
        #     False
        # else:
        #     return True

    def reset(self):
        # Reset the machine to the initial state
        self.orientation = 0
        self.position = [0, 0]
        print("Machine has been reset to the 0,(0,0) state.")

print('```')
# Example of using MachineA
machine = MachineA()  # Initialize with default orientation and position
#              y
#              ^
#              |
#              |
#              |
#              |
# <----------- O>----------------->x

machine.turn_left(90)
#              y
#              ^
#              |
#              |
#              |
#              ^
# <----------- O------------------>x

machine.move_forward(10)
#              y
#              ^
#              ^
#              O
#              |
#              |
# <----------- |------------------>x

print(machine.get_machine_state())

machine.turn_right(90)
#             y
#             ^
#             |
#             O>
#             |
#             |
# <-----------|------------------>x

machine.move_backward(5)
#             y
#             ^
#             |
#         O>  |
#             |
#             |
# <-----------|------------------>x

print(machine.get_machine_state())
print('```')
```

    ```
    Turned left 90 degrees. New orientation: 90
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    (90, [6.123233995736766e-16, 10.0])
    Turned right 90 degrees. New orientation: 0
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    (0, [-4.999999999999999, 10.0])
    ```
    

- **Machine(Controller)**: This example demonstrates that a machine (or an object of MachineA or a controller) with certain parameters (or initialization arguments) can perform actions (or processes or tasks) and then reach a state (or result). The "Resumable Implementation" allows us to make this machine resumable at any checkpoint, even if it crashes suddenly( we will enable random_crash function later).

- **State**: In this example of a machine state, the orientation and position are considered. To ensure this machine has resumability, we have two ways to implement it. The first way is to record the orientation and position of the machine state after performing each action( or process). The second way is to record the action name and its arguments as a "state" after performing each action.


```python
import math
import random
class MachineA:
    def __init__(self, initial_orientation=0, initial_position=(0, 0)):
        # Initialize the machine with orientation and position
        self.orientation = initial_orientation  # In degrees, 0 pointing east( x+ )
        self.position = list(initial_position)  # Position as a list [x, y]

    def turn_left(self, degrees):
        # Turn the machine left by a certain degree
        self.orientation = (self.orientation + degrees) % 360
        print(f"Turned left {degrees} degrees. New orientation: {self.orientation}")
        return self.random_crash()

    def turn_right(self, degrees):
        # Turn the machine right by a certain degree
        self.orientation = (self.orientation - degrees) % 360
        print(f"Turned right {degrees} degrees. New orientation: {self.orientation}")
        return self.random_crash()

    def move_forward(self, distance):
        # Move the machine forward in the direction of the current orientation
        radian = math.radians(self.orientation)
        self.position[0] += distance * math.cos(radian)  # x position changes
        self.position[1] += distance * math.sin(radian)  # y position changes
        print(f"Moved forward {distance} distance. New position: {self.position}")
        return self.random_crash()

    def move_backward(self, distance):
        # Move the machine backward opposite to the current orientation
        radian = math.radians(self.orientation)
        self.position[0] -= distance * math.cos(radian)  # x position changes
        self.position[1] -= distance * math.sin(radian)  # y position changes
        print(f"Reversed {distance} distance. New position: {self.position}")
        return self.random_crash()

    def get_machine_state(self):
        return self.orientation,self.position
    
    def random_crash(self):
        if random.random() > 0.6:
            print('!!!!!!!!!This machine crashed, auto reset!!!!!!!!!')
            self.reset()
            return False
        else:
            return True

    def reset(self):
        # Reset the machine to the initial state
        self.orientation = 0
        self.position = [0, 0]
        print("Machine has been reset to the 0,(0,0) state.")

# Example of using MachineA
print('```')
machine = MachineA()
machine.turn_left(90)
machine.move_forward(10)
print(machine.get_machine_state())
machine.turn_right(90)
machine.move_backward(5)
print(machine.get_machine_state())
print('```')
```

    ```
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Moved forward 10 distance. New position: [10.0, 0.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    (0, [0, 0])
    Turned right 90 degrees. New orientation: 270
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Reversed 5 distance. New position: [-5.0, 0.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    (0, [0, 0])
    ```
    

The machine in the code shows unstable movements, making it very hard to reach the goal axis of (-5, 10). In production systems, obviously, users will hate losing their previous work and ending up in an unexpected state, which is not the goal.

let us make a simple "Resumable Implementation" as following:


```python
"The first way is to record the orientation and position of the machine state after performing each action( or process)."

import shelve  # Used for simple key-value pair storage
with shelve.open('machine_cache.db') as db:
    
    print('```')
    machine = MachineA()
    db['machine_state'] = machine.get_machine_state() # reord
    
    while not machine.turn_left(90): # try action untill success
        machine = MachineA(*db['machine_state']) # recover machine by last state
    db['machine_state'] = machine.get_machine_state() # reord when success

    while not machine.move_forward(10):        
        machine = MachineA(*db['machine_state'])
    db['machine_state'] = machine.get_machine_state()
        
    print(machine.get_machine_state())

    while not machine.turn_right(90):
        machine = MachineA(*db['machine_state'])
    db['machine_state'] = machine.get_machine_state()

    while not machine.move_backward(5):
        machine = MachineA(*db['machine_state'])
    db['machine_state'] = machine.get_machine_state()
        
    print(machine.get_machine_state())    
    print('```')
    
# The second way is to record the action name and its arguments as a "state" after performing each action. 
```

    ```
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Turned left 90 degrees. New orientation: 90
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    (90, [6.123233995736766e-16, 10.0])
    Turned right 90 degrees. New orientation: 0
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    (0, [-4.999999999999999, 10.0])
    ```
    

- **Fist Way: Recording Machine State After Each Action**: This approach saves the entire state of the machine after each action using a key-value store. When an action results in a crash, the machine's state is restored from the last successful operation, and the action is retried.
    - Strengths:
      - **Direct State Management**: This method directly saves the complete state of the machine after each successful action. It's straightforward and ensures that you always revert to a known good state.
      - **Simplicity**: The approach is relatively simple to implement as it involves straightforward serialization and deserialization of the machine's state, making it easy to understand and maintain.
      - **Immediate Recovery**: Recovery can be immediate and precise because the entire state is saved, allowing the machine to pick up exactly where it left off.

    - Weaknesses:
      - **Applicability**: Recovering a machine to certain entire state requires that the machine can be set to a given state. Many times, libraries do not allow us to do that.
      - **Storage Space**: Storing the entire state after every action can consume a lot of storage space, especially if the state includes **large** data structures.
      - **Scalability Issues**: As the complexity of the machine's state grows, the time and resources required to serialize, save, and reload the state can increase, potentially making this method less scalable.


```python
"The second way is to record the action name and its arguments as a 'state' after performing each action."

import shelve  # Used for simple key-value pair storage
import copy

def redo_actions(machine_class,action_list):
    state = copy.deepcopy(action_list)
    machine = machine_class() # initial machine
    while len(state)>0:
        action,args = state.pop(0)
        print(action,args)
        if not getattr(machine,action)(args): # recover history actions
            state = copy.deepcopy(action_list)  # recover failure and do init again
            machine = machine_class()
    return machine


with shelve.open('machine_cache.db') as db:
    
    print('```')
    machine = MachineA()
    db['machine_state'] = []

    while not machine.turn_left(90): # try action untill success
        machine = redo_actions(MachineA,db['machine_state'])
    db['machine_state'] = db['machine_state'] + [('turn_left',90)]

    while not machine.move_forward(10):
        machine = redo_actions(MachineA,db['machine_state'])
    db['machine_state'] = db['machine_state'] + [('move_forward',10)]
    
    print(machine.get_machine_state())

    while not machine.turn_right(90):
        machine = redo_actions(MachineA,db['machine_state'])
    db['machine_state'] = db['machine_state'] + [('turn_right',90)]

    while not machine.move_backward(5):
        machine = redo_actions(MachineA,db['machine_state'])
    db['machine_state'] = db['machine_state'] + [('move_backward',5)]
        
    print(machine.get_machine_state())
    print('```')
# The second way is to record the action name and its arguments as a "state" after performing each action. 
```

    ```
    Turned left 90 degrees. New orientation: 90
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    (90, [6.123233995736766e-16, 10.0])
    Turned right 90 degrees. New orientation: 0
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    Turned right 90 degrees. New orientation: 0
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    (0, [-4.999999999999999, 10.0])
    ```
    

- **Second Way: Recording Actions and Arguments as State**: In this method, we record each action and its parameters. Upon a crash, the machine is reinitialized, and all recorded actions are replayed to restore the last known good state before attempting to continue from the point of failure.

  - Strengths:
    - **Action Replay**: This method records actions and their parameters, allowing the system to reconstruct the state by replaying these actions. This can be more storage-efficient, especially if the actions are compact.
    - **Audit Trail**: Storing a list of actions provides an audit trail of what the machine did, which can be useful for debugging, auditing, and understanding the sequence of operations leading to a crash.
    - **Adaptive Recovery**: By replaying actions from the beginning, this method can potentially adapt to changes in the system's logic or configuration since the state is dynamically reconstructed.

  - Weaknesses:
    - **Replay Overhead**: The major downside is the need to replay all actions from the start or from a checkpoint in the event of a crash. This can be time-consuming and inefficient, especially if the list of actions is long.
    - **Complexity in Handling Stateful Actions**: If actions are not purely functional or if they depend on external state not captured solely by the action parameters, replaying actions might not accurately reconstruct the state.
    - **Potential for Infinite Loops**: Without proper checks, there's a risk of entering an infinite loop of crashes and recoveries if a particular action consistently leads to a crash.



### Conclusion

- **Importance of Resumable Programming**: Resumability is crucial for developing robust, scalable applications in environments prone to interruptions or where tasks are long-running.
   
- **Reliability and Robustness**: Applications that can resume from the last known good state enhance reliability, especially in critical systems where downtime is costly.

- **Enhanced User Experience**: Resumability improves the user experience by providing the ability to pause and resume processes, which is essential in consumer applications like video streaming and file uploads.

- **Scalability**: Resumable programming supports graceful scaling by allowing individual components to be paused and resumed independently, reducing bottlenecks.

- **Persistence and Performance**: Implementing resumability through methods like storing states or actions ensures that applications can recover from interruptions without redundant recalculations, enhancing performance.

- **Recording Machine State**: if the machine's state is relatively small, quick to serialize/deserialize, or if precise recovery to the last known good state is critical. This method is suitable for systems where actions are expensive or have significant side effects that need to be precisely managed.

- **Recording Machine Action**: if actions are relatively simple, the state is large or complex, or if you benefit from having an audit trail of actions. This method is preferable when actions are cheap to replay, or when the system's design allows for efficient state reconstruction.

### Additional Notes
- **Databases**: As the examples above show, we indeed need persistent storage (or a database) to save our states for resumability and to manage our states. We can use both SQL (such as PostgreSQL's support for transactional states) and NoSQL technologies (such as MongoDB's document-based storage, which can be effectively used for maintaining state), which we will discuss in the next chapter.

- **Message Queues**: Message queues can be used to send commands, events, etc., which will be useful for controlling resumable machine clusters over the internet. Tools like RabbitMQ or Kafka can manage tasks in a resumable fashion by decoupling task submission from execution.

- **Cloud Services**: Review cloud-based solutions that provide built-in support for resumability, such as AWS Step Functions, which allows the definition of workflows as state machines, or Azure Durable Functions, a solution designed to write stateful functions in a serverless computing environment.

- **Potential Challenges**: The text highlights potential challenges in resumable programming, such as handling complex, stateful actions, and the risk of inefficiencies or infinite loops in action replay methods.

- **Future Considerations**: For effective resumability, future systems may need to balance between state management and action replay, potentially incorporating intelligent mechanisms to minimize performance overhead and maximize reliability.


---

## Chapter 3: SQL vs Key-Value Databases
### Introduction
- **Overview**: This chapter delves into the comparison of SQL and key-value databases, focusing on their roles in maintaining state within resumable systems. These databases offer distinct approaches to data management and state persistence, crucial for applications that require robust resumability features.
- **Objective**: By exploring the characteristics of both SQL and key-value databases, readers will gain insights into which database type is better suited for specific scenarios in resumable programming, enhancing the efficiency and reliability of their systems.

### Section 1: SQL Databases

#### What: Understanding SQL Databases

- Definition and Core Characteristics
  - **SQL (Structured Query Language)**: SQL databases use SQL, a standard programming language specifically designed for managing and manipulating relational databases. SQL provides the means to execute queries, retrieve data, insert new data, update existing data, and delete data.
  - **Structured Data**: Unlike NoSQL databases that can handle unstructured or semi-structured data, SQL databases are structured. They require a predefined schema that dictates the table structure, data types, and relationships—making them highly organized and suitable for complex queries.

- Components of SQL Databases

  - Tables
A table in an SQL database stores data in rows and columns, similar to a spreadsheet. For example, consider a table named `Users` that stores information about users in an application:

    ```sql
        CREATE TABLE Users (
            UserID INT PRIMARY KEY,
            FirstName VARCHAR(50),
            LastName VARCHAR(50),
            Email VARCHAR(100) UNIQUE,
            RegistrationDate DATE
        );
    ```
    - Each row represents a single user.
    - Columns include `UserID`, `FirstName`, `LastName`, `Email`, and `RegistrationDate`.
    - `UserID` serves as the primary key, uniquely identifying each row in the table.



- Primary and Foreign Keys
    - Primary keys uniquely identify each record in a table, while foreign keys link the records of one table to another. For instance, if there's another table called `Orders` that needs to link back to `Users`, it might look like this:

        ```sql
            CREATE TABLE Orders (
                OrderID INT PRIMARY KEY,
                UserID INT,
                OrderDate DATE,
                Amount DECIMAL(10, 2),
                FOREIGN KEY (UserID) REFERENCES Users(UserID)
            );
        ```

        - `OrderID` is the primary key of the `Orders` table.
        - `UserID` is a foreign key that connects each order to a user in the `Users` table.

- Indexes
    - Indexes improve the speed of data retrieval operations by providing quick lookups on columns that are frequently searched. An index can be created on the `Email` column in the `Users` table to optimize search queries for user emails:

        ```sql
            CREATE INDEX idx_email ON Users(Email);
        ```

        - This index allows the database to find data using the `Email` column more efficiently than scanning the entire table.

- Views
    - Views are virtual tables based on the result-set of an SQL statement. They can simplify complex queries, improve readability, and restrict access to certain data. For example, a view to get only the names and email of users could be defined as follows:

        ```sql
            CREATE VIEW View_UserContacts AS
            SELECT FirstName, LastName, Email
            FROM Users;
        ```

        - This view, `View_UserContacts`, does not store data itself but provides a simplified and restricted view of the users' data, which can be particularly useful for applications where only minimal user information is needed and enhances security by not exposing sensitive data like `UserID`.

- Data Integrity and ACID Properties
  - **Atomicity**: Guarantees that each transaction is treated as a single unit, which is either completed in full or not at all. This property is crucial for maintaining consistency in case of a system failure.
  - **Consistency**: Ensures that only valid data following all rules and constraints is written to the database. Any transaction the database processes must leave it in a consistent state.
  - **Isolation**: Ensures that transactions occur independently without interference. Changes occurring in a transaction will not be visible to other transactions until that transaction is committed.
  - **Durability**: Once a transaction has been committed, it will remain so, even in the event of a power loss, crash, or error. This makes SQL databases extremely reliable for critical systems where data must not be lost.

- Querying and Transaction Management
  - **Complex Queries**: SQL databases support complex queries involving multiple tables (joins), complex conditions, and aggregations, which are essential for in-depth data analysis and reporting.
  - **Transaction Control**: SQL provides robust transaction control capabilities, including commands like `BEGIN`, `COMMIT`, `ROLLBACK`, and `SAVEPOINT`. These commands allow for precise control over transaction execution, which is vital for implementing resumable functionalities in applications.


#### Who: Users of SQL Databases
- **Target Users**: Identify the primary users of SQL databases, including database administrators, developers, and companies that require robust data integrity, complex querying capabilities, and strong transactional support.
- **Industries**: Highlight industries where SQL databases are particularly prevalent, such as finance, healthcare, and e-commerce.

#### Where: Applications of SQL Databases in Resumable Systems
- **Use Cases**: Discuss specific use cases of SQL databases in resumable systems, such as transaction processing systems, inventory management systems, and any application requiring complex transactional logic that must be resumed after interruptions.
- **Environment**: Explain the typical environments where SQL databases are deployed, focusing on server-based architectures, cloud environments, and on-premise solutions.

#### When: Choosing SQL Databases
- **Scenarios for Use**: Outline scenarios where using SQL databases is ideal, emphasizing situations that require complex queries, transaction integrity, and historical data analysis.
- **Evolution Over Time**: Briefly discuss the historical development of SQL databases and their evolution to meet modern computing needs, including enhancements in handling large-scale operations and cloud integration.

#### Why: Benefits of Using SQL Databases in Resumable Systems
- **Data Integrity and ACID Properties**: Stress the importance of data integrity, particularly the ACID properties (Atomicity, Consistency, Isolation, Durability) that are crucial for ensuring that transactions are processed reliably, which is vital in resumable systems.
- **Recovery Mechanisms**: Highlight the built-in mechanisms for data recovery and backup solutions that SQL databases offer, making them suitable for systems where resumability and data preservation are essential.


#### How: Implementing Resumability with SQL Databases
- **Basic Examples**:In Python, managing database transactions can be done effectively using the `sqlite3` library. Transactions in SQL databases like SQLite allow you to execute multiple operations in a safe, atomic manner. If an error occurs during one of the operations, you can roll back to the original state as if none of the operations had happened. This feature is crucial for implementing resumability because it ensures data integrity and consistency.

    Here’s how to manage transactions in Python with `sqlite3`:


```python
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def execute_transaction(conn):
    try:
        # start a transaction
        conn.execute('BEGIN TRANSACTION;')
        print("Transaction started.")
        
        # create table
        conn.execute('''CREATE TABLE IF NOT EXISTS Users (
                            UserID INT PRIMARY KEY,
                            FirstName VARCHAR(50),
                            LastName VARCHAR(50),
                            Email VARCHAR(100) UNIQUE,
                            RegistrationDate DATE
                        );''')
        
        # Insert data into table
        conn.execute("INSERT INTO Users (FirstName, LastName, Email) VALUES (?, ?, ?);",
                     ('John', 'Doe', 'john.doe@example.com'))
        print("Data inserted.")

        # Create a savepoint
        conn.execute("SAVEPOINT Savepoint1;")
        print("Savepoint created.")

        # Insert more data
        conn.execute("INSERT INTO Users (FirstName, LastName, Email) VALUES (?, ?, ?);",
                     ('Jane', 'Smith', 'jane.smith@example.com'))
        print("More data inserted.")

        # Assume an error occurred, rollback to savepoint
        conn.execute("ROLLBACK TRANSACTION TO Savepoint1;")
        print("Rolled back to savepoint.")

        # Continue with transaction
        conn.execute("INSERT INTO Users (FirstName, LastName, Email) VALUES (?, ?, ?);",
                     ('Alice', 'Johnson', 'alice.johnson@example.com'))
        print("Additional data inserted after rollback.")

        # Commit transaction
        conn.commit()
        print("Transaction committed.")
    except Error as e:
        # Rollback the entire transaction in case of error
        conn.rollback()
        print("Transaction failed and rolled back due to error:", e)

# Example usage
if __name__ == '__main__':
    print('```')
    database = "example.db"
    conn = create_connection(database)
    if conn is None:
        raise Exception("Failed to connect to the database.")
    
    execute_transaction(conn)
    conn.close()
    print('```')
```

    ```
    Transaction started.
    Data inserted.
    Savepoint created.
    More data inserted.
    Rolled back to savepoint.
    Additional data inserted after rollback.
    Transaction committed.
    ```
    

  - **Explanation of the Code**:
    - **Connection Establishment**: The `create_connection` function establishes a connection to the SQLite database.
    - **Transaction Management**: The `execute_transaction` function starts a transaction and performs several operations. It uses a savepoint to mark a position in the transaction that it can roll back to if an error occurs or if certain conditions are met.
    - **Savepoints and Rollbacks**: The script inserts some data, sets a savepoint, and then inserts more data. It then simulates an error or change in condition by rolling back to the savepoint, effectively undoing the second insert but keeping the first.
    - **Committing the Transaction**: After correcting the situation or performing additional operations, the transaction is committed, making all changes permanent in the database.
    - **Error Handling**: If an exception is raised during the transaction, the entire transaction is rolled back, ensuring the database remains consistent.

- **Practical Example (for MachineA)**: Using SQL Transactions for Resumability: In this example, we'll use an SQLite database to manage the state of a hypothetical `MachineA`. The database will store the machine's state, and we'll use SQL transactions to ensure all state changes are consistent and recoverable. Here’s how you can implement it:


```python
############# same as before

import math
import random
class MachineA:
    def __init__(self, initial_orientation=0, initial_position=(0, 0)):
        # Initialize the machine with orientation and position
        self.orientation = initial_orientation  # In degrees, 0 pointing east( x+ )
        self.position = list(initial_position)  # Position as a list [x, y]

    def turn_left(self, degrees):
        # Turn the machine left by a certain degree
        self.orientation = (self.orientation + degrees) % 360
        print(f"Turned left {degrees} degrees. New orientation: {self.orientation}")
        return self.random_crash()

    def turn_right(self, degrees):
        # Turn the machine right by a certain degree
        self.orientation = (self.orientation - degrees) % 360
        print(f"Turned right {degrees} degrees. New orientation: {self.orientation}")
        return self.random_crash()

    def move_forward(self, distance):
        # Move the machine forward in the direction of the current orientation
        radian = math.radians(self.orientation)
        self.position[0] += distance * math.cos(radian)  # x position changes
        self.position[1] += distance * math.sin(radian)  # y position changes
        print(f"Moved forward {distance} distance. New position: {self.position}")
        return self.random_crash()

    def move_backward(self, distance):
        # Move the machine backward opposite to the current orientation
        radian = math.radians(self.orientation)
        self.position[0] -= distance * math.cos(radian)  # x position changes
        self.position[1] -= distance * math.sin(radian)  # y position changes
        print(f"Reversed {distance} distance. New position: {self.position}")
        return self.random_crash()

    def get_machine_state(self):
        return self.orientation,self.position
    
    def random_crash(self):
        if random.random() > 0.6:
            print('!!!!!!!!!This machine crashed, auto reset!!!!!!!!!')
            self.reset()
            return False
        else:
            return True

    def reset(self):
        # Reset the machine to the initial state
        self.orientation = 0
        self.position = [0, 0]
        print("Machine has been reset to the 0,(0,0) state.")
############# end same as before

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def save_machine_state(conn, machine):
    try:
        with conn:
            # Begin a transaction
            conn.execute("BEGIN;")
            state = machine.get_machine_state()
            # Insert the machine state
            conn.execute("INSERT INTO MachineState (Orientation, PositionX, PositionY ) VALUES (?, ?, ?);", [state[0],*state[1]])
            # Commit the changes
            conn.commit()
            print("Machine state saved: Orientation {}, Position {}".format(*state))
    except Error as e:
        # Rollback in case of error
        conn.rollback()
        print("Failed to save state, rolled back transaction:", e)

def get_last_machine_state(conn):
    """ Retrieve the last saved state of the machine """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Orientation, PositionX, PositionY FROM MachineState ORDER BY Id DESC LIMIT 1;")
        state = cursor.fetchone()
        if state:
            print("Last machine state retrieved: Orientation {}, (PositionX, PositionY) {}".format(*state))
            return (state[0],(state[1],state[2]))
        else:
            print("No previous state found.")
            return (0,(0,0))
    except Error as e:
        print("Error retrieving the last state:", e)
        return None

def setup_database(conn):
    # Create a table for storing machine state
    conn.execute('''CREATE TABLE IF NOT EXISTS MachineState (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Orientation NUMBER NOT NULL,
                        PositionX NUMBER NOT NULL,
                        PositionY NUMBER NOT NULL);''')
    print("Database setup complete.")


def main():
    conn = create_connection("machine_state.db")
    if conn is None: return
    
    setup_database(conn)

    # Retrieve the last known state and initialize MachineA with it
    machine = MachineA()
    save_machine_state(conn, machine)

    while not machine.turn_left(90): # try action untill success
        machine = MachineA(*get_last_machine_state(conn)) # recover machine by last state
    save_machine_state(conn, machine) # reord when success

    while not machine.move_forward(10):        
        machine = MachineA(*get_last_machine_state(conn))
    save_machine_state(conn, machine)
        
    print(machine.get_machine_state())

    while not machine.turn_right(90):
        machine = MachineA(*get_last_machine_state(conn))
    save_machine_state(conn, machine)

    while not machine.move_backward(5):
        machine = MachineA(*get_last_machine_state(conn))
    save_machine_state(conn, machine)
        
    print(machine.get_machine_state())
    # Close connection
    conn.close()

if __name__ == '__main__':    
    print('```')
    main()    
    print('```')
```

    ```
    Database setup complete.
    Machine state saved: Orientation 0, Position [0, 0]
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Last machine state retrieved: Orientation 0, (PositionX, PositionY) 0
    Turned left 90 degrees. New orientation: 90
    Machine state saved: Orientation 90, Position [0, 0]
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    Machine state saved: Orientation 90, Position [6.123233995736766e-16, 10.0]
    (90, [6.123233995736766e-16, 10.0])
    Turned right 90 degrees. New orientation: 0
    Machine state saved: Orientation 0, Position [6.123233995736766e-16, 10.0]
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Last machine state retrieved: Orientation 0, (PositionX, PositionY) 6.123233995736766e-16
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    Machine state saved: Orientation 0, Position [-4.999999999999999, 10.0]
    (0, [-4.999999999999999, 10.0])
    ```
    

  - Key Aspects of This Example:

    - **Database Setup**: This involves initializing a SQLite database and creating a table specifically designed to store the operational state of `MachineA`. The setup might look something like this:
      ```python
        conn.execute("""
        CREATE TABLE IF NOT EXISTS MachineState (
                          Id INTEGER PRIMARY KEY AUTOINCREMENT,
                          Orientation NUMBER NOT NULL,
                          PositionX NUMBER NOT NULL,
                          PositionY NUMBER NOT NULL);
        """)
      ```
      This table is structured to automatically record the time of each state change alongside the state itself, which aids in tracking and debugging.

    - **State Management**: The code uses SQL transactions to manage changes to the machine's state. This ensures that all operations related to a single state change are treated as a single atomic unit. If any part of the transaction fails, the entire transaction is rolled back to the previous consistent state, thus preventing partial updates and ensuring data integrity. 

    - **Action and State Recovery**: Every significant action performed on `MachineA` triggers a corresponding update to the database. This method ensures that the machine's state is continually recorded. If an unexpected shutdown or failure occurs, the system can revert to or resume from the last successfully recorded state. This functionality is critical for maintaining the continuity and reliability of operations, especially in automated or semi-automated systems.

  - Additional Notes
    - **Complexity**: Managing state with transactions adds a layer of complexity to system design (especially **table design**). Developers must carefully handle transaction scopes, ensure proper rollback on failures, and maintain database performance under high-throughput conditions. Thorough testing is required to ensure the system behaves as expected under various failure scenarios.
    - **Advanced Tool: Using SQLAlchemy**: To manage database interactions more robustly and elegantly, SQLAlchemy, an SQL toolkit and Object-Relational Mapping (ORM) system for Python, can be employed. SQLAlchemy provides a high-level abstraction to interact with the database, allowing developers to write Pythonic code rather than SQL queries. It supports a wide range of SQL constructs, transaction management, and automatic rollback mechanisms, which are ideal for implementing complex transactional logic required in resumable systems.
      ```python
        from sqlalchemy import create_engine, Table, Column, Integer, MetaData, NUMBER
        from sqlalchemy.orm import sessionmaker
        
        engine = create_engine('sqlite:///example.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        metadata = MetaData()

        machine_state = Table('MachineState', metadata,
                              Column('Id', Integer, primary_key=True),
                              Column('Orientation', NUMBER),
                              Column('PositionX', NUMBER),
                              Column('PositionY', NUMBER)
                              )
        
        metadata.create_all(engine)  # Create tables based on metadata definition

        try:
            # Using SQLAlchemy's ORM to handle transactions
            new_state = machine_state.insert().values(MachineState='Operational')
            session.execute(new_state)
            session.commit()
        except:
            session.rollback()
            print("Error updating machine state.")
        finally:
            session.close()
      ```
    - **Migration Strategy**: migrating a SQL database, particularly when there are **slight changes** to table schemas, it's crucial to ensure that data integrity is maintained and downtime is minimized.
      - **Create Migration Scripts**: Write SQL scripts that modify the database schema. These scripts should be idempotent, meaning they can be run multiple times without causing issues.
        
      - **Examples of Migration Scripts**:
        ```sql
          -- Adding a Column
          ALTER TABLE my_table ADD COLUMN new_column VARCHAR(255) NULL;
          -- Changing Data Type
          ALTER TABLE my_table ALTER COLUMN existing_column TYPE new_type;
          -- Dropping a Column
          ALTER TABLE my_table DROP COLUMN old_column;
        ```

### Section 2: Key-Value Databases

#### What: Understanding Key-Value Databases
- **Definition**: Key-value databases store data as a collection of key-value pairs where each key is unique. This structure provides a straightforward and flexible way to store data, as the keys function as unique identifiers for accessing their corresponding values quickly.
- **Examples**: 
    - **Redis**
        - **Description**: An open-source, in-memory key-value store known for its speed and flexibility. It supports various data structures like strings, lists, sets, hashes, and more.
        - **Common Use**: Often used for caching, session management, pub/sub applications, and leaderboards in gaming applications.
        - **Example**: Storing user sessions in a web application.
            ```python
            import redis
            r = redis.Redis(host='localhost', port=6379, db=0)
            r.set('user123', 'session_data_here')
            print(r.get('user123'))
            ```
    - **MongoDB**
        - **Description**: MongoDB is a document database with the scalability and flexibility that you want with the querying and indexing that you need. It stores data in JSON-like documents, which makes the data structure both flexible and expressive.
        - **Common Use**: Often used for handling large sets of distributed data, MongoDB is suitable for real-time analytics and high speed logging, configuration, or caching.
        - **Example**: Storing user preferences in a flexible schema.
            ```python
            from pymongo import MongoClient

            # Connecting to the MongoDB server
            client = MongoClient('mongodb://localhost:27017/')

            # Selecting the database and collection
            db = client.user_preferences
            collection = db.preferences

            # Inserting a key-value pair into the database
            collection.insert_one({'user_id': 'user123', 'preferences': {'theme': 'dark', 'notifications': 'enabled'}})

            # Retrieving the value by key
            user_preferences = collection.find_one({'user_id': 'user123'})
            print(user_preferences['preferences'])
            ```
    - **Amazon DynamoDB**
        - **Description**: A fully-managed NoSQL database service that supports both key-value and document data models. Offers built-in security, backup and restore, and in-memory caching.
        - **Common Use**: Suitable for all applications that need consistent, single-digit millisecond latency at any scale.
        - **Example**: Storing order information in an e-commerce platform.
            ```python
            import boto3
            dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
            table = dynamodb.Table('Orders')
            table.put_item(
                Item={
                    'OrderId': '001',
                    'OrderData': 'Details of the order here'
                }
            )
            response = table.get_item(Key={'OrderId': '001'})
            print(response['Item'])
            ```

- **Simplicity and Performance**: Unlike relational databases that require data to be stored in tables with a predefined schema, key-value stores are schema-less. This simplicity results in fewer overheads and potentially faster performance, particularly for lookup queries.
- **Schema-less**: Since schema-less databases do not require a fixed schema, we can easily modify the data format **without needing to migrate** the entire database. This is especially useful for applications that evolve rapidly or require frequent changes to the data structure.

#### Who: Users of Key-Value Databases
- **Target Users**: Developers and companies that require rapid, scalable, and flexible storage solutions for large amounts of unstructured data. Key-value databases are popular in scenarios that require high-speed lookups, such as caching and session storage.
- **Industries**: Widely used in tech industries, especially in areas like gaming, advertising technology, and real-time analytics, where quick data retrieval is crucial.
#### Where: Applications of Key-Value Databases in Resumable Systems
- **Use Cases**: Key-value stores are ideal for applications that need to manage large volumes of state information rapidly, such as web session data, user preferences, and temporary data in distributed applications.
- **Environment**: They are commonly implemented in environments that require high throughput and low-latency data access, and are often used as part of a larger microservices architecture to enhance scalability and resiliency.

#### When: Choosing Key-Value Databases
- **Scenarios for Use**: Best suited for applications where quick data access, minimal response time, and horizontal scalability are more critical than complex data relationships and data integrity guarantees.
- **Advantages Over Other Databases**: Particularly effective when the application does not require joins or complex transactions but does need efficient, scalable access to data with a simple query pattern.

#### Why: Benefits of Using Key-Value Databases in Resumable Systems
- **Speed and Efficiency**: The flat structure allows for very fast data retrieval using keys, making key-value stores particularly useful for performance-critical applications.
- **Scalability**: Typically easier to scale horizontally compared to relational databases, as they are designed to distribute data across multiple nodes effectively.
- **Flexibility**: Schema-less nature means that the data model can easily evolve without the need for migrations or downtime, which is beneficial in dynamic environments where application requirements frequently change.

#### How: Implementing Resumability with Key-Value Databases
- **Basic Example with MongoDB:**: MongoDB, a NoSQL document-oriented database, offers flexibility and resilience that are advantageous for implementing resumable systems. 
Here's the assembled Python code block for managing a MongoDB-based implementation of the `Users` table.


```python
from pymongo import MongoClient, errors

# Establishing MongoDB connection
client = MongoClient('mongodb://localhost:27017/')

# 'resumable_db' is the name of the database where the users' data will be stored.
# If 'resumable_db' does not exist, MongoDB will create it automatically when data is first written.
db = client.get_database("resumable_db")

# Accessing the collection
# 'users' is the collection within the 'resumable_db' database where user documents will be stored.
# Similar to the database, if the 'users' collection does not exist, it will be created on the first insert operation.
users_collection = db.get_collection("users")

# Function to insert a new user
def insert_user(user_data):
    if users_collection.find_one({"Email": user_data['Email']}):
        print("User already exists.")
    else:
        try:
            users_collection.insert_one(user_data)
            print("User added.")
        except errors.ConnectionFailure:
            print("Connection failed. Attempting to resume...")
            # Additional logic to handle resumption would be implemented here

# Example of adding a new user
user_data = {
    "UserID": 2,
    "FirstName": "Jane",
    "LastName": "Roe",
    "Email": "jane.roe@example.com",
    "RegistrationDate": "2024-02-01"
}

print('```')
insert_user(user_data)
print('```')
```

    ```
    User already exists.
    ```
    

- **Practical Example (for MachineA)**: (Using MongoDB for Resumability) In this MongoDB-based example, we'll manage the state of a hypothetical MachineA. Instead of using SQL transactions, we'll leverage MongoDB's document model to store the machine's state, employing operations that ensure data consistency and can be resumed if interrupted.
Here's how we can implement it:


```python
############# same as before

import math
import random
class MachineA:
    def __init__(self, initial_orientation=0, initial_position=(0, 0)):
        # Initialize the machine with orientation and position
        self.orientation = initial_orientation  # In degrees, 0 pointing east( x+ )
        self.position = list(initial_position)  # Position as a list [x, y]

    def turn_left(self, degrees):
        # Turn the machine left by a certain degree
        self.orientation = (self.orientation + degrees) % 360
        print(f"Turned left {degrees} degrees. New orientation: {self.orientation}")
        return self.random_crash()

    def turn_right(self, degrees):
        # Turn the machine right by a certain degree
        self.orientation = (self.orientation - degrees) % 360
        print(f"Turned right {degrees} degrees. New orientation: {self.orientation}")
        return self.random_crash()

    def move_forward(self, distance):
        # Move the machine forward in the direction of the current orientation
        radian = math.radians(self.orientation)
        self.position[0] += distance * math.cos(radian)  # x position changes
        self.position[1] += distance * math.sin(radian)  # y position changes
        print(f"Moved forward {distance} distance. New position: {self.position}")
        return self.random_crash()

    def move_backward(self, distance):
        # Move the machine backward opposite to the current orientation
        radian = math.radians(self.orientation)
        self.position[0] -= distance * math.cos(radian)  # x position changes
        self.position[1] -= distance * math.sin(radian)  # y position changes
        print(f"Reversed {distance} distance. New position: {self.position}")
        return self.random_crash()

    def get_machine_state(self):
        return self.orientation,self.position
    
    def random_crash(self):
        if random.random() > 0.6:
            print('!!!!!!!!!This machine crashed, auto reset!!!!!!!!!')
            self.reset()
            return False
        else:
            return True

    def reset(self):
        # Reset the machine to the initial state
        self.orientation = 0
        self.position = [0, 0]
        print("Machine has been reset to the 0,(0,0) state.")
############# end same as before

from pymongo import MongoClient, errors, database

def create_connection():
    """ Create a database connection to a MongoDB database """
    try:
        return MongoClient('mongodb://localhost:27017/')
    except errors.ConnectionFailure as e:
        print("Connection error:", e)
    return None

def save_machine_state(client:MongoClient, machine:MachineA):
    try:
        orientation,position = machine.get_machine_state()
        # Insert the machine state
        result = client.get_database("machine_states_db").get_collection("MachineState").insert_one({
            "orientation":orientation,"position":position})
        print("Machine state saved: Orientation {}, Position {}".format(orientation, position))
    except errors.PyMongoError as e:
        print("Failed to save state:", e)

def get_last_machine_state(client:MongoClient):
    """ Retrieve the last saved state of the machine """
    try:
        cursor = client.get_database("machine_states_db").get_collection("MachineState").find().sort('_id', -1).limit(1)
        state = list(cursor)
        state = state[0] if len(state) > 0 else None
        if state:
            print("Last machine state retrieved: Orientation {}, Position {}".format(state["orientation"], state["position"]))
            return state["orientation"], state["position"]
        else:
            print("No previous state found.")
            return (0, (0, 0))
    except errors.PyMongoError as e:
        print("Error retrieving the last state:", e)
        return None

def setup_database(client:MongoClient):
    # Ensure the MachineState collection exists and is ready to store documents
    db = client.get_database("machine_states_db")
    if "MachineState" not in db.list_collection_names():
        db.create_collection("MachineState")
    print("Database setup complete.")



def main():
    conn = create_connection()
    if conn is None: return
    
    setup_database(conn)

    # Retrieve the last known state and initialize MachineA with it
    machine = MachineA()
    save_machine_state(conn, machine)

    while not machine.turn_left(90): # try action untill success
        machine = MachineA(*get_last_machine_state(conn)) # recover machine by last state
    save_machine_state(conn, machine) # reord when success

    while not machine.move_forward(10):        
        machine = MachineA(*get_last_machine_state(conn))
    save_machine_state(conn, machine)
        
    print(machine.get_machine_state())

    while not machine.turn_right(90):
        machine = MachineA(*get_last_machine_state(conn))
    save_machine_state(conn, machine)

    while not machine.move_backward(5):
        machine = MachineA(*get_last_machine_state(conn))
    save_machine_state(conn, machine)
        
    print(machine.get_machine_state())
    # Close connection
    conn.close()

if __name__ == '__main__':
    print('```')
    main()
    print('```')
```

    ```
    Database setup complete.
    Machine state saved: Orientation 0, Position [0, 0]
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Last machine state retrieved: Orientation 0, Position [0, 0]
    Turned left 90 degrees. New orientation: 90
    Machine state saved: Orientation 90, Position [0, 0]
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Last machine state retrieved: Orientation 90, Position [0, 0]
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Last machine state retrieved: Orientation 90, Position [0, 0]
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    Machine state saved: Orientation 90, Position [6.123233995736766e-16, 10.0]
    (90, [6.123233995736766e-16, 10.0])
    Turned right 90 degrees. New orientation: 0
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Last machine state retrieved: Orientation 90, Position [6.123233995736766e-16, 10.0]
    Turned right 90 degrees. New orientation: 0
    Machine state saved: Orientation 0, Position [6.123233995736766e-16, 10.0]
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    Machine state saved: Orientation 0, Position [-4.999999999999999, 10.0]
    (0, [-4.999999999999999, 10.0])
    ```
    

### Conclusion
- **Summary**: Evaluate the pros and cons of each database type for resumable applications.
- **Future Outlook**: Consider future database technologies and trends.

### Additional Notes
- ...

## Chapter 4: Design Pattern of Model-View-Controller (MVC)

### Introduction

- **Overview**:
The Model-View-Controller (MVC) design pattern is pivotal in the architecture of modern web applications. At its core, MVC divides application logic into three interconnected components: the Model, the View, and the Controller. This separation not only clarifies roles and responsibilities within the application but also enhances modularity and manageability. Particularly relevant to resumable web applications, MVC allows developers to create systems that can easily save their state and recover from interruptions or failures, making them robust and user-friendly.

- **Objective**:
This chapter aims to dissect the MVC pattern, illustrating its fundamental role in enforcing separation of concerns—a principle that dictates that each module or layer of an application should manage a specific and unique aspect of the application's functionality. By adhering to this principle, MVC enhances the modularity of code, which is essential for building resumable applications that can maintain their state over time or during unexpected interruptions. Through practical examples and detailed explanations, we will explore how leveraging MVC can lead to more reliable, maintainable, and resumable web applications.

## Section 1: Components of MVC
The MVC design pattern is structured around three core components that interact seamlessly to separate the concerns of input, processing, and output. Understanding each component is crucial for leveraging MVC effectively in the development of resumable web applications. This section provides a detailed exploration of the Model, View, and Controller components.

- **Model**: The Model represents the application's dynamic data structure, independent of the user interface. It directly manages the data, logic, and rules of the application. In the context of resumable applications, the Model is crucial as it not only holds the data but also the state information necessary to resume processes from a paused state. By encapsulating the state within the Model, applications can ensure data consistency and integrity throughout the lifecycle of the application and across different sessions.
    - **Example**:
        In a Python MVC framework, the Model would be responsible for data access and business logic. Here's a simple example of a Python Model that uses SQLite to manage the state of a `Book` object:

        ```python
        import sqlite3
        class BookModel:
            def __init__(self, book_id, title, author):
                self.book_id = book_id
                self.title = title
                self.author = author

            def save(self):
                conn = sqlite3.connect('library.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (self.title, self.author))
                self.book_id = cursor.lastrowid
                conn.commit()
                conn.close()

            def update(self):
                conn = sqlite3.connect('library.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE books SET title = ?, author = ? WHERE id = ?", (self.title, self.author, self.book_id))
                conn.commit()
                conn.close()
        ```

- **View**: The View component is responsible for rendering the Model’s data to the user and specifying exactly how that data should appear. It is the visual representation of the Model, making it an integral part of creating a responsive and engaging user experience. In resumable systems, the View can restore its state by querying the current status from the Model, thus allowing the user interface to reflect the application's state at the point of interruption. This ability makes it straightforward to provide users with a seamless experience, even in 
    - **Example**:
    The View in Python might be a simple function that outputs data to the console or a complex GUI interface. Here’s an example using a console-based View:
    
        ```python
        class BookView:
            def display_book(self, book:BookModel):
                if book.book_id:
                    print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
                else:
                    print("No book found.")

            def display_error(self, message):
                print(f"Error: {message}")
        ```

- **Controller**: The Controller acts as an intermediary between the Model and the View, handling user input and converting it into commands for the Model or View. It receives input, optionally validates it, and then passes the input to the Model to affect the data state or to the View to change the display. In resumable web applications, the Controller plays a key role by managing the flow of data and ensuring that state transitions are handled smoothly, enabling the application to pause and resume gracefully.
    - **Example**:
    The Controller processes user input, interacts with the Model, and updates the View. Here's an example of a Python Controller for managing books:

        ```python
        class BookController:
            def __init__(self):
                # Initialize the database at the start
                BooksModel.initialize()

            def add_book(self, title, author):
                if not title or not author:
                    book_view.display_error("Title and author cannot be empty")
                    return
                new_book = BookModel(None, title, author)
                new_book.save()
                print("Book added successfully.")

            def update_book(self, book_id, title, author):
                book = BooksModel.get_book(book_id)
                if book:
                    book.title = title
                    book.author = author
                    book.update()
                    print("Book updated successfully.")
                else:
                    book_view.display_error("Book not found.")

            def view_book(self, book_id):
                book = BooksModel.get_book(book_id)
                if book:
                    book_view.display_book(book)
                else:
                    book_view.display_error("Book not found.")

            def list_books(self):
                books = BooksModel.get_all_books()
                for book in books:
                    book_view.display_book(book)
        ```

These examples demonstrate how Python can be used to implement each part of the MVC architecture, making it clear how data flows through the application and how state management can be encapsulated within these components for building resumable web applications.


```python
import sqlite3
    
class BookModel:
    def __init__(self, book_id=None, title=None, author=None):
        self.init_book(book_id, title, author)
    
    def init_book(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        return self

    def save(self): LibraryController.save_book(self)
    def update(self): LibraryController.update_book(self)

"Here is an example for an SQL controller. Trying to build a Key-Value version will be very interesting!"
class LibraryController:
    @staticmethod
    def sqlite3_query(query,vals=None,cursor_executed_callback=lambda x:x, db_name='library.db'):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        if vals is None:
            cursor.execute(query)
        else:
            cursor.execute(query,vals)
        cursor_executed_callback(cursor)
        conn.commit()
        conn.close()
        
    @staticmethod
    def initialize():
        LibraryController.sqlite3_query("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)")
        
    @staticmethod
    def get_book(book_id):
        book = BookModel()
        LibraryController.sqlite3_query("SELECT id, title, author FROM books WHERE id = ?",
                      (book_id,),
                      lambda cursor:book.init_book(*cursor.fetchone()))
        return book if book.book_id else None

    @staticmethod
    def get_all_books():
        res = []
        LibraryController.sqlite3_query("SELECT id, title, author FROM books",None,
                      lambda cursor:[
                          res.append(BookModel(*row)) for row in cursor.fetchall()])
        return res   
    
    @staticmethod
    def save_book(book:BookModel):
        LibraryController.sqlite3_query("INSERT INTO books (title, author) VALUES (?, ?)",
                      (book.title, book.author),
                      lambda cursor:book.init_book(cursor.lastrowid,book.title,book.author))
        
    def update_book(book:BookModel):
        LibraryController.sqlite3_query("UPDATE books SET title = ?, author = ? WHERE id = ?",
                      (book.title, book.author, book.book_id))

class BookView:
    def display_book(self, book:BookModel):
        if book.book_id:
            print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
        else:
            print("No book found.")

    def display_error(self, message):
        print(f"Error: {message}")

class BookController:
    def __init__(self):
        # Initialize the database at the start
        LibraryController.initialize()

    def add_book(self, title, author):
        if not title or not author:
            BookView().display_error("Title and author cannot be empty")
            return
        BookModel(None, title, author).save()
        print("Book added successfully.")

    def update_book(self, book_id, title, author):
        book = LibraryController.get_book(book_id)
        if book:
            book.init_book(book_id,title,author).update()
            print("Book updated successfully.")
        else:
            BookView().display_error("Book not found.")

    def view_book(self, book_id):
        book = LibraryController.get_book(book_id)
        if book:
            BookView().display_book(book)
        else:
            BookView().display_error("Book not found.")

    def list_books(self):
        books = LibraryController.get_all_books()
        for book in books:
            BookView().display_book(book)


# Example of using the MVC components
print('```')
controller = BookController()
controller.add_book("1984", "George Orwell")
controller.add_book("Brave New World", "Aldous Huxley")
controller.view_book(1)
controller.update_book(1, "1984", "George Orwell - Updated")
controller.list_books()
print('```')
```

    ```
    Book added successfully.
    Book added successfully.
    Book ID: 1, Title: 1984, Author: George Orwell
    Book updated successfully.
    Book ID: 1, Title: 1984, Author: George Orwell - Updated
    Book ID: 2, Title: Brave New World, Author: Aldous Huxley
    ```
    

### Section 2: MVC in Resumability

- **Introduction to MVC in Resumability**:
The Model-View-Controller (MVC) architecture pattern is a well-established design paradigm used to separate concerns within an application, making it easier to manage and scale. In the context of resumable programming, MVC can play a pivotal role by structuring applications in a way that supports interruption and resumption of processes without loss of state or behavior.

    - **Model**:
    In resumable MVC, the Model represents not only the data but also the state of the application. This includes any ongoing processes, intermediate results, and checkpoints that enable the application to pause and resume operations seamlessly. Implementing persistent or serialized state management within the model ensures that data can be restored or rolled back to a consistent state after an interruption.

    - **View**:
    The View in a resumable system needs to dynamically reflect changes in the model's state, accommodating interruptions and resumptions. This requires the view components to be aware of the resumability aspects of the model, **possibly subscribing to state change notifications** and being able to render partial states when resuming from interruptions.

    - **Controller**:
    Controllers in a resumable MVC architecture are responsible for handling user inputs, inter-process communication, and managing the flow of control in scenarios where operations can be paused and resumed. The controllers must be capable of initiating, pausing, and resuming tasks. They also need to handle the logistics of saving and restoring state, coordinating these actions with the model and the view.

- **Implementing Resumability in MVC**:
To implement resumability in MVC, one can use various techniques such as:
    - **Persistent Storage:** Storing the states of the application in a database or other durable storage solutions ensures that the model can recover the same state even after a shutdown or crash. This technique is crucial for long-running applications which might experience unpredictable interruptions.
    - **Model Serialization:** Serializing the model allows for saving a snapshot of the application's state at various points, making it easier to restore to these points after failure. Serialization can be particularly useful in environments where changes to the state are frequent and need to be captured incrementally.
    - **View Event Sourcing:** Utilizing event sourcing for views means recording every change to the view state as a sequence of events. This approach not only allows the view to be reconstructed to any past state but also helps in maintaining consistency between the model and view during resumptions.
    - **Controller Handling Range:** Controllers should be designed to handle a range of operations from initiating and pausing tasks to complex error handling and state recovery scenarios. This flexibility is key to managing user interactions and system processes reliably across interruptions.
    - **Checkpointing for Resumability:** Implementing checkpoints within the application flow allows the system to save its state at regular intervals or at critical points. This makes it possible to resume operations smoothly after a pause or failure, minimizing the loss of data and user inputs.

- **Example in MVC (using Key-Value Store)**:To incorporate the `MachineA` class into an MVC design similar to the one we used for the book model, we'll define a corresponding controller, model, and view. Since `MachineA` contains operations that affect its state (like moving and turning), our model will handle these state changes, while the controller will handle user interactions, and the view will present the state or results to the user. We'll also use shelve for persistent storage.

Here's how we can design the MVC components for `MachineA`:



```python
import shelve
import math
import random
import os

# exactly this is Machine (state) Model
class MachineAModel:
    def __init__(self, machine_id=None, initial_orientation=0, initial_position=(0, 0)):
        # Initialize the machine with orientation and position
        self.orientation = initial_orientation  # In degrees, 0 pointing east( x+ )
        self.position = list(initial_position)  # Position as a list [x, y]
        
        # exactly this is machine (state) id
        self._machine_id = machine_id

    def get_machine_state(self):
        return self.orientation,self.position
        
    def soft_reset(self):
        # Reset the machine to the initial state in scope of instance
        self.orientation = 0
        self.position = [0, 0]
        print("Machine has been reset to the 0,(0,0) state.")

class MachineLibrary:
    db_path = "machine.db"

    @staticmethod
    def open_shelve_db():
        if not os.path.exists(MachineLibrary.db_path):
            with shelve.open(MachineLibrary.db_path, writeback=True) as db:
                yield db
        return

    @staticmethod
    def initialize():
        for db in MachineLibrary.open_shelve_db(): pass

    @staticmethod
    def get_machine(machine_id):
        for db in MachineLibrary.open_shelve_db():
            if machine_id in db:
                machine_data = db[machine_id]
                return MachineAModel(machine_id, machine_data['orientation'], machine_data['position'])
        return None

    @staticmethod
    def save_machine(machine: MachineAModel):
        for db in MachineLibrary.open_shelve_db():
            machine_id = str(len(db) + 1)
            db[machine_id] = {'orientation': machine.orientation, 'position': machine.position}
            machine._machine_id = machine_id
        return machine

    @staticmethod
    def update_machine(machine: MachineAModel):
        for db in MachineLibrary.open_shelve_db():
            if machine._machine_id in db:
                db[machine._machine_id] = {'orientation': machine.orientation, 'position': machine.position}        
        return machine

    @staticmethod
    def reset_machine(machine_id):
        for db in MachineLibrary.open_shelve_db():
            if machine_id in db:
                db[machine_id] = {'orientation': 0, 'position': [0, 0]}
                return True
        return False

class MachineView:
    def display_machine(self, machine: MachineAModel):
        print(f"Machine ID: {machine._machine_id}, Orientation: {machine.orientation}, Position: {machine.position}")

    def display_error(self, message):
        print(f"Error: {message}")

class MachineController:
    ##############################################
    def __init__(self,model=None):
        MachineLibrary.initialize()
        self.model=model

    def add_machine(self, initial_orientation=0, initial_position=(0, 0)):
        self.model = machine = MachineLibrary.save_machine(
                        MachineAModel(None, initial_orientation, initial_position))
        print("Machine added successfully.")
        return machine

    def hard_reset_machine(self, machine_id):
        # reset machine in scope of database!!!
        if MachineLibrary.reset_machine(machine_id):
            print(f"Machine {machine_id} reset successfully.")
        else:
            MachineView().display_error("Machine not found.")
        self.model=MachineLibrary.get_machine(machine_id)

    def view_machine(self, machine_id=None):
        machine = MachineLibrary.get_machine(machine_id if machine_id else self.model.machine_id)
        if machine:
            MachineView().display_machine(machine)
        else:
            MachineView().display_error("Machine not found.")
    
    ##############################################
    def turn_left(self, degrees):
        # Turn the machine left by a certain degree
        self.model.orientation = (self.model.orientation + degrees) % 360
        print(f"Turned left {degrees} degrees. New orientation: {self.model.orientation}")
        return self.random_crash()

    def turn_right(self, degrees):
        # Turn the machine right by a certain degree
        self.model.orientation = (self.model.orientation - degrees) % 360
        print(f"Turned right {degrees} degrees. New orientation: {self.model.orientation}")
        return self.random_crash()

    def move_forward(self, distance):
        # Move the machine forward in the direction of the current orientation
        radian = math.radians(self.model.orientation)
        self.model.position[0] += distance * math.cos(radian)  # x position changes
        self.model.position[1] += distance * math.sin(radian)  # y position changes
        print(f"Moved forward {distance} distance. New position: {self.model.position}")
        return self.random_crash()

    def move_backward(self, distance):
        # Move the machine backward opposite to the current orientation
        radian = math.radians(self.model.orientation)
        self.model.position[0] -= distance * math.cos(radian)  # x position changes
        self.model.position[1] -= distance * math.sin(radian)  # y position changes
        print(f"Reversed {distance} distance. New position: {self.model.position}")
        return self.random_crash()
    
    def random_crash(self):
        if random.random() > 0.6:
            print('!!!!!!!!!This machine crashed, auto reset!!!!!!!!!')
            self.model.soft_reset()
            return False
        else:            
            self.model = MachineLibrary.update_machine(self.model) # save if success
            return True
        
# Example of Resumabe Implementation by using the MVC components
def main():
    controller = MachineController()
    machine = controller.add_machine(0,(0,0))
    machine_id = controller.model._machine_id

    while not controller.turn_left(90): # try action untill success
        machine = MachineLibrary.get_machine(machine_id) # recover machine by last state
        controller = MachineController(machine)          # recover controller by last machine

    while not controller.move_forward(10):        
        machine = MachineLibrary.get_machine(machine_id)
        controller = MachineController(machine)
        
    MachineView().display_machine(machine)

    while not controller.turn_right(90):
        machine = MachineLibrary.get_machine(machine_id)
        controller = MachineController(machine)

    while not controller.move_backward(5):
        machine = MachineLibrary.get_machine(machine_id)
        controller = MachineController(machine)
        
    MachineView().display_machine(machine)

if __name__ == '__main__':
    print('```')
    for i in range(1):
        main()
    print('```')
```

    ```
    Machine added successfully.
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Turned left 90 degrees. New orientation: 90
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    Machine ID: 3, Orientation: 90, Position: [6.123233995736766e-16, 10.0]
    Turned right 90 degrees. New orientation: 0
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Turned right 90 degrees. New orientation: 0
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    Machine ID: 3, Orientation: 0, Position: [-4.999999999999999, 10.0]
    ```
    

##### Explanation
- **MachineAModel** is a simple Python class representing the machine.
- **MachineLibrary** handles the shelve database operations similar to the book library example.
- **MachineView** provides methods to output the state of the machine and any errors.
- **MachineController** manages interactions such as adding, resetting, and viewing machines.

Incorporating resumability into the MVC architecture enhances the robustness and user experience of applications, especially in environments where interruptions are common or expected. By carefully designing the model, view, and controller to handle interruptions gracefully, developers can create more resilient and flexible applications.

(PS: The following code is the action recording version, which is also very important when the target model is hard to initialize with arguments.)


```python
import shelve
import math
import random
import copy
import datetime

class MachineAModel:
    def __init__(self, machine_id=None, initial_orientation=0, initial_position=(0, 0), actions=None):
        self.orientation = initial_orientation
        self.position = list(initial_position)
        self._machine_id = machine_id
        self.actions = actions if actions is not None else []

    def soft_reset(self):
        self.orientation = 0
        self.position = [0, 0]

class MachineLibrary:
    db_path = "machine.db"

    @staticmethod
    def with_db(func):
        def wrapper(*args, **kwargs):
            with shelve.open(MachineLibrary.db_path, writeback=True) as db:
                return func(db, *args, **kwargs)
        return wrapper

    @staticmethod
    @with_db
    def get_machine(db, machine_id):
        if machine_id in db:
            data:dict = db[machine_id]
            return MachineAModel(machine_id, data['orientation'], data['position'], data.get('actions', []))

    @staticmethod
    @with_db
    def save_machine(db, machine:MachineAModel)->MachineAModel:
        machine_id = machine._machine_id if machine._machine_id else str(len(db) + 1)
        db[machine_id] = {
            'orientation': machine.orientation,
            'position': machine.position,
            'actions': machine.actions
        }
        machine._machine_id = machine_id
        return machine

    @staticmethod
    def new_machine()->MachineAModel:
        return MachineLibrary.save_machine(MachineAModel(None, 0, (0, 0)))
    
    @staticmethod
    @with_db
    def reset_machine(db, machine_id):
        if machine_id in db:
            db[machine_id] = {'orientation': 0, 'position': [0, 0], 'actions': []}

class MachineView:
    @staticmethod
    def display_machine(machine:MachineAModel):
        print(f"Machine ID: {machine._machine_id}, Orientation: {machine.orientation}, Position: {machine.position}")

    @staticmethod
    def display_error(message):
        print(f"Error: {message}")

class MachineController:
    def __init__(self, model):
        self.model:MachineAModel = model
    
    def save_machine(self):
        MachineLibrary.save_machine(self.model)
        return self

    def action_with_record(self, action, *args):
        while not action(*args):
            self.replay_actions(copy.deepcopy(self.model.actions))
        self.record_action(action, *args)
        MachineLibrary.save_machine(self.model)
    
    def replay_actions(self,const_actions):
        actions:list = copy.deepcopy(const_actions)
        self.model = MachineLibrary.new_machine()
        while len(actions)>0:
            _, action_name, args = actions.pop(0)
            action = getattr(self, action_name)
            if not action(*args): # recover history actions
                actions:list = copy.deepcopy(const_actions) # recover failure and do init again
                self.model = MachineLibrary.new_machine()
            else:
                self.record_action(action, *args)
        return self
    
    def record_action(self, action, *args):
        # Record the action and the current timestamp
        self.model.actions.append((datetime.datetime.now().isoformat(), action.__name__, args))
        self.save_machine()

    # Movement and rotation methods follow similar patterns, with random_crash checks
    def turn_left(self, degrees):
        self.model.orientation = (self.model.orientation + degrees) % 360
        return self.random_crash()

    def turn_right(self, degrees):
        self.model.orientation = (self.model.orientation - degrees) % 360
        return self.random_crash()

    def move_forward(self, distance):
        radian = math.radians(self.model.orientation)
        self.model.position[0] += distance * math.cos(radian)
        self.model.position[1] += distance * math.sin(radian)
        return self.random_crash()

    def move_backward(self, distance):
        radian = math.radians(self.model.orientation)
        self.model.position[0] -= distance * math.cos(radian)
        self.model.position[1] -= distance * math.sin(radian)
        return self.random_crash()
    
    def random_crash(self):
        if random.random() > 0.6:
            print('Machine crashed, auto reset')
            self.model.soft_reset()
            return False
        return True

def main():
    new_conn = lambda:MachineController(MachineLibrary.new_machine())
    controller = new_conn()

    # MachineView.display_machine(controller.model)
    # controller.action_with_record(controller.turn_left,    90)
    # controller.action_with_record(controller.move_forward, 10)
    # MachineView.display_machine(controller.model)
    # controller.action_with_record(controller.turn_right,   90)
    # controller.action_with_record(controller.move_backward, 5)
    # MachineView.display_machine(controller.model)
    
    while not controller.turn_left(90): # try action untill success
        # recover controller by last machine
        controller = new_conn().replay_actions(controller.model.actions)
    controller.record_action(controller.turn_left, 90)
    
    while not controller.move_forward(10):
        controller = new_conn().replay_actions(controller.model.actions)
    controller.record_action(controller.move_forward,10)

    while not controller.turn_right(90):
        controller = new_conn().replay_actions(controller.model.actions)
    controller.record_action(controller.turn_right,90)
        
    MachineView().display_machine(controller.model)

    while not controller.move_backward( 5):
        controller = new_conn().replay_actions(controller.model.actions)
    controller.record_action(controller.move_backward, 5)

    MachineView().display_machine(controller.model)

if __name__ == '__main__':
    print('```')
    main()
    print('```')
```

    ```
    Machine ID: 6, Orientation: 0, Position: [6.123233995736766e-16, 10.0]
    Machine crashed, auto reset
    Machine crashed, auto reset
    Machine crashed, auto reset
    Machine crashed, auto reset
    Machine crashed, auto reset
    Machine crashed, auto reset
    Machine crashed, auto reset
    Machine crashed, auto reset
    Machine crashed, auto reset
    Machine crashed, auto reset
    Machine crashed, auto reset
    Machine crashed, auto reset
    Machine crashed, auto reset
    Machine ID: 20, Orientation: 0, Position: [-4.999999999999999, 10.0]
    ```
    

### Conclusion
The application of the MVC design pattern in your script allows for well-organized code with clear separation of concerns:
- **Separation of Concerns**: Each component has a distinct responsibility. The model manages the data, the view handles the presentation, and the controller bridges the two with business logic.    
- **Modularity**: The modular nature of MVC makes the script more maintainable and scalable. Each part can be modified independently without affecting the others. For instance, changes in the view presentation would not require changes in the model or controller.
- **Ease of Maintenance and Extendibility**: The clear division makes it easier to update and maintain the code. For example, adding new features, such as additional machine actions or different recovery strategies, can be done with minimal impact on the existing code structure.
- **Testability**: The separation allows for more straightforward unit testing of individual components, especially the business logic in the controller and the state management in the model.

### Additional Notes

- **Consideration of MachineAModel (Model)**:
   - Represents a virtual machine with attributes for orientation, position, and a list of actions.
   - Should be kept simple, akin to a data structure. Includes methods to get/set the model's state (soft, not persistent).
   - Should not perform persistent operations.
   - Focus on serialization and reconstruction.

- **Consideration of MachineLibrary (Controller)**:
   - MVC defines roles but not the number of classes.
   - Handles interactions (controlling) with **persistent storage** using the `shelve` library, such as retrieving and saving machine states.
   - The `with_db` decorator manages database connections and ensures they are closed properly.
   - Provides methods to create a new model, save a model's state, and reset a model's state in the database.

- **Consideration of MachineController (Controller)**:
   - Manages a specific machine model.
   - Includes methods to perform and record actions (e.g., turning, moving) with error handling that simulates random crashes by potentially resetting the machine.
   - Implements a recovery mechanism to restore (or replay actions from) the last known good state when a crash occurs.
   - Controls persistent operations.

- **Consideration of MachineView (View)**:
   - Contains static methods to display model details or errors, helping to separate the user interface logic from the business logic.



---

## Chapter 5: Design Pattern of Finite State Machine

### Introduction

- **Overview:** 
The state machine design pattern is a crucial methodology for managing state transitions in a systematic and predictable manner. This pattern is particularly valuable in resumable systems where the state of the application needs to be preserved and managed accurately across different stages or conditions of the process. State machines help in defining clear state transition rules, making the system easier to understand, debug, and maintain.

A state machine, in essence, consists of a finite number of states, transitions between these states based on events or conditions, and actions that are carried out in each state. This design pattern is widely applicable, from simple applications such as user interface management to more complex systems like network protocol operations or workflow management.

- **Objective:** 
This chapter aims to equip readers with the knowledge and tools to design and implement state machines in their software development projects. By understanding the principles and structure of state machines, developers can create more robust, error-resistant, and maintainable systems. The chapter will cover:

    - **Fundamental Concepts**: Introducing the basic components of state machines, including states, transitions, events, and actions.
    - **Design Techniques**: Offering strategies and best practices for designing effective state machines.
    - **Implementation Examples**: Providing concrete examples in popular programming languages to illustrate how state machines can be implemented in actual software projects.
    - **Common Pitfalls and Solutions**: Identifying typical challenges faced when designing and implementing state machines and providing solutions to overcome these issues.

By the end of this chapter, readers will not only understand the theoretical aspects of state machines but also gain practical insights into implementing them effectively in various programming environments. This knowledge will empower them to tackle complex state management issues in their resumable systems, enhancing both the performance and reliability of their applications.

### Section 1: Understanding State Machines

- Basics of State Machines
State machines are conceptual models used to describe a system in terms of its states, transitions between those states, and actions that are performed in each state. This section will outline the basic components of a state machine, which include states, transitions, and actions, and will demonstrate how these components can be used to model software behavior.

  - **States**: These represent the conditions or the status of a system at any given time. A state machine will have a finite number of states, and at any point, it must be in one of these states.

  - **Transitions**: Transitions are the movements from one state to another. A transition is triggered by an event or a condition. It's the pathway that connects two states.

  - **Actions**: Actions are tasks or operations that are performed when entering a state, exiting a state, or during a transition. Actions can depend on the state of the system or the transition taken.

- Example with Python: A Simple Traffic Light System
To illustrate how a state machine works, let's consider a simple example of a traffic light system. This system can be in one of three states: Red, Green, or Yellow. The transitions between these states occur after a timer expires, and each state transition can trigger specific actions like turning on a light.

Here's a simple implementation of **finite** state machine using Python:


```python
class TrafficLight:
    def __init__(self):
        # Start with the green light state
        self.state = TrafficLightGreenState()

    def to_Green(self):
        self.state.to_Green(self)
    def to_Yellow(self):
        self.state.to_Yellow(self)
    def to_Red(self):
        self.state.to_Red(self)

    def info(self):
        self.state.info()

class TrafficLightGreenState:
    def to_Green(self, traffic_light:TrafficLight):
        print("Already on Green light.")
    
    def to_Yellow(self, traffic_light:TrafficLight):
        traffic_light.state = TrafficLightYellowState()
        print("Transition to Yellow light.")
    
    def to_Red(self, traffic_light:TrafficLight):
        raise ValueError("Invalid transition from Green to Red.")

    def info(self):
        print("Green light is on. Cars can move.")

class TrafficLightYellowState:
    def to_Green(self, traffic_light:TrafficLight):
        raise ValueError("Invalid transition from Yellow to Green.")
    
    def to_Yellow(self, traffic_light:TrafficLight):
        print("Already on Yellow light.")
    
    def to_Red(self, traffic_light:TrafficLight):
        traffic_light.state = TrafficLightRedState()
        print("Transition to Red light.")

    def info(self):
        print("Yellow light is on. Please prepare to stop.")

class TrafficLightRedState:
    def to_Green(self, traffic_light:TrafficLight):
        traffic_light.state = TrafficLightGreenState()
        print("Transition to Green light.")
    
    def to_Yellow(self, traffic_light:TrafficLight):
        raise ValueError("Invalid transition from Red to Yellow.")
    
    def to_Red(self, traffic_light:TrafficLight):
        print("Already on Red light.")

    def info(self):
        print("Red light is on. Stop.")


# # Example Usage
print('```')
traffic_light = TrafficLight()
traffic_light.to_Green()
traffic_light.info()
traffic_light.to_Yellow()
traffic_light.info()
traffic_light.to_Red()
traffic_light.info()
print('```')
```

    ```
    Already on Green light.
    Green light is on. Cars can move.
    Transition to Yellow light.
    Yellow light is on. Please prepare to stop.
    Transition to Red light.
    Red light is on. Stop.
    ```
    

- Explanation of the Traffic Light **Finite** State Machine Implementation

    - **Core Classes and Methods:**
        - **TrafficLight Class:** Acts as the context for the state machine. It initializes with the green light state and provides methods to transition to green, yellow, or red states. It also includes an `info()` method to display the current state's information.
        
        - **Finite States:** TrafficLightGreenState, TrafficLightYellowState, TrafficLightRedState Classes, each class represents a specific state of the traffic light and includes methods for transitioning to other states. These methods either change the state of the `TrafficLight` context or raise an exception if an invalid transition is attempted.

    - **Key Features of the Implementation:**
        - **Encapsulation of State Behavior:** Each state class encapsulates the behavior and possible transitions from that state. This makes it clear what actions are possible from any given state and centralizes the control logic within each state class.
        
        - **Ease of Modification:** If the behavior or allowed transitions of a state need to change, only the corresponding state class needs to be modified. This simplifies maintenance and testing.

        - **Error Handling:** The state classes handle errors by preventing invalid transitions directly, using exceptions to enforce correct usage of the state machine.

Overall, this implementation effectively demonstrates the use of the finite state machine design pattern in managing complex state transitions in a simple and robust way. The separation of state behaviors into distinct classes ensures that the system remains flexible and easy to manage as complexities or requirements change.

### Section 2: Finite State Machine in Resumability

Finite State Machines (FSMs) are a powerful tool for managing the complexities of state in systems that require resumability. By clearly defining state transitions and actions, FSMs ensure that a system can pause and resume at any point without losing the context or consistency of its operations. This section will explore practical examples of how FSMs can be effectively used in various resumable systems, illustrating their versatility and utility.

- **Example 1: Task Management System**

    - **Scenario**: Consider a task management system used in a business process where tasks move through various stages (e.g., Initiation, Approval, Execution, Completion, Failure). Each task's progress needs to be tracked and managed even if the system experiences interruptions.

    - **Implementation**:
        - **States**: Initiation, Approval, Execution, Completion, Failure.
        - **Transitions**: Tasks move from Initiation to Approval, from Approval to Execution, and from Execution to Completion or Failure. Each transition might occur only after certain conditions are met, such as receiving approvals or completing previous tasks.
        - **Actions**: On entering each state, specific actions are triggered, such as sending notifications, updating task status, or logging activity for audit purposes.

    - **Resumability**: The state of each task is saved persistently in a database. If the workflow system stops or is interrupted, it can resume by reloading the state from the database and continuing from the last recorded state, ensuring no steps are skipped or repeated.


```python
import random
class Task:
    def __init__(self):
        self.state = InitiationState()

    def approve(self): self.state.approve(self)

    def execute(self): self.state.execute(self)

    def complete(self): self.state.complete(self)

    def failure(self): self.state.failure(self)

    def is_failure(self): return type(self.state) == FailureState

    def recover(self): self.state.recover(self)
    
    def info(self): self.state.info(self)

class TaskState:
    def approve(self, task:Task):
        raise NotImplementedError(f"This transition not valid at state from {self.__class__.__name__} to approve")

    def execute(self, task:Task):
        raise NotImplementedError(f"This transition not valid at state from {self.__class__.__name__} to execute")

    def complete(self, task:Task):
        raise NotImplementedError(f"This transition not valid at state from {self.__class__.__name__} to complete")

    def failure(self, task:Task):
        raise NotImplementedError(f"This transition not valid at state from {self.__class__.__name__} to failure")   
    
    def recover(self, task:Task):
        raise NotImplementedError(f"This transition not valid at state from {self.__class__.__name__} to recover")
    
    def info(self, task:Task):
        raise NotImplementedError(f"This method needs to be overridden.")

class InitiationState(TaskState):
    def approve(self, task:Task):
        task.state = ApprovalState()
        print("Task moved to Approval.")

    def info(self, task:Task):
        print("Task is in Initiation state. Awaiting approval.")

class ApprovalState(TaskState):
    def execute(self, task:Task):
        task.state = ExecutionState()
        print("Task moved to Execution.")

    def info(self, task:Task):
        print("Task is in Approval state. Awaiting execution.")

class ExecutionState(TaskState):
    def complete(self, task:Task):    
        # random_crash
        if random.random() > 0.6:
            print('!!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!')
            task.state = FailureState()
        else:
            task.state = CompletionState()
            print("Task moved to Completion.")

    def info(self, task:Task):
        print("Task is in Execution state. Awaiting completion.")

class CompletionState(TaskState):
    def info(self, task:Task):
        print("Task is completed.")
        
class FailureState(TaskState):
    def info(self, task:Task):
        print("Task is in Failure state due to an error.")

    def recover(self, task:Task):
        # Assuming we have a way to determine the appropriate state to recover to init
        task.state = InitiationState()
        print(f"Task recovered from Failure, transitioning back to {type(task.state).__name__}.")

print('```')
# Example Usage 1
network_task = Task()

# try invalid transition
# task.complete() 

network_task.info()
network_task.approve()
network_task.info()
network_task.execute()
network_task.info()
network_task.complete()
network_task.info()


# Example Usage 2
tasks = [Task() for i in range(10)]
for i,network_task in enumerate(tasks):
    print(f'{i}:')

    ii = 1
    print(f'try No.{ii}:')
    network_task.approve()
    network_task.execute()
    network_task.complete()

    while network_task.is_failure():
        network_task.recover()
        ii += 1
        print(f'try No.{ii}:')
        network_task.approve()
        network_task.execute()
        network_task.complete()
print('```')
```

    ```
    Task is in Initiation state. Awaiting approval.
    Task moved to Approval.
    Task is in Approval state. Awaiting execution.
    Task moved to Execution.
    Task is in Execution state. Awaiting completion.
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task is in Failure state due to an error.
    0:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    1:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    2:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task recovered from Failure, transitioning back to InitiationState.
    try No.2:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    3:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    4:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    5:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task recovered from Failure, transitioning back to InitiationState.
    try No.2:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    6:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    7:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    8:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    9:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    ```
    

This example involves very simple sequential tasks, meaning its states and transitions are minimal. However, in many cases, our system has many more states and transitions, making it difficult to do **Resumability** in a single function. As the following example shows, we will need a solver.


```python
from collections import deque

# Define the state transitions with the additional states
_states = [
    'init','connected','close','loss','waiting','failure','talk'
    ]
transitions = {
    'init': ['waiting'],
    'connected': ['loss', 'talk', 'close'],
    'close': ['init'],
    'loss': ['init'],
    'waiting': ['connected', 'failure'],
    'failure': ['init'],
    'talk': ['close']
}

# Function to find the path from start_state to end_state
def find_path(transitions:dict, start_state, end_state):
    # Use a queue to store the paths
    queue = deque([[start_state]])
    
    # Use a set to store the visited states
    visited = set()
    
    # Loop until the queue is empty
    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        # Get the last state from the path
        state = path[-1]
        
        # If the state is the end_state, return the path
        if state == end_state:
            return path
        
        # If the state has not been visited
        if state not in visited:
            # Mark the state as visited
            visited.add(state)
            
            # Get the next states from the transitions
            next_states = transitions.get(state, [])
            # Loop through the next states
            for next_state in next_states:
                # Create a new path with the next state
                new_path = list(path)
                new_path.append(next_state)
                # Add the new path to the queue
                queue.append(new_path)
    
    # Return None if no path is found
    return None

# Define the start and end states
start_state = 'loss'
end_state = 'talk'

# Find the path
path = find_path(transitions, start_state, end_state)

# Print the path
print('```')
if path:
    print("Path from", start_state, "to", end_state, ":", " -> ".join(path))
else:
    print("No path found from", start_state, "to", end_state)
print('```')
```

    ```
    Path from loss to talk : loss -> init -> waiting -> connected -> talk
    ```
    

- **Example 2: Network Connection Resumable System:** In a network connection resumable system, managing various states such as `init`, `connected`, `loss`, `close`, `waiting`, `failure`, and `talk` is crucial for maintaining a stable and resilient connection. An FSM can be used to handle these state transitions and ensure that the system can recover from disruptions seamlessly.

    - **Scenario**: Consider the previous state transition. Each state has defined transitions to other states, creating a robust mechanism for handling changes in the network connection status. For instance, if the system is in the `loss` state, it needs to transition to `talk` to resume communication.
    
    - **Implementation**:
        - **States**: Initiation, ConnectionEstablished, Closure, ConnectionLost, Waiting, Failure, Communication
        - **Transitions**: 
            ```python
                transitions = {
                    'Initiation':            ['Waiting'],
                    'ConnectionEstablished': ['ConnectionLost', 'Communication', 'Closure'],
                    'Closure':               ['Initiation'],
                    'ConnectionLost':        ['Initiation'],
                    'Waiting':               ['ConnectionEstablished', 'Failure'],
                    'Failure':               ['Initiation'],
                    'Communication':         ['ConnectionLost', 'Closure']
                }
            ```

    - **Resumability**: The state of each task is saved persistently in a database. If the system stops or is interrupted, it can resume by reloading and solving from the current state to the target state, continuing from the last recorded state. This ensures that no steps are skipped or repeated.

Here is a Python implementation to find the path from "ConnectionLost" to "Communication," demonstrating how FSMs can manage **Resumability** effectively:



```python
import json
import time
import random

class NetworkTask:
    def __init__(self): self.state = InitiationState()
    def transition_to(self, state): self.state = state
    def initiation(self): self.state.initiation(self)
    def connectionEstablished(self): self.state.connectionEstablished(self)
    def closure(self): self.state.closure(self)
    def connectionLost(self): self.state.connectionLost(self)
    def failure(self): self.state.failure(self)    
    def communication(self): 
        self.state.communication(self)
        self.state.simulate_communication(self)

    def waiting(self): 
        self.state.waiting(self)
        return self.state.simulate_waiting(self)
    def current_state(self): return self.state.current_state(self)

class NetworkState:
    def _defult_error(self,to=''): raise NotImplementedError(f"Invalid transition from [{self.__class__.__name__}] -> [{to}]")
    def initiation(self, task: NetworkTask): self._defult_error("Initiation")
    def connectionEstablished(self, task: NetworkTask): self._defult_error("Connection Established")
    def closure(self, task: NetworkTask): self._defult_error("Closure")
    def connectionLost(self, task: NetworkTask): self._defult_error("Connection Lost")
    def waiting(self, task: NetworkTask): self._defult_error("Waiting")
    def failure(self, task: NetworkTask): self._defult_error("Failure")
    def communication(self, task: NetworkTask): self._defult_error("Communication")


    def simulate_communication(self, task: NetworkTask): raise NotImplementedError(f"simulate_communication NotImplemented")
    def simulate_waiting(self, task: NetworkTask): raise NotImplementedError(f"simulate_waiting NotImplemented")
    def current_state(self, task: NetworkTask):    return self.__class__


class InitiationState(NetworkState):
    @staticmethod
    def _transitions(): return [WaitingState]
    def waiting(self, task: NetworkTask):                task.transition_to(WaitingState())

class ConnectionEstablishedState(NetworkState):
    @staticmethod
    def _transitions(): return [ConnectionLostState,CommunicationState,ClosureState]    
    def connectionLost(self, task: NetworkTask):         task.transition_to(ConnectionLostState())
    def communication(self, task: NetworkTask):          task.transition_to(CommunicationState())
    def closure(self, task: NetworkTask):                task.transition_to(ClosureState())

class ClosureState(NetworkState):
    @staticmethod
    def _transitions(): return [InitiationState]
    def initiation(self, task: NetworkTask):             task.transition_to(InitiationState())

class ConnectionLostState(NetworkState):
    @staticmethod
    def _transitions(): return [InitiationState]
    def initiation(self, task: NetworkTask):             task.transition_to(InitiationState())

class WaitingState(NetworkState):    
    def simulate_waiting(self, task: NetworkTask):
        time.sleep(1)
        if random.random() > 0.5:
            self.connectionEstablished(task)
            return True
        else:
            self.failure(task)
            return False
     
    @staticmethod
    def _transitions(): return [ConnectionEstablishedState,FailureState]
    def connectionEstablished(self, task: NetworkTask):  task.transition_to(ConnectionEstablishedState())
    def failure(self, task: NetworkTask):                task.transition_to(FailureState())

class FailureState(NetworkState):
    @staticmethod
    def _transitions(): return [InitiationState]
    def initiation(self, task: NetworkTask):             task.transition_to(InitiationState())

class CommunicationState(NetworkState):
    def simulate_communication(self, task: NetworkTask):
        time.sleep(1)
        if random.random() > 0.5:
            self.connectionLost(task)
            return True
        return False
        
    @staticmethod
    def _transitions(): return [ClosureState, ConnectionLostState]
    def closure(self, task: NetworkTask):                task.transition_to(ClosureState())
    def connectionLost(self, task: NetworkTask):         task.transition_to(ConnectionLostState())
```


```python
# Example usage
network_task = NetworkTask()
print(f'State: {network_task.current_state()}')  # State: Initiation

network_task.waiting()  # Transition to Waiting 
print(f'State: {network_task.current_state()}')  # State: Connection Established or False!!

network_task.communication()  # Transition to Connection
print(f'State: {network_task.current_state()}')  # State: Communication or Connection Lost !!

network_task.closure()  # Transition to Initiation
print(f'State: {network_task.current_state()}')  # State: Initiation
```

```python
State: <class '__main__.InitiationState'>
State: <class '__main__.FailureState'>



---------------------------------------------------------------------------

NotImplementedError                       Traceback (most recent call last)

Cell In[101], line 9
      6 task.waiting()  # Transition to Waiting 
      7 print(f'State: {task.current_state()}')  # State: Connection Established or False!!
----> 9 task.communication()  # Transition to Connection
     10 print(f'State: {task.current_state()}')  # State: Communication or Connection Lost !!
     12 task.closure()  # Transition to Initiation


Cell In[100], line 14, in NetworkTask.communication(self)
     13 def communication(self): 
---> 14     self.state.communication(self)
     15     self.state.simulate_communication(self)


Cell In[100], line 30, in NetworkState.communication(self, task)
---> 30 def communication(self, task: NetworkTask): self._defult_error("Communication")


Cell In[100], line 23, in NetworkState._defult_error(self, to)
     22 class NetworkState:
---> 23     def _defult_error(self,to=''): raise NotImplementedError(f"Invalid transition from [{self.__class__.__name__}] -> [{to}]")
     24     def initiation(self, task: NetworkTask): self._defult_error("Initiation")
     25     def connectionEstablished(self, task: NetworkTask): self._defult_error("Connection Established")


NotImplementedError: Invalid transition from [FailureState] -> [Communication]
```


```python
# Extract transitions
transitions = {
    InitiationState:InitiationState._transitions(),
    ConnectionEstablishedState:ConnectionEstablishedState._transitions(),
    ClosureState:ClosureState._transitions(),
    ConnectionLostState:ConnectionLostState._transitions(),
    WaitingState:WaitingState._transitions(),
    FailureState:FailureState._transitions(),
    CommunicationState:CommunicationState._transitions(),
}
class_str_map = {cls.__name__:cls for cls,trans in transitions.items()}
class_str_map.update({cls:cls.__name__ for cls,trans in transitions.items()})
class_methodstr_map = {cls.__name__:cls.__name__.replace('State','').lower() for cls,trans in transitions.items()}

transitions_str = {class_str_map[cls]:[class_str_map[t] for t in trans] for cls,trans in transitions.items()}
print('```json')
print(json.dumps(transitions_str,indent=2))
print('```')
```

    ```json
    {
      "InitiationState": [
        "WaitingState"
      ],
      "ConnectionEstablishedState": [
        "ConnectionLostState",
        "CommunicationState",
        "ClosureState"
      ],
      "ClosureState": [
        "InitiationState"
      ],
      "ConnectionLostState": [
        "InitiationState"
      ],
      "WaitingState": [
        "ConnectionEstablishedState",
        "FailureState"
      ],
      "FailureState": [
        "InitiationState"
      ],
      "CommunicationState": [
        "ClosureState",
        "ConnectionLostState"
      ]
    }
    ```
    


```python
from collections import deque

def find_path(transitions:dict, start_state, end_state):
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

start_state = FailureState
end_state   = CommunicationState
path        = find_path(transitions, start_state, end_state)
print('```')
print(f"Path from {class_str_map[start_state]} to {class_str_map[end_state]} : "+' -> '.join([class_str_map[p] for p in path]))
print('```')
```

    ```
    Path from FailureState to CommunicationState : FailureState -> InitiationState -> WaitingState -> ConnectionEstablishedState -> CommunicationState
    ```
    


```python
print('```')
# Example usage
network_task = NetworkTask()
target_state = CommunicationState

print(f'Set target state: {target_state}')

def next_action(task:NetworkTask,target_state):
    path = find_path(transitions, task.current_state(), target_state)
    if len(path)<=1: return None
    return path[1]
    
#In practice, it is better to set a maximum number for attempts.
while network_task.current_state() != target_state:
    cls = next_action(network_task,target_state)
    if cls is None:raise ValueError('no next acion! unreachable!')

    cls_str = class_str_map[cls]
    method_str = class_methodstr_map[cls_str]
    print(f'Current: {class_str_map[network_task.current_state()]}, try {method_str}')
    getattr(network_task,method_str)()
    
print(f'Success to target state: {network_task.current_state()}')
print('```')
```

    ```
    Set target state: <class '__main__.CommunicationState'>
    Current: InitiationState, try waiting
    Current: FailureState, try initiation
    Current: InitiationState, try waiting
    Current: FailureState, try initiation
    Current: InitiationState, try waiting
    Current: FailureState, try initiation
    Current: InitiationState, try waiting
    Current: ConnectionEstablishedState, try communication
    Current: ConnectionLostState, try initiation
    Current: InitiationState, try waiting
    Current: FailureState, try initiation
    Current: InitiationState, try waiting
    Current: FailureState, try initiation
    Current: InitiationState, try waiting
    Current: FailureState, try initiation
    Current: InitiationState, try waiting
    Current: ConnectionEstablishedState, try communication
    Current: ConnectionLostState, try initiation
    Current: InitiationState, try waiting
    Current: FailureState, try initiation
    Current: InitiationState, try waiting
    Current: FailureState, try initiation
    Current: InitiationState, try waiting
    Current: ConnectionEstablishedState, try communication
    Current: ConnectionLostState, try initiation
    Current: InitiationState, try waiting
    Current: FailureState, try initiation
    Current: InitiationState, try waiting
    Current: ConnectionEstablishedState, try communication
    Current: ConnectionLostState, try initiation
    Current: InitiationState, try waiting
    Current: FailureState, try initiation
    Current: InitiationState, try waiting
    Current: ConnectionEstablishedState, try communication
    Current: ConnectionLostState, try initiation
    Current: InitiationState, try waiting
    Current: FailureState, try initiation
    Current: InitiationState, try waiting
    Current: FailureState, try initiation
    Current: InitiationState, try waiting
    Current: ConnectionEstablishedState, try communication
    Success to target state: <class '__main__.CommunicationState'>
    ```
    

This code defines the state transitions and uses a breadth-first search algorithm to find the shortest path from any state to the target `CommunicationState` state. By implementing such FSMs, network systems can automatically recover from disruptions, ensuring continuous and reliable communication.

In summary, FSMs are invaluable for managing state transitions in resumable systems. They provide a clear and structured approach to handling various states and transitions, ensuring that systems can pause and resume operations without losing context or consistency. This example demonstrates how FSMs can be applied to a network connection recovery system, highlighting their practical utility and importance.

- **Future Outlook**: Look at evolving uses of state machines in software development.

### Conclusion

- **Summary**: Finite State Machines (FSMs) are a powerful and versatile tool for managing state transitions in both simple and complex systems. By defining clear states, transitions, and actions, FSMs offer a systematic approach to handling various conditions and events within a system. This design pattern is particularly beneficial for resumable systems, where the ability to pause and resume operations without losing context or consistency is crucial.

- **Future Outlook**: 
    - **Encapsulation of State Behavior**: Each state class encapsulates specific behaviors and transitions, making the system easier to understand and modify.
    - **Ease of Modification**: Changes to state behavior or transitions can be made within individual state classes, simplifying maintenance.
    - **Error Handling**: FSMs prevent invalid transitions through built-in error handling mechanisms, enhancing the robustness of the system.

By implementing FSMs, developers can create more robust, error-resistant, and maintainable systems. Whether managing user interfaces, network protocols, or workflow processes, FSMs provide a clear and structured approach to state management. As demonstrated, FSMs not only improve system reliability and performance but also ensure that resumable systems can handle interruptions gracefully, **resuming** operations seamlessly from the last recorded state.

### Additional Notes
- **Advanced State Machine Patterns**:
   - While this chapter covers the basics, there are advanced patterns such as hierarchical state machines (HSM) and statecharts that can further enhance the capabilities of FSMs. These patterns allow for more complex state hierarchies and transitions, useful in large-scale systems.

- **State Machine Libraries**:
   - Various programming languages offer robust libraries and frameworks to implement state machines efficiently. For example, `transitions` in Python, `StateMachine` in JavaScript, and `Boost.Statechart` in C++. Leveraging these libraries can save time and reduce errors.

- **Documentation and Visualization**:
   - Documenting the state machine design with diagrams (e.g., state diagrams or flowcharts) helps in understanding and maintaining the system. Visualization tools can generate these diagrams automatically from the state machine code.

- **Concurrency and State Machines**:
   - In multi-threaded or distributed systems, managing concurrency with state machines can be challenging. Techniques such as locking mechanisms, state machine replicas, or distributed state management should be considered.

- **Event-Driven Architectures**:
   - State machines are a natural fit for event-driven architectures. They can be integrated with event queues, message brokers, or reactive programming frameworks to handle asynchronous events efficiently.

- **Integration with Other Design Patterns**:
   - State machines often work well in combination with other design patterns like Singleton (for a single instance of the state machine), Observer (for notifying state changes), and Strategy (for state-specific behavior).

Let's try `transitions` in Python as following example:


```python
from dataclasses import dataclass
from transitions import Machine
import random
import time


class NetworkTask:
    @dataclass
    class States:
        Initiation='Initiation'
        ConnectionEstablished='ConnectionEstablished'
        Closure='Closure'
        ConnectionLost='ConnectionLost'
        Waiting='Waiting'
        Failure='Failure'
        Communication='Communication'
    _transitions = {
        States.Initiation:            [States.Waiting],
        States.ConnectionEstablished: [States.ConnectionLost,States.Communication,States.Closure],
        States.Closure:               [States.Initiation],
        States.ConnectionLost:        [States.Initiation],
        States.Waiting:               [States.ConnectionEstablished,States.Failure],
        States.Failure:               [States.Initiation],
        States.Communication:         [States.Closure,States.ConnectionLost,States.Communication]
    }
    _states = list(_transitions.keys())

    def __init__(self):
        self.machine = Machine(model=self, states=NetworkTask._states, initial=NetworkTask.States.Initiation)
        for source,v in self._transitions.items():
            for dest in v:
                self.machine.add_transition(source=source,dest=dest,trigger=f'to_{dest}')

        self.to_Waiting()

    def to_Waiting(self):
        self.simulate_waiting()

    def to_Communication(self):
        self.simulate_communication()
        
    def simulate_waiting(self):
        time.sleep(1)
        if random.random() <= 0.5:
            # function of to_ConnectionEstablished is auto set by lib
            self.to_ConnectionEstablished()
        else:
            # function of to_Failure is auto set by lib
            self.to_Failure()
    
    def simulate_communication(self):
        self.state = NetworkTask.States.Waiting
        time.sleep(1)
        if random.random() <= 0.3:
            self.state = NetworkTask.States.Communication
        elif random.random() <= 0.6:
            # function of to_ConnectionLost is auto set by lib
            self.to_ConnectionLost()
        else:
            
            self.to_Failure()

    def get_transitions(self):
        return self._transitions

print('```')
# Example usage
network_task = NetworkTask()
if network_task.state == 'ConnectionEstablished':
    network_task.simulate_communication()
print(network_task.state)


print();print()
# Example find_path
from collections import deque
def find_path(transitions:dict, start_state, end_state):
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

start_state = NetworkTask.States.Failure
end_state   = NetworkTask.States.Communication
path        = find_path(network_task.get_transitions(), start_state, end_state)
print(f"Path from {start_state} to {end_state} : "+' -> '.join([p for p in path]))


print();print()
# Example resumability
network_task = NetworkTask()
target_state = NetworkTask.States.Communication
print(f'Set target state: {target_state} ( current is {network_task.state})')
def next_action(task:NetworkTask,target_state):
    path = find_path(network_task.get_transitions(), task.state, target_state)
    if len(path)<=1: return None
    return path[1]
    
#In practice, it is better to set a maximum number for attempts.
while network_task.state != target_state:
    cls = next_action(network_task,target_state)
    if cls is None:raise ValueError('no next acion! unreachable!')
    
    print(f'Current: {network_task.state}, try to_{cls}')
    getattr(network_task,f'to_{cls}')()

print(f'Success to target state: {network_task.state}')

print('```')
```

    ```
    ConnectionLost
    
    
    Path from Failure to Communication : Failure -> Initiation -> Waiting -> ConnectionEstablished -> Communication
    
    
    Set target state: Communication ( current is Failure)
    Current: Failure, try to_Initiation
    Current: Initiation, try to_Waiting
    Current: Failure, try to_Initiation
    Current: Initiation, try to_Waiting
    Current: Failure, try to_Initiation
    Current: Initiation, try to_Waiting
    Current: Failure, try to_Initiation
    Current: Initiation, try to_Waiting
    Current: ConnectionEstablished, try to_Communication
    Current: Failure, try to_Initiation
    Current: Initiation, try to_Waiting
    Current: Failure, try to_Initiation
    Current: Initiation, try to_Waiting
    Current: ConnectionEstablished, try to_Communication
    Current: ConnectionLost, try to_Initiation
    Current: Initiation, try to_Waiting
    Current: ConnectionEstablished, try to_Communication
    Success to target state: Communication
    ```
    

---

## Chapter 6: Design Patterns for Resumability
- (Existing content)

## Chapter 7: Testing Resumable Systems
- (Existing content)

## Chapter 8: Resumability in Distributed Systems
- (Existing content)

## Chapter 9: Practical Applications and Case Studies
- (Existing content)

## Chapter 10: Architectural Considerations for Resumability
- (Newly added chapter)

## Chapter 11: State Management Techniques
- (Newly added chapter)

## Chapter 13: The Role of AI in Enhancing Resumability
- (Newly added chapter)

## Chapter 12: Global Trends and Future Directions
- (Newly added chapter)

---
## Conclusion (of this Book)

### Recap of Key Points
- Summarize the core principles, patterns, and technologies discussed.

### Encouragement to Experiment
- Motivate readers to apply learned concepts to their projects, emphasizing experimentation and learning.

### Looking Forward
- Discuss potential future developments in resumable programming and its expanding role in software development.

### Final Thoughts
- Reflect on the journey of reading the book and the transformative potential of adopting resumable programming practices.

## Closing
- Thank readers and invite them to engage further through online communities and forums.

---
## Fast References

### Quick Tips
- Provide bullet points of handy tips and best practices for quick reference.

### Glossary
- Define technical terms and jargon used throughout the book.

### Further Reading
- Recommend books, articles, and papers that expand on topics covered.

### Online Resources
- List websites, forums, and online courses for continued learning.

### Tools and Utilities
- Detail software tools and utilities that support the development of resumable programs.

### FAQs
- Address common questions and misconceptions about resumable programming.


