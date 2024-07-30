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
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    Moved forward 10 distance. New position: [10.0, 0.0]
    (0, [10.0, 0.0])
    Turned right 90 degrees. New orientation: 270
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
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    (0, [-4.999999999999999, 10.0])
    

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
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
    Turned left 90 degrees. New orientation: 90
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    !!!!!!!!!This machine crashed, auto reset!!!!!!!!!
    Machine has been reset to the 0,(0,0) state.
    turn_left 90
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
    (0, [-4.999999999999999, 10.0])
    

- **Second Way: Recording Actions and Arguments as State**: In this method, we record each action and its parameters. Upon a crash, the machine is reinitialized, and all recorded actions are replayed to restore the last known good state before attempting to continue from the point of failure.

  - Strengths:
    - **Action Replay**: This method records actions and their parameters, allowing the system to reconstruct the state by replaying these actions. This can be more storage-efficient, especially if the actions are compact.
    - **Audit Trail**: Storing a list of actions provides an audit trail of what the machine did, which can be useful for debugging, auditing, and understanding the sequence of operations leading to a crash.
    - **Adaptive Recovery**: By replaying actions from the beginning, this method can potentially adapt to changes in the system's logic or configuration since the state is dynamically reconstructed.

  - Weaknesses:
    - **Replay Overhead**: The major downside is the need to replay all actions from the start or from a checkpoint in the event of a crash. This can be time-consuming and inefficient, especially if the list of actions is long.
    - **Complexity in Handling Stateful Actions**: If actions are not purely functional or if they depend on external state not captured solely by the action parameters, replaying actions might not accurately reconstruct the state.
    - **Potential for Infinite Loops**: Without proper checks, there's a risk of entering an infinite loop of crashes and recoveries if a particular action consistently leads to a crash.

#### Which to Choose?
- **Choose Method 1** if the machine's state is relatively small, quick to serialize/deserialize, or if precise recovery to the last known good state is critical. This method is suitable for systems where actions are expensive or have significant side effects that need to be precisely managed.
- **Choose Method 2** if actions are relatively simple, the state is large or complex, or if you benefit from having an audit trail of actions. This method is preferable when actions are cheap to replay, or when the system's design allows for efficient state reconstruction.

#### Additional Notes:
- **Databases**: As the examples above show, we indeed need persistent storage (or a database) to save our states for resumability and to manage our states. We can use both SQL (such as PostgreSQL's support for transactional states) and NoSQL technologies (such as MongoDB's document-based storage, which can be effectively used for maintaining state), which we will discuss in the next chapter.
- **Message Queues**: Message queues can be used to send commands, events, etc., which will be useful for controlling resumable machine clusters over the internet. Tools like RabbitMQ or Kafka can manage tasks in a resumable fashion by decoupling task submission from execution.
- **Cloud Services**: Review cloud-based solutions that provide built-in support for resumability, such as AWS Step Functions, which allows the definition of workflows as state machines, or Azure Durable Functions, a solution designed to write stateful functions in a serverless computing environment.


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
    database = "example.db"
    conn = create_connection(database)
    
    if conn is None:
        raise Exception("Failed to connect to the database.")
    
    execute_transaction(conn)
    conn.close()
```

    Transaction started.
    Data inserted.
    Savepoint created.
    More data inserted.
    Rolled back to savepoint.
    Additional data inserted after rollback.
    Transaction committed.
    

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
            False
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
    main()
```

    Database setup complete.
    Machine state saved: Orientation 0, Position [0, 0]
    Turned left 90 degrees. New orientation: 90
    Machine state saved: Orientation 90, Position [0, 0]
    Moved forward 10 distance. New position: [6.123233995736766e-16, 10.0]
    Machine state saved: Orientation 90, Position [6.123233995736766e-16, 10.0]
    (90, [6.123233995736766e-16, 10.0])
    Turned right 90 degrees. New orientation: 0
    Machine state saved: Orientation 0, Position [6.123233995736766e-16, 10.0]
    Reversed 5 distance. New position: [-4.999999999999999, 10.0]
    Machine state saved: Orientation 0, Position [-4.999999999999999, 10.0]
    (0, [-4.999999999999999, 10.0])
    

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

  - Additional Notes:
    - **Complexity**: Managing state with transactions adds a layer of complexity to system design (especially table design). Developers must carefully handle transaction scopes, ensure proper rollback on failures, and maintain database performance under high-throughput conditions. Thorough testing is required to ensure the system behaves as expected under various failure scenarios.
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

### Section 2: Key-Value Databases
- Explore how key-value stores can facilitate quick state retrieval and updates essential for resumability.

### Conclusion
- **Summary**: Evaluate the pros and cons of each database type for resumable applications.
- **Future Outlook**: Consider future database technologies and trends.

### Additional Notes:
- ...

---
## Chapter 4: Design Pattern of Model-View-Controller (MVC)
### Introduction
- **Overview**: Explain the MVC design pattern and its relevance to building resumable web applications.
- **Objective**: Demonstrate how MVC facilitates separation of concerns, essential for modular resumable code.

### Section 1: Components of MVC
- Detailed exploration of the Model, View, and Controller components.

### Section 2: MVC in Practice
- Case studies and examples of MVC applied in web development.

### Conclusion
- **Summary**: Discuss the strengths and limitations of MVC in the context of resumability.
- **Future Outlook**: Future enhancements and alternatives to MVC.

### Additional Notes:
- ...

---
## Chapter 5: Design Pattern of State Machine
### Introduction
- **Overview**: Discuss the state machine design pattern and its importance in managing state in resumable systems.
- **Objective**: Teach how to design and implement state machines in software development.

### Section 1: Understanding State Machines
- Basics of state machines, including states, transitions, and actions.

### Section 2: Implementing State Machines
- Practical examples showing how state machines are used to handle complex state management in a resumable manner.

### Conclusion
- **Summary**: Highlight how state machines can simplify resumability challenges.
- **Future Outlook**: Look at evolving uses of state machines in software development.

### Additional Notes:
- ...

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


