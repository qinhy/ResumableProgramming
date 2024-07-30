### Book Title: "Resumable Programming"

### Preface

#### Introduction
- Discuss the evolution of programming practices with a focus on the need for resiliency and adaptability in modern software development.

#### History of Resumable Programming
- Trace the origins from early computing systems to contemporary frameworks that support asynchrony and fault tolerance.

#### Purpose of the Book
- Outline the book’s goals: educating developers on building more robust applications, and providing a toolkit for implementing resumable features in software projects.

---
### Chapter 0: Basic Python
#### Introduction
- **Overview**: Introduce Python as a programming language, focusing on features that facilitate resumable programming.
- **Objective**: Equip readers with basic Python skills necessary to implement examples provided in the book.

#### Section 1: Python Basics
- Cover Python syntax, control structures, functions, and modules.

#### Section 2: Advanced Python Features
- Introduce more complex Python features such as decorators, generators, and context managers, which are crucial for writing resumable code.

#### Conclusion
- **Summary**: Recap the Python basics and their relevance to resumable programming.
- **Future Outlook**: Discuss how these fundamentals will be used in subsequent chapters.

---
### Chapter 1: Understanding Resumability

#### Introduction
- **Overview**: Define resumable programming as the ability of a process to pause at certain points and then continue from those points later, either after a failure or after a deliberate halt. This capability is crucial for developing robust and scalable applications in environments where interruptions are common or where tasks are long-running.
- **Objective**: Equip readers with a foundational understanding of concepts and applications. By the end of this chapter, readers should appreciate the critical role that resumability plays in modern software development, particularly in distributed systems, cloud applications, and complex data processing workflows.

#### Section 0: Why We Need Resumability
In today’s technological landscape, applications are increasingly expected to operate continuously and handle a variety of interruptions—be they from system failures, planned downtime, or user-driven pauses. Resumable programming addresses these needs by ensuring that applications can maintain their functionality and data integrity under such circumstances. 

let's think a simple example without resumability.


```python
def fibonacci(n):
    if n <= 1 : return n
    return fibonacci(n-1)+fibonacci(n-2)

# Example 
for i in range(37):
    print(f"Fibonacci of {i} result:", fibonacci(i))
```

    Fibonacci of 0 result: 0
    Fibonacci of 1 result: 1
    Fibonacci of 2 result: 1
    Fibonacci of 3 result: 2
    Fibonacci of 4 result: 3
    Fibonacci of 5 result: 5
    Fibonacci of 6 result: 8
    Fibonacci of 7 result: 13
    Fibonacci of 8 result: 21
    Fibonacci of 9 result: 34
    Fibonacci of 10 result: 55
    Fibonacci of 11 result: 89
    Fibonacci of 12 result: 144
    Fibonacci of 13 result: 233
    Fibonacci of 14 result: 377
    Fibonacci of 15 result: 610
    Fibonacci of 16 result: 987
    Fibonacci of 17 result: 1597
    Fibonacci of 18 result: 2584
    Fibonacci of 19 result: 4181
    Fibonacci of 20 result: 6765
    Fibonacci of 21 result: 10946
    Fibonacci of 22 result: 17711
    Fibonacci of 23 result: 28657
    Fibonacci of 24 result: 46368
    Fibonacci of 25 result: 75025
    Fibonacci of 26 result: 121393
    Fibonacci of 27 result: 196418
    Fibonacci of 28 result: 317811
    Fibonacci of 29 result: 514229
    Fibonacci of 30 result: 832040
    Fibonacci of 31 result: 1346269
    Fibonacci of 32 result: 2178309
    Fibonacci of 33 result: 3524578
    Fibonacci of 34 result: 5702887
    Fibonacci of 35 result: 9227465
    Fibonacci of 36 result: 14930352
    


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
for i in range(37):
    print(f"Fibonacci of {i} result:", fibonacci(i))
```

    Fibonacci of 0 result: 0
    Fibonacci of 1 result: 1
    Fibonacci of 2 result: 1
    Fibonacci of 3 result: 2
    Fibonacci of 4 result: 3
    Fibonacci of 5 result: 5
    Fibonacci of 6 result: 8
    Fibonacci of 7 result: 13
    Fibonacci of 8 result: 21
    Fibonacci of 9 result: 34
    Fibonacci of 10 result: 55
    Fibonacci of 11 result: 89
    Fibonacci of 12 result: 144
    Fibonacci of 13 result: 233
    Fibonacci of 14 result: 377
    Fibonacci of 15 result: 610
    Fibonacci of 16 result: 987
    Fibonacci of 17 result: 1597
    Fibonacci of 18 result: 2584
    Fibonacci of 19 result: 4181
    Fibonacci of 20 result: 6765
    Fibonacci of 21 result: 10946
    Fibonacci of 22 result: 17711
    Fibonacci of 23 result: 28657
    Fibonacci of 24 result: 46368
    Fibonacci of 25 result: 75025
    Fibonacci of 26 result: 121393
    Fibonacci of 27 result: 196418
    Fibonacci of 28 result: 317811
    Fibonacci of 29 result: 514229
    Fibonacci of 30 result: 832040
    Fibonacci of 31 result: 1346269
    Fibonacci of 32 result: 2178309
    Fibonacci of 33 result: 3524578
    Fibonacci of 34 result: 5702887
    Fibonacci of 35 result: 9227465
    Fibonacci of 36 result: 14930352
    


##### Key Features of This Resumable Implementation:
- **Persistence**: The use of a `shelve` database (we will discuss more databases later), which is a simple persistent storage for Fibonacci integers, allows the function to get/set results. If the process is interrupted, the previously computed values of the sequence are saved (this is also very beneficial when the app crashes unexpectedly).
- **Performance**: By saving previously computed values, we avoid redundant calculations, thus minimizing re-computation. This drastically improves performance, especially for large `n`.

This approach illustrates a basic method to make the Fibonacci function resumable by using external storage for state. This can be extended to more complex algorithms and applications where resumability is crucial.

#### Section 1: Core Concepts
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
```

    Turned left 90 degrees. New orientation: 90
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    (90, [6.123233995736766e-16, 10.0])
    Turned right 90 degrees. New orientation: 0
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    (0, [-4.999999999999999, 10.0])
    

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
            False
        else:
            return True

    def reset(self):
        # Reset the machine to the initial state
        self.orientation = 0
        self.position = [0, 0]
        print("Machine has been reset to the 0,(0,0) state.")

# Example of using MachineA
machine = MachineA()
machine.turn_left(90)
machine.move_forward(10)
print(machine.get_machine_state())
machine.turn_right(90)
machine.move_backward(5)
print(machine.get_machine_state())
```

    Turned left 90 degrees. New orientation: 90
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    (90, [6.123233995736766e-16, 10.0])
    Turned right 90 degrees. New orientation: 0
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Reversed 5 distance. New position: [-5.0, 0.0]
    (0, [-5.0, 0.0])
    

The machine in the code shows unstable movements, making it very hard to reach the goal axis of (-5, 10). In production systems, obviously, users will hate losing their previous work and ending up in an unexpected state, which is not the goal.

let us make a simple "Resumable Implementation" as following:


```python
"The first way is to record the orientation and position of the machine state after performing each action( or process)."

import shelve  # Used for simple key-value pair storage
with shelve.open('machine_cache.db') as db:
    
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
    
# The second way is to record the action name and its arguments as a "state" after performing each action. 
```

    Turned left 90 degrees. New orientation: 90
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    (90, [6.123233995736766e-16, 10.0])
    Turned right 90 degrees. New orientation: 0
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Turned right 90 degrees. New orientation: 0
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Turned right 90 degrees. New orientation: 0
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    (0, [-4.999999999999999, 10.0])
    


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
    
# The second way is to record the action name and its arguments as a "state" after performing each action. 
```

    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Turned left 90 degrees. New orientation: 90
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    (90, [6.123233995736766e-16, 10.0])
    Turned right 90 degrees. New orientation: 0
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    turn_right 90
    Turned right 90 degrees. New orientation: 0
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    turn_right 90
    Turned right 90 degrees. New orientation: 0
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    turn_right 90
    Turned right 90 degrees. New orientation: 0
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    turn_right 90
    Turned right 90 degrees. New orientation: 0
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    turn_right 90
    Turned right 90 degrees. New orientation: 0
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    turn_right 90
    Turned right 90 degrees. New orientation: 0
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    turn_right 90
    Turned right 90 degrees. New orientation: 0
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    move_forward 10
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    turn_right 90
    Turned right 90 degrees. New orientation: 0
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    (0, [-4.999999999999999, 10.0])
    

- **Fist way**: ...

- **Second way**: ...

---

#### Section 2: Technologies Enabling Resumability
- **Message Queues**: Describe how message queues like RabbitMQ or Kafka can be used to manage tasks in a resumable fashion by decoupling task submission from execution.
- **Databases**: Discuss how databases are used to store state information, using examples from both SQL (like PostgreSQL's support for transactional states) and NoSQL technologies (like MongoDB's document-based storage which can be effectively used for maintaining state).
- **Cloud Services**: Review cloud-based solutions that provide built-in support for resumability, such as AWS Step Functions, which allows the definition of workflows as state machines, or Azure Durable Functions, a solution designed to write stateful functions in a serverless computing environment.

#### Conclusion
- **Summary**: Recap the chapter’s key points, emphasizing the importance of understanding and implementing resumable programming techniques to build fault-tolerant, scalable, and robust applications.
- **Future Outlook**: Speculate on the evolving trends in resumable programming, including the integration of AI to predict and manage system failures proactively, and the development of more sophisticated state management tools that enhance the resumability of applications.

#### Additional Notes:
- **Critical Takeaways**: Emphasize the importance of careful design in state management to avoid common pitfalls like state corruption or loss during failures.
- **Practical Tips**: Offer advice on testing resumability in applications, such as using chaos engineering principles to simulate failures and ensure that the application can resume as expected.
- **Common Pitfalls and Avoidance**: List common mistakes, such as inadequate testing of edge cases in state recovery or using non-idempotent operations without proper safeguards, and provide strategies for avoiding these issues.

This deep dive should set the stage for readers to understand not just the 'how' but the 'why' behind resumable programming, equipping them with the knowledge to implement these concepts in their own development projects effectively.

---
### Chapter 2: SQL vs Key-Value Databases
#### Introduction
- **Overview**: Compare SQL and key-value databases in the context of maintaining state for resumable systems.
- **Objective**: Understand which type of database is best suited for specific resumability requirements.

#### Section 1: SQL Databases
- Discuss traditional relational database models with examples in resumable scenarios.

#### Section 2: Key-Value Databases
- Explore how key-value stores can facilitate quick state retrieval and updates essential for resumability.

#### Conclusion
- **Summary**: Evaluate the pros and cons of each database type for resumable applications.
- **Future Outlook**: Consider future database technologies and trends.

#### Additional Notes:
- ...

---
### Chapter 3: Design Pattern of Model-View-Controller (MVC)
#### Introduction
- **Overview**: Explain the MVC design pattern and its relevance to building resumable web applications.
- **Objective**: Demonstrate how MVC facilitates separation of concerns, essential for modular resumable code.

#### Section 1: Components of MVC
- Detailed exploration of the Model, View, and Controller components.

#### Section 2: MVC in Practice
- Case studies and examples of MVC applied in web development.

#### Conclusion
- **Summary**: Discuss the strengths and limitations of MVC in the context of resumability.
- **Future Outlook**: Future enhancements and alternatives to MVC.

#### Additional Notes:
- ...

---
### Chapter 4: Design Pattern of State Machine
#### Introduction
- **Overview**: Discuss the state machine design pattern and its importance in managing state in resumable systems.
- **Objective**: Teach how to design and implement state machines in software development.

#### Section 1: Understanding State Machines
- Basics of state machines, including states, transitions, and actions.

#### Section 2: Implementing State Machines
- Practical examples showing how state machines are used to handle complex state management in a resumable manner.

#### Conclusion
- **Summary**: Highlight how state machines can simplify resumability challenges.
- **Future Outlook**: Look at evolving uses of state machines in software development.

#### Additional Notes:
- ...

---
### Chapter 5: Design Patterns for Resumability
- (Existing content)

### Chapter 6: Testing Resumable Systems
- (Existing content)

### Chapter 7: Resumability in Distributed Systems
- (Existing content)

### Chapter 8: Practical Applications and Case Studies
- (Existing content)

### Chapter 9: Architectural Considerations for Resumability
- (Newly added chapter)

### Chapter 10: State Management Techniques
- (Newly added chapter)

### Chapter 11: The Role of AI in Enhancing Resumability
- (Newly added chapter)

### Chapter 12: Global Trends and Future Directions
- (Newly added chapter)

---
### Conclusion (of this Book)

#### Recap of Key Points
- Summarize the core principles, patterns, and technologies discussed.

#### Encouragement to Experiment
- Motivate readers to apply learned concepts to their projects, emphasizing experimentation and learning.

#### Looking Forward
- Discuss potential future developments in resumable programming and its expanding role in software development.

#### Final Thoughts
- Reflect on the journey of reading the book and the transformative potential of adopting resumable programming practices.

### Closing
- Thank readers and invite them to engage further through online communities and forums.

---
### Fast References

#### Quick Tips
- Provide bullet points of handy tips and best practices for quick reference.

#### Glossary
- Define technical terms and jargon used throughout the book.

#### Further Reading
- Recommend books, articles, and papers that expand on topics covered.

#### Online Resources
- List websites, forums, and online courses for continued learning.

#### Tools and Utilities
- Detail software tools and utilities that support the development of resumable programs.

#### FAQs
- Address common questions and misconceptions about resumable programming.
