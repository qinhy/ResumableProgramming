# Resumable Programming
#### Authors : Huangyi Qin, ChatGPT

## Preface

### Introduction
Over the past few decades, software development has evolved at a breathtaking pace. Initially focused on creating straightforward applications with limited scope, programming practices have expanded to address the complexities of highly interconnected, ever-changing systems. Today’s digital landscape demands applications that are **resilient**, adaptable, and capable of gracefully handling unforeseen events. The move towards more distributed and asynchronous systems, the proliferation of microservices, and the increasing need for high availability have all intensified the demand for resilient programming paradigms. To meet these challenges, modern developers must adopt strategies and patterns that enable software to continue operating even when unexpected disruptions occur. This shift has given rise to practices that emphasize error handling, system recovery, and state persistence, collectively forming a crucial part of contemporary development methodologies.

### History of Resumable Programming
The concept of resumable programming can be traced back to the early days of computing when batch processing systems had to manage long-running tasks prone to interruptions. In those times, programmers devised basic checkpointing and **state-saving** techniques to **recover and resume** tasks following a system crash. As computing technology advanced, so too did approaches to fault tolerance and asynchrony. From the introduction of interrupts and state machines in hardware-based systems to the rise of sophisticated programming models like multithreading, coroutines, and distributed event-driven architectures, resumable programming has been an evolving journey. Today, numerous frameworks and languages provide built-in support for asynchrony, retries, and error recovery, demonstrating just how deeply integrated these principles have become in modern software engineering.

### Purpose of the Book
This book aims to provide software developers with the knowledge and practical tools to design and implement robust, resilient applications capable of handling unexpected failures and interruptions. Through real-world examples, detailed case studies, and step-by-step guidance, readers will learn how to leverage resumable programming principles to create software that not only recovers from disruptions but also thrives in highly dynamic environments. Whether you are a seasoned engineer or a newcomer eager to build fault-tolerant systems, this book serves as a comprehensive resource to equip you with the skills necessary to craft resilient software solutions tailored to the demands of modern computing.

---


## Chapter 1: Basic Python
### Introduction
- **Overview**
Python is a versatile and powerful programming language that has gained immense popularity among developers and data scientists alike. Known for its simplicity and readability, Python offers a wide range of features that cater to both beginners and seasoned programmers. One of Python's standout qualities is its flexibility: it allows you to write concise, readable code for small scripts while also providing robust capabilities for large-scale applications and complex software systems. In this chapter, we will explore the fundamental aspects of Python, laying a strong foundation for the more advanced topics covered later in this book.

- **Objective**
The objective of this chapter is to equip reader with the basic Python skills necessary to effectively understand and implement the examples and concepts provided in subsequent chapters. Whether reader is new to Python or need a refresher, this chapter will guide reader through the core components of the language, ensuring reader are well-prepared for the journey ahead.

This chapter is divided into two main sections: **Python Basics** and **Advanced Python Features**. The **Python Basics** section introduces essential Python syntax, control structures, functions, and modules, providing a solid groundwork for those just getting started. In the **Advanced Python Features** section, we delve into more sophisticated topics like decorators, generators, and context managers—powerful tools that will enhance readerr ability to write efficient and elegant Python code.

By the end of this chapter, reader will have a comprehensive understanding of Python's core and advanced features, preparing reader to tackle the programming challenges presented throughout this book.


### Section 1: Python Basics

Python's syntax is designed to be intuitive and easy to read. This section will cover the foundational aspects of Python programming, including basic syntax, control structures, functions, and modules. Each topic will be presented with code examples to reinforce understanding.



```python
'Python syntax is clean and easy to understand, emphasizing readability. '
'Python uses indentation to define code blocks instead of curly braces or keywords.'
print('```')
# This is a comment
print("Hello, World!")  # Output: Hello, World!

# Variables and types
name = "Alice"
age = 30
height = 5.7

# Printing variables
print(f"Name: {name}, Age: {age}, Height: {height}")

# Basic arithmetic
a = 10
b = 5
print(a + b)  # Output: 15
print(a - b)  # Output: 5
print(a * b)  # Output: 50
print(a / b)  # Output: 2.0
print('```')
```

    ```
    Hello, World!
    Name: Alice, Age: 30, Height: 5.7
    15
    5
    50
    2.0
    ```
    


```python
'Control structures in Python allow you to control the flow of program.' 
'Python supports common control structures like `if` statements, `for` loops, and `while` loops.'

print('```')
# Example of an if-else statement
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
    
# Example of a for loop
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# Example of a while loop
count = 0

while count < 5:
    # The indentations of each line must be the same
    print("Count is:", count)
    count += 1
print('```')
```

    ```
    x is positive
    1
    2
    3
    4
    5
    Count is: 0
    Count is: 1
    Count is: 2
    Count is: 3
    Count is: 4
    ```
    


```python
'Functions in Python are defined using the `def` keyword.'
'They are reusable blocks of code that perform a specific task.'
'Python functions can take arguments and return values.'

print('```')
# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))  # Output: Hello, Alice!

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print(result)  # Output: 15
print('```')
```

    ```
    Hello, Alice!
    15
    ```
    


```python
'Python modules are .py files that can be imported into other Python programs.'
'This allows you to organize your code into reusable components.'

# Importing the math module
import math

# Using functions from the math module
print(math.sqrt(16))  # Output: 4.0
print(math.pi)  # Output: 3.141592653589793


# Example: Creating and Importing a Custom Module**

######## Create a Python file named `my_module.py`
# my_module.py
def say_hello():
      print("Hello from my_module!")
######## end of the file my_module.py


######## Import and use `my_module` in another Python file (main.py):
# main.py
import my_module

my_module.say_hello()  # Output: Hello from my_module!
######## end of the file main.py

```

### Section 2: Advanced Python Features

These advanced Python features—generators, decorators, and context managers—are crucial for writing efficient and clean code. Understanding these concepts will not only help you write more Pythonic code but will also be essential for implementing the more advanced programming patterns discussed in the later chapters of this book.


- **Generators**:
Generators are a type of iterable, like lists or tuples. Unlike lists, however, generators do not store all their values in memory; they generate each value on the fly and are hence more memory-efficient for large data sets. Generators are defined using functions and the `yield` keyword.


```python
def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print('```')
# Using the generator
for number in fibonacci_sequence(10):
    print(number)
print('```')
```

    ```
    0
    1
    1
    2
    3
    5
    8
    13
    21
    34
    ```
    


- **Decorators**: Decorators are a powerful and expressive tool in Python that allow you to modify or enhance functions or methods without changing their actual code. Decorators are widely used in Python for logging, enforcing access control, instrumentation, caching, and more.



```python

def debug(func):
    """A simple decorator that prints the arguments and return value of a function."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug
def multiply(a, b):
    return a * b

print('```')
# Using the decorated function
multiply(5, 3)
print('```')
```

    ```
    Calling multiply with arguments (5, 3) and keyword arguments {}
    multiply returned 15
    ```
    


- **Context Managers**: Context managers are used for resource management in Python, such as managing files, network connections, and locks. The most common way to define a context manager is with the `with` statement, which ensures that resources are properly acquired and released. You can create your own context managers using the `contextlib` module or by defining a class with `__enter__` and `__exit__` methods.


```python
from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    'Context manager for opening and closing a file.'
    'Or for opening and closing original resource.'
    try:
        file = open(file_name, mode)
        yield file
    finally:
        file.close()

# Using the context manager
with open_file('example.txt', 'w') as f:
    f.write('Hello, world!')
```

### Section 3: Python Classes

Classes are one of the fundamental building blocks of object-oriented programming (OOP) in Python. They provide a way to bundle data and functionality together. Python classes allow you to define complex data types that behave like real-world objects and are an essential part of writing clean and maintainable code.


- **What is a Class?**: A clas is a blueprint for creating objects. It defines a set of attributes and methods that the created objects (also called instances) can use. Attributes represent the state of an object, while methods define its behavior. In Python, a class is defined using the `class` keyword, followed by the class name and a colon.


```python
class MyClass:
    # Attributes and methods go here
    pass

my_object = MyClass()
```


- **Defining Attributes and Methods** :
Attributes in a Python class are defined within the `__init__` method, which is the constructor method that is automatically called when a new instance is created. Methods are functions defined within the class body that operate on instances of the class.



```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")
print('```')
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()  # Output: Buddy says Woof!
print('```')
```

    ```
    Buddy says Woof!
    ```
    

- **Class vs. Instance Attributes** :
Class attributes are shared among all instances of a class, while instance attributes are unique to each instance. Class attributes are defined directly within the class body and are not inside any methods.


```python
# Here, `species` is a class attribute, and `name` is an instance attribute.
class Cat:
    species = "Felis catus"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

my_cat = Cat("Whiskers")

print('```')
print(my_cat.species)  # Output: Felis catus
print('```')
```

    ```
    Felis catus
    ```
    

- **Encapsulation and Data Hiding** :
Encapsulation is the concept of bundling data and methods that operate on the data within one unit, a class. Python uses a naming convention to make attributes and methods private (not intended to be accessed from outside the class). Prefixing an attribute name with an underscore (`_`) suggests that it is intended for internal use.



```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance
```

- **Inheritance** : 
Inheritance is a powerful feature of OOP that allows a class to inherit attributes and methods from another class. The class that is inherited from is called the **parent** or **base class**, and the class that inherits is called the **child** or **derived class**.

- **Polymorphism** :
Polymorphism allows methods to have different implementations depending on the object that calls them. In the example above, both `Dog` and `Cat` implement the `speak()` method differently. Polymorphism enables the same interface to be used for different underlying forms (data types).


```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print('```')
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
print('```')
```

    ```
    Buddy says Woof!
    Whiskers says Meow!
    ```
    

-  **Using `super()`** :
The `super()` function allows you to call methods from a parent class from within a child class. This is especially useful in constructors when you want to initialize the base class.



```python
class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name)
        self.can_fly = can_fly
```

- **Special Methods and Operator Overloading** :
Python classes have special methods, also known as "dunder" methods (double underscore methods), like `__init__`, `__str__`, `__repr__`, and `__eq__`, which can be used to overload operators and provide custom behavior for common operations.



```python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __repr__(self) -> str:
        return f'Point(x={self.x},y={self.y})'

print('```')
print(Point(1,0) + Point(0,1))
print('```')

```

    ```
    Point(x=1,y=1)
    ```
    

Understanding Python classes is crucial for writing efficient and maintainable code. Classes provide a way to encapsulate data and behavior, implement inheritance for code reuse, and enable polymorphism for flexible design. Mastering classes and OOP in Python will give you a solid foundation for developing robust software solutions.

### Conclusion

This chapter has provided an overview of both foundational and advanced Python programming concepts that are essential for any developer aiming to write clean, efficient, and maintainable code. Starting from the basics, you have learned the importance of Python’s readable syntax and fundamental control structures. The discussion then progressed to advanced features like generators, decorators, and context managers, which are powerful tools for writing more concise and Pythonic code. Lastly, we explored Python's object-oriented programming through classes, emphasizing the importance of encapsulation and modularity in building scalable applications. These concepts are not only crucial in their own right but will also serve as the building blocks for the more advanced topics and programming patterns covered in later chapters. Mastering these Python features will enable you to better understand and implement the "Resumable Programming" techniques discussed throughout this book.

### Additional Notes

- **Python Documentation**: For deeper insights and advanced use cases, always refer to the [official Python documentation](https://docs.python.org/). It provides comprehensive details and examples that can help solidify your understanding.

- **Real Python** ([realpython.com](https://realpython.com)): A comprehensive site with tutorials, articles, and courses for all levels, from beginner to advanced Python topics. The site covers practical use cases and provides coding exercises to reinforce learning.
- **Talk Python Training** ([talkpython.fm/training](https://talkpython.fm/training)): Offers a range of video courses on Python development, focusing on topics like web development, data science, automation, and more. The site is known for its in-depth coverage and practical, real-world projects.
- **Full Stack Python** ([fullstackpython.com](https://www.fullstackpython.com/)): This resource is great for those who want to understand how Python fits into the full stack of web development. It covers everything from Python basics to deploying Python applications on different platforms.
- **LeetCode** ([leetcode.com](https://leetcode.com/)): For those interested in competitive programming and coding interviews, LeetCode provides a platform to practice advanced Python algorithms and data structures, with problems that range from easy to very challenging.
- **Python Software Foundation's Community** ([python.org/community](https://www.python.org/community/)): Engaging with Python's community through mailing lists, user groups, and local meetups is a great way to stay connected with other Python developers and learn from their experiences.
- **Advanced Python Patterns and Techniques** ([O'Reilly Learning](https://www.oreilly.com/)): O'Reilly's online learning platform offers books and video content that dive deep into Python patterns, performance optimization, and other advanced techniques.

---

## Chapter 2: Understanding Resumability

### Introduction
- **Overview**: Define resumable programming as the ability of a process to pause at certain points and then continue from those points later, either after a failure or after a deliberate halt. This capability is crucial for developing robust and scalable applications in environments where interruptions are common or where tasks are long-running.

- **Objective**: Equip readers with a foundational understanding of concepts and applications. By the end of this chapter, readers should appreciate the critical role that resumability plays in modern software development, particularly in distributed systems, cloud applications, and complex data processing workflows.


### Section 1: Why We Need Resumability
In today’s technological landscape, applications are increasingly expected to operate continuously and handle a variety of interruptions—be they from system failures, planned downtime, or user-driven pauses. Resumable programming addresses these needs by ensuring that applications can maintain their functionality and data integrity under such circumstances. 

let's think a simple example without resumability.


```python
print('```')
def fibonacci(n):
    if n <= 1 : return n
    return fibonacci(n-1)+fibonacci(n-2)

# Example
%time res = [(i,fibonacci(i))for i in range(37)]
print(f"\nFibonacci results: ... {res[-5:]}")
print('```')
```

    ```
    CPU times: user 11.3 s, sys: 110 ms, total: 11.4 s
    Wall time: 12.1 s
    
    Fibonacci results: ... [(32, 2178309), (33, 3524578), (34, 5702887), (35, 9227465), (36, 14930352)]
    ```
    


Here are some key reasons why resumability is essential from the example:

- **Reliability and Robustness**: In this example, we find that it is very time-consuming (about 11s) and computationally expensive. Applications that can resume from the last known good state are inherently more reliable. In environments where service interruptions are costly, such as in financial systems or critical infrastructure, the ability to recover quickly and seamlessly from failures is invaluable.

- **User Experience**: For end-users, the ability to pause and resume processes can significantly enhance the user experience, especially in terms of responsiveness. This is particularly evident in consumer applications like video streaming, downloads, or large file uploads, where users expect the ability to pause and resume activities at their convenience.

- **Scalability**: As systems grow and handle more parallel processes, the ability to manage and maintain state across these processes becomes crucial. Resumable programming facilitates scaling by allowing individual components or services to be paused and resumed independently, thus supporting graceful scaling and reducing bottlenecks.

- **Long-Running Processes**: Certain applications involve processes that inherently take a long time to complete, such as scientific simulations, batch processing jobs, or media encoding tasks. Resumability ensures that these long-running processes can continue from where they left off in the event of interruptions, without the need to start over.


Here's how we can implement a resumable Fibonacci function in Python, using **memoization** with persistent storage:


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
%time res = [(i,fibonacci(i))for i in range(37)]
print(f"\nFibonacci results: ... {res[-5:]}")
print('```')
```

    ```
    CPU times: user 27.3 ms, sys: 57.1 ms, total: 84.4 ms
    Wall time: 2.48 s
    
    Fibonacci results: ... [(32, 2178309), (33, 3524578), (34, 5702887), (35, 9227465), (36, 14930352)]
    ```
    


- **Key Features of This Resumable Implementation**:

    - **Persistence**: The use of a `shelve` database (we will discuss more databases later), which is a simple persistent storage for Fibonacci integers, allows the function to get/set results. If the process is interrupted, the previously computed values of the sequence are saved (this is also very beneficial when the app crashes unexpectedly).

    - **Performance**: By saving previously computed values, we avoid redundant calculations, thus minimizing re-computation. This drastically improves performance, especially for large `n`.

This approach illustrates a basic method to make the Fibonacci function resumable by using external storage for state. This can be extended to more complex algorithms and applications where resumability is crucial.

### Section 2: Core Concepts
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
    

- **First Way: Recording Machine State After Each Action**: This approach saves the entire state of the machine after each action using a key-value store. When an action results in a crash, the machine's state is restored from the last successful operation, and the action is retried.
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
- **Basic Example**:In Python, managing database transactions can be done effectively using the `sqlite3` library. Transactions in SQL databases like SQLite allow you to execute multiple operations in a safe, atomic manner. If an error occurs during one of the operations, you can roll back to the original state as if none of the operations had happened. This feature is crucial for implementing resumability because it ensures data integrity and consistency.

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

### Section 1: Components of MVC
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
    

- **Explanation** :
    - **MachineAModel** is a simple Python class representing the machine.
    - **MachineLibrary** handles the shelve database operations similar to the book library example.
    - **MachineView** provides methods to output the state of the machine and any errors.
    - **MachineController** manages interactions such as adding, resetting, and viewing machines.

Incorporating resumability into the MVC architecture enhances the robustness and user experience of applications, especially in environments where interruptions are common or expected. By carefully designing the model, view, and controller to handle interruptions gracefully, developers can create more resilient and flexible applications.

(PS: The following code is the action recording version, which is also very important when the target model is hard to initialize with arguments.)


```python
'Action Recording version'

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
   - Should be kept simple, akin to a data structure. Includes methods to get/set the model's state (**soft, not persistent**).
   - Should not perform persistent operations.
   - Focus on serialization and reconstruction.

- **Consideration of MachineLibrary (Controller)**:
   - MVC defines roles but not the number of classes, we can define many controllers that we needed.
   - MachineLibrary handles interactions (controlling) with **persistent storage** using the `shelve` library, such as retrieving and saving machine states.
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

An advanced example is the transitions between different states of matter: solid, liquid, gas, and plasma. These transitions can be very complex; for instance, converting a substance to a liquid can occur through two processes: melting and condensation. In this book, **we discuss simpler relationships** between states, where converting to a state typically involves defining a function, such as `to_some_state`.

![alt text](image.png)
- **Solid to Liquid**: Melting
- **Liquid to Solid**: Freezing
- **Liquid to Gas**: Vaporization
- **Gas to Liquid**: Condensation
- **Solid to Gas**: Sublimation
- **Gas to Solid**: Deposition
- **Gas to Plasma**: Ionization
- **Plasma to Gas**: Deionization

Both Melting and Condensation are transition processes that result in the formation of a liquid. In this book, we define them collectively as a single function called `to_Liquid`.

### Section 2: Finite State Machine(FSM) in Resumability

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
    Task moved to Completion.
    Task is completed.
    0:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task recovered from Failure, transitioning back to InitiationState.
    try No.2:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    1:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task recovered from Failure, transitioning back to InitiationState.
    try No.2:
    Task moved to Approval.
    Task moved to Execution.
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task recovered from Failure, transitioning back to InitiationState.
    try No.3:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    2:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    3:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task recovered from Failure, transitioning back to InitiationState.
    try No.2:
    Task moved to Approval.
    Task moved to Execution.
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task recovered from Failure, transitioning back to InitiationState.
    try No.3:
    Task moved to Approval.
    Task moved to Execution.
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task recovered from Failure, transitioning back to InitiationState.
    try No.4:
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
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task recovered from Failure, transitioning back to InitiationState.
    try No.2:
    Task moved to Approval.
    Task moved to Execution.
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task recovered from Failure, transitioning back to InitiationState.
    try No.3:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    9:
    try No.1:
    Task moved to Approval.
    Task moved to Execution.
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task recovered from Failure, transitioning back to InitiationState.
    try No.2:
    Task moved to Approval.
    Task moved to Execution.
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task recovered from Failure, transitioning back to InitiationState.
    try No.3:
    Task moved to Approval.
    Task moved to Execution.
    !!!!!!!!!!!!!This task crashed! Task moved to FailureState.!!!!!!!!!!!!!
    Task recovered from Failure, transitioning back to InitiationState.
    try No.4:
    Task moved to Approval.
    Task moved to Execution.
    Task moved to Completion.
    ```
    

This example involves very simple sequential tasks, meaning its states and transitions are minimal. However, in many cases, our system has many more states and transitions, making it difficult to do **Resumability** in a single function. As the following example shows, we will need a **solver**.


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
    print("Recovery path from", start_state, "to", end_state, ":", " -> ".join(path))
else:
    print("No path found from", start_state, "to", end_state)
print('```')
```

    ```
    Recovery path from loss to talk : loss -> init -> waiting -> connected -> talk
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
    def set_state(self, state): self.state = state
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
    def waiting(self, task: NetworkTask):                task.set_state(WaitingState())

class ConnectionEstablishedState(NetworkState):
    @staticmethod
    def _transitions(): return [ConnectionLostState,CommunicationState,ClosureState]    
    def connectionLost(self, task: NetworkTask):         task.set_state(ConnectionLostState())
    def communication(self, task: NetworkTask):          task.set_state(CommunicationState())
    def closure(self, task: NetworkTask):                task.set_state(ClosureState())

class ClosureState(NetworkState):
    @staticmethod
    def _transitions(): return [InitiationState]
    def initiation(self, task: NetworkTask):             task.set_state(InitiationState())

class ConnectionLostState(NetworkState):
    @staticmethod
    def _transitions(): return [InitiationState]
    def initiation(self, task: NetworkTask):             task.set_state(InitiationState())

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
    def connectionEstablished(self, task: NetworkTask):  task.set_state(ConnectionEstablishedState())
    def failure(self, task: NetworkTask):                task.set_state(FailureState())

class FailureState(NetworkState):
    @staticmethod
    def _transitions(): return [InitiationState]
    def initiation(self, task: NetworkTask):             task.set_state(InitiationState())

class CommunicationState(NetworkState):
    def simulate_communication(self, task: NetworkTask):
        time.sleep(1)
        if random.random() > 0.5:
            self.connectionLost(task)
            return True
        return False
        
    @staticmethod
    def _transitions(): return [ClosureState, ConnectionLostState]
    def closure(self, task: NetworkTask):                task.set_state(ClosureState())
    def connectionLost(self, task: NetworkTask):         task.set_state(ConnectionLostState())
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

## Chapter 6: Designing MVC & FSMs for Resumability

### Introduction

In the realm of software design, combining the Model-View-Controller (MVC) architectural pattern with Finite State Machines (FSMs) offers a robust framework for building resumable systems. This chapter delves into how the structured approach of MVC can be enhanced with the dynamic state management capabilities of FSMs to create highly resilient and maintainable applications. We will explore the integration of these two methodologies, demonstrating their effectiveness in managing complex state transitions while maintaining a clear separation of concerns.


### Section 1: Combine MVC and FSMs

- **Overview of MVC and FSM Integration** :

    MVC separates the concerns of an application into three interconnected components: the Model (data), the View (user interface), and the Controller (business logic). FSMs manage state transitions and behaviors in a predictable manner. Integrating FSMs within the MVC structure enhances the controller’s ability to manage state transitions in response to events triggered by user interactions or system changes.

- **Benefits of Integration** :

    - **Enhanced State Management**: FSMs provide a clear and organized way to handle the states within the controller, facilitating more manageable and predictable state transitions.
    - **Improved Resilience**: By defining explicit state transitions, systems can easily revert or recover to a stable state in case of errors, enhancing the application's robustness.
    - **Simplified Debugging and Testing**: Clear state management makes it easier to reproduce issues and test various parts of the application systematically.

- **Implementation Strategy** :

    - **Stateful Controllers**: Embed **FSMs within controllers** to manage the state of the model effectively, ensuring that the model reflects the correct state of the application at all times.
    - **Event-Driven Transitions**: Use events generated by user actions or system triggers to drive state changes, handled by the FSM within the controller.



```python
database = {"admin":"1234",
            "admin:role":"full",

            "anna":"5678",
            "anna:role":"readonly",
            }

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.role = 'not set'

class View:
    def display_login_form(self,model:User):
        print("---\nPlease enter name:[   ] password:[   ]")

    def display_welcome(self,model:User):
        print(f"---\nWelcome {model.username}, you are now logged in.")
        self.display_role(model)

    def display_role(self,model:User):
        print(f"You have {model.role} access permissions")

    def display_loginout(self,model:User):
        print(f"---\n{model.username} is now logged out.")

    def display_login_failed(self,model:User):
        print(f"Account of {model.username} is Login failed. Please try again.")

    def display_please_login_first(self,model:User):
        print("[warning]: Please login at first!")

    def display_loginout_again(self,model:User):
        print("[warning]: You are already Loginout.")

    def display_login_again(self,model:User):
        print("[warning]: You are already login.")

class UserAuthFSMsController:    
    def __init__(self, model:User, view:View):
        self.model = model
        self.view = view
        self.state = UserAuthState.Entry(self)
    
    ####################### data controll
    def set_role(self):
        self.model.role = database.get(self.model.username+':role',self.model.role)
    
    ####################### state controll
    def login(self):
        # maybe to do some database operations
        if database.get(self.model.username,None) == self.model.password:
            self.set_role()
            self.state.login()
        else:
            self.state = UserAuthState.LoginFailed(self)
        return self

    def logout(self):
        # maybe to do some database operations
        self.state.logout()
        return self
    
class UserAuthState:
    _transitions = {
        'Entry':       ['Entry','LoggedIn','LoginFailed'],
        'LoggedIn':    ['LoggedOut'],
        'LoggedOut':   ['Entry','LoggedIn'],
        'LoginFailed': ['Entry','LoggedIn'],
    }
    _states = list(_transitions.keys())
    
    class Base:
        def __init__(self,controller:UserAuthFSMsController):
            self.controller=controller
            self.model = self.controller.model
            
    class Entry(Base):
        def __init__(self, controller: UserAuthFSMsController):
            super().__init__(controller)
            View().display_login_form(controller.model)

        def login(self):
            self.controller.view.display_welcome(self.model)
            self.controller.state = UserAuthState.LoggedIn(self.controller)

        def logout(self):
            self.controller.view.display_please_login_first(self.model)

    class LoggedOut(Base):
        def login(self):
            self.controller.view.display_welcome(self.model)
            self.controller.state = UserAuthState.LoggedIn(self.controller)

        def logout(self):
            self.controller.view.display_loginout_again(self.model)

    class LoggedIn(Base):
        def login(self):
            self.controller.view.display_login_again(self.model)
            
        def logout(self):
            self.controller.view.display_loginout(self.model)
            self.controller.state = UserAuthState.LoggedOut(self.controller)

    class LoginFailed(Base):
        def __init__(self, controller: UserAuthFSMsController):
            super().__init__(controller)
            View().display_login_failed(self.model)

        def login(self):
            self.controller.view.display_welcome(self.model)
            self.controller.state = UserAuthState.LoggedIn(self.controller)
            
        def logout(self):
            self.controller.view.display_please_login_first(self.model)

print('```')
# Example Usage
controller = UserAuthFSMsController(
                User(username="admin", password="1234"),
                View()).login()  # Should log in successfully
controller.logout()

controller = UserAuthFSMsController(
                User(username="admin", password="wrongpassword"),
                View()).login()   # Should show login failed
controller.logout()

controller = UserAuthFSMsController(
                User(username="anna", password="5678"),
                View()).login()  # Should show login failed
controller.logout()  # Should log out successfully
print('```')

```

    ```
    ---
    Please enter name:[   ] password:[   ]
    ---
    Welcome admin, you are now logged in.
    You have full access permissions
    ---
    admin is now logged out.
    ---
    Please enter name:[   ] password:[   ]
    Account of admin is Login failed. Please try again.
    [warning]: Please login at first!
    ---
    Please enter name:[   ] password:[   ]
    ---
    Welcome anna, you are now logged in.
    You have readonly access permissions
    ---
    anna is now logged out.
    ```
    

- Design Review and Explanation

    - MVC Integration:
        - **Model (`User`)**: Manages user data such as username, password, and role.
        - **View (`View`)**: Responsible for outputting user-related messages and states, providing a direct way to give feedback based on different states or transitions.
        - **Controller (`UserAuthFSMsController`)**: Acts as the intermediary between the model and the view, manipulating the model based on user input and changing the view accordingly.

    - State Machine (in Controller) Implementation:
        - **State Definitions (`UserAuthState` classes)**: Each state (Entry, LoggedIn, LoggedOut, LoginFailed) inherits from a base state and defines specific behaviors for login and logout actions.
        - **Transition Management**: Transitions between states are handled inside state methods (`login` and `logout`), which update the controller's current state based on the outcome of actions (successful login, failed login, logout).

    - User Interaction:
        - On user login, the controller verifies credentials against a mock database. If successful, it transitions to the `LoggedIn` state; otherwise, it transitions to the `LoginFailed` state.
        - The `logout` method transitions from the `LoggedIn` state to the `LoggedOut` state.
        - Each state class uses the `View` class to communicate the result of actions to the user, maintaining clear feedback and interaction.

This code demonstrates how an FSM can be integrated within an MVC framework to manage user authentication in a resilient, stateful manner. The code effectively simulates user interactions, transitioning through various authentication states and providing appropriate feedback at each step.

### Section 2: Basic Resumable MVC & FSMs

- **Designing a Basic Resumable System by MVC & FSMs** :
A basic resumable system can be designed by implementing an FSM in the controller that handles key application states and transitions based on user interactions or process steps.

- **Example: Simple Socket Request System** :
Let's consider the following service: searching for something and communicating via socket.


```python
import socket
import json
import random
import time

def perform_search(query: str):
    # Simulate a random delay and occasional error in search
    if random.random() < 0.2:  # 20% chance to raise an error
        raise RuntimeError("Simulated search error")
    
    time.sleep(int(random.random() * 10))
    items = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
    results = [item for item in items if query.lower() in item.lower()]
    return results

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen()

    print("Server is listening on port 65432")

    while True:
        try:
            # Simulate a random delay and occasional error in connection acceptance
            if random.random() < 0.2:  # 20% chance to raise an error
                raise RuntimeError("Simulated connection acceptance error")
            
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
        except Exception as e:
            print(f"Error during connection acceptance: {e}")
            client_socket.close()
            continue

        try:
            data = client_socket.recv(1024)
            if not data:
                raise ValueError("No data received from client")

            query = data.decode('utf-8')
            print(f"Received search query: {query}")

            results = perform_search(query)
            response = json.dumps(results)

            client_socket.sendall(response.encode('utf-8'))
            print(f"Sent results: {response}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()
            print("Connection closed")

# start_server()

```

- **To design MVC(with FSMs)**:
  - **sequence for implementing** the client to connect to the server, send a search query, receive the results, and print them.
    - **Create and Connect the Client Socket**:
      - Create a socket object.
      - Connect the socket to the server address and port.

    - **Send the Search Query**:
      - Send the search query to the server in UTF-8 encoded format.

    - **Receive and Decode the Response**:
      - Receive the response from the server.
      - Decode the response from UTF-8 format and parse the JSON data.

    - **Close the Socket**: Close the client socket.

    - **Print the Results**: Print the search results received from the server.


  - **Model**: The `RequestModel` class holds the data required for Controller( with FSM ) operation, such as the request body, response body, URL, port, and timeout settings. It also includes a method to create a socket connection, `get_socket`, make a network instance connection without actual database write or read operations.

  - **View**: The `View` class is responsible for displaying the current state of the application to the user. It contains methods to print useful messages.

  - **Controller with FSM**: The `RequestFSMsController` class manages the finite state machine (FSM) logic, orchestrating state transitions and interacting with both the model and the view. It initializes with the model and view instances and sets the initial state to `RequestState.Initiation`. The controller provides methods to transition between states, such as `to_Initiation`, `to_WaitConnection`, `to_WaitSearching`, `to_ResponseReceived`, `to_Close`, and `to_Failure`. Each state transition updates the current state and uses the view to display the new state, while error handling is managed via decorators to ensure smooth transitions even in the presence of errors.


```python
database = {}

from collections import deque
import socket
import random
from functools import wraps
from dataclasses import dataclass
import uuid

class RequestModel:
    def __init__(self, request_body: str,
                 receive_body: str='NULL',  receive_sep:str = '\n',
                 url: str='localhost', port: int=65432, timeout=10):
        # useful for storing into database
        self.uuid = uuid.uuid4()
        self.url = url
        self.port = port
        self.timeout = timeout
        self.request_body = request_body
        self.receive_body = receive_body
        self.receive_sep = receive_sep

    # Soft creation, without database write or read operations.
    def get_socket(self):        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(self.timeout)
        return client_socket

# we do not use view, just a example
class View:
    def display_waiting_for_connection(self, model:RequestModel):
        print("Waiting for connection...")

    def display_searching(self, model:RequestModel):
        print("Searching...")

    def display_processing_start(self, model:RequestModel):
        print("Start received, processing...")

    def display_closed(self, model:RequestModel):
        print("Closed")

    def display_failure(self, model:RequestModel):
        print("Failure")

    def display_completed(self, model:RequestModel):
        print("Completed")

    def display_transaction_closed(self, model:RequestModel):
        print("Transaction closed")

    def display_initiation(self, model:RequestModel):
        print("Initiation")

    def display_error(self, model:RequestModel):
        print("Error occurred")

    def display_restart(self, model:RequestModel):
        print("Restarting...")
    
    
class RequestFSMsController:
    def __init__(self, model:RequestModel, view):
        # private tmp var
        self._socket:socket.socket = None
        
        self.model = model
        self.view = view
        # self.state = RequestState.Initiation(self)
        self.set_state(RequestState.Initiation)
    
    ################# public
    def get_transitions(self):        return RequestState._transitions
    def current_state(self):          return self.state.__class__.__name__

    def resume_state(self,target_state, max_attempts=100):
        self._resume_state(target_state, max_attempts)

    def to_Initiation(self):          self.state.to_Initiation()
    def to_WaitConnection(self):      self.state.to_WaitConnection()
    def to_WaitSearching(self):       self.state.to_WaitSearching()
    def to_ResponseReceived(self):    self.state.to_ResponseReceived()
    def to_Close(self):               self.state.to_Close()
    def to_Failure(self):             self.state.to_Failure()

    ################# private
    ######################## socket controlls (will call from state controlls)
    def init_socket(self): self._socket=self.model.get_socket()
    def connect(self):     self._socket.connect((self.model.url, self.model.port))
    def send(self):        self._socket.send(self.model.request_body.encode())            
    def close(self):       self._socket.close()
    
    def recieve(self):
        # !!!! Write operation , maybe need database
        self.model.receive_body = self._socket.recv(1024).decode()
        if self.model.receive_body == '':
            raise ValueError('recieve invalid data (empty) from server!')

    ######################## state controlls
    def set_state(self, state_class): self.state:RequestState.Base = state_class(self)

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
    
    def _resume_state(self,target_state, max_attempts=100):
        print(f'Set target state: {target_state} ( current is {self.current_state()})')
        def next_action(task:RequestFSMsController,target_state):
            path = self.find_path(task.get_transitions(), task.current_state(), target_state)
            if len(path)<=1: return None
            return path[1]
            
        while self.current_state() != target_state:
            cls = next_action(self,target_state)
            if cls is None:raise ValueError('no next acion! unreachable!')
            if max_attempts<0:raise ValueError(f'over max_attempts!')
            
            print(f'Current: {self.current_state()}, try to_{cls}')
            getattr(self,f'to_{cls}')()
            max_attempts -= 1
        print(f'Success to target state: {self.current_state()}')


############################ for FSMs 
def handle_errors(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self:RequestState.Base=self
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            print(f'[{self.__class__.__name__}]: {e}')
            self.to_Failure()
    return wrapper
    
class RequestState:
    @dataclass
    class States:
        Initiation='Initiation'
        WaitConnection='WaitConnection'
        WaitSearching='WaitSearching'
        ResponseReceived='ResponseReceived'
        Close='Close'
        Failure='Failure'

    _transitions = {
        States.Initiation:      [States.WaitConnection, States.Failure],
        States.WaitConnection:  [States.WaitSearching, States.Close, States.Failure],
        States.WaitSearching:   [States.ResponseReceived, States.Close, States.Failure],
        States.ResponseReceived:[States.Close, States.Failure],
        States.Close:           [States.Initiation],
        States.Failure:         [States.Initiation]
    }
    _states = list(_transitions.keys())
    
    class Base:
        def __init__(self, controller: RequestFSMsController):
            self.controller = controller
            self.model = self.controller.model

        def _Initiation(self):
            self.controller._socket = None
            self.controller.set_state(RequestState.Initiation)

        def _Failure(self):
            self.controller.set_state(RequestState.Failure)
        
        def _defult_error(self,to): 
            raise NotImplementedError(f"Invalid transition from [{self.__class__.__name__}] -> [{to}]")

        def to_Initiation(self):      self._defult_error("Initiation")
        def to_WaitConnection(self):  self._defult_error("WaitConnection")
        def to_WaitSearching(self):   self._defult_error("WaitSearching")
        def to_ResponseReceived(self):self._defult_error("ResponseReceived")
        def to_Close(self):           self._defult_error("Close")
        def to_Failure(self):         self._defult_error("Failure")

    class Close(Base):
        _transitions = ['Initiation']
        @handle_errors
        def to_Initiation(self):self._Initiation()

    class Failure(Base):
        _transitions = ['Initiation']
        @handle_errors
        def to_Initiation(self):self._Initiation()

    ##############################  following code is useful for debug and simulation    

    class Initiation(Base):
        # These to_XXXX functions need to implement
        _transitions = ['WaitConnection', 'Failure']
        
        @handle_errors
        def __init__(self, controller: RequestFSMsController):
            super().__init__(controller)
            self.controller.init_socket()
            if random.random() > 0.5:raise ValueError('network error!')

        @handle_errors
        def to_WaitConnection(self):
            self.controller.set_state(RequestState.WaitConnection)
            if random.random() > 0.5:raise ValueError('network error!')
            
        def to_Failure(self):self._Failure()

    class WaitConnection(Base):
        _transitions = ['WaitSearching', 'Close', 'Failure']
        
        @handle_errors
        def to_WaitSearching(self):
            if random.random() > 0.5:raise ValueError('network error!')
            self.controller.set_state(RequestState.WaitSearching)
        
        @handle_errors
        def to_Close(self):
            if random.random() > 0.5:raise ValueError('network error!')
            self.controller.set_state(RequestState.Close)
            
        def to_Failure(self):self._Failure()

    class WaitSearching(Base):
        _transitions = ['ResponseReceived', 'Close', 'Failure']
        
        @handle_errors
        def to_ResponseReceived(self):
            if random.random() > 0.5:raise ValueError('network error!')
            # !!!! Write operation , maybe need database
            # self.model.receive_body = data
            print('self.model.receive_body = xxxx')
            self.controller.set_state(RequestState.ResponseReceived)
        
        @handle_errors
        def to_Close(self):
            if random.random() > 0.5:raise ValueError('network error!')
            self.controller.set_state(RequestState.Close)

        def to_Failure(self):self._Failure()

    class ResponseReceived(Base):
        _transitions = ['Close', 'Failure']

        @handle_errors
        def to_Close(self):
            if random.random() > 0.5:raise ValueError('network error!')
            self.controller.set_state(RequestState.Close)

        def to_Failure(self):self._Failure()
```


```python
print('```')
# Example of normal usage (maybe get random error!)
search_request = RequestFSMsController(RequestModel(request_body='apple'),View())
search_request.to_WaitConnection()
search_request.to_WaitSearching()
search_request.to_ResponseReceived()
search_request.to_Close()
print('```')
```

```python
	"name": "NotImplementedError",
	"message": "Invalid transition from [Failure] -> [WaitSearching]",
	"stack": "---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
Cell In[18], line 5
      3 search_request = RequestFSMsController(RequestModel(request_body='apple'),View())
      4 search_request.to_WaitConnection()
----> 5 search_request.to_WaitSearching()
      6 search_request.to_ResponseReceived()
      7 search_request.to_Close()

Cell In[15], line 91, in RequestFSMsController.to_WaitSearching(self)
---> 91 def to_WaitSearching(self):   self.state.to_WaitSearching()

Cell In[15], line 180, in RequestState.Base.to_WaitSearching(self)
--> 180 def to_WaitSearching(self):   self._defult_error(\"WaitSearching\")

Cell In[15], line 176, in RequestState.Base._defult_error(self, to)
    175 def _defult_error(self,to): 
--> 176     raise NotImplementedError(f\"Invalid transition from [{self.__class__.__name__}] -> [{to}]\")

NotImplementedError: Invalid transition from [Failure] -> [WaitSearching]"
```


```python
print('```')
# Example resumability
search_request = RequestFSMsController(RequestModel(request_body='apple'),View())
search_request.resume_state(target_state = RequestState.States.ResponseReceived)
print('```')
```

    ```
    [Initiation]: network error!
    Set target state: ResponseReceived ( current is Initiation)
    Current: Initiation, try to_WaitConnection
    Current: WaitConnection, try to_WaitSearching
    [WaitConnection]: network error!
    Current: Failure, try to_Initiation
    [Initiation]: network error!
    Current: Initiation, try to_WaitConnection
    [Initiation]: network error!
    Current: Failure, try to_Initiation
    Current: Initiation, try to_WaitConnection
    Current: WaitConnection, try to_WaitSearching
    Current: WaitSearching, try to_ResponseReceived
    self.model.receive_body = xxxx
    Success to target state: ResponseReceived
    ```
    

Let's implement an interactive controller with the previous server.


```python
class RequestState:
    @dataclass
    class States:
        Initiation='Initiation'
        WaitConnection='WaitConnection'
        WaitSearching='WaitSearching'
        ResponseReceived='ResponseReceived'
        Close='Close'
        Failure='Failure'

    _transitions = {
        States.Initiation:      [States.WaitConnection, States.Failure],
        States.WaitConnection:  [States.WaitSearching, States.Close, States.Failure],
        States.WaitSearching:   [States.ResponseReceived, States.Close, States.Failure],
        States.ResponseReceived:[States.Close, States.Failure],
        States.Close:           [States.Initiation],
        States.Failure:         [States.Initiation]
    }
    _states = list(_transitions.keys())
    
    class Base:
        
        def __init__(self, controller: RequestFSMsController):
            self.controller = controller
            self.model = self.controller.model

        def _Initiation(self):
            self.controller._socket = None
            self.controller.set_state(RequestState.Initiation)

        def _Failure(self):
            self.controller.set_state(RequestState.Failure)
            
        def _Close(self):
            self.controller.close()
            self.controller.set_state(RequestState.Close)
        
        def _defult_error(self,to): 
            raise NotImplementedError(f"Invalid transition from [{self.__class__.__name__}] -> [{to}]")

        def to_Initiation(self):      self._defult_error("Initiation")
        def to_WaitConnection(self):  self._defult_error("WaitConnection")
        def to_WaitSearching(self):   self._defult_error("WaitSearching")
        def to_ResponseReceived(self):self._defult_error("ResponseReceived")
        def to_Close(self):           self._defult_error("Close")
        def to_Failure(self):         self._defult_error("Failure")


    class Close(Base):
        _transitions = ['Initiation']
        @handle_errors
        def to_Initiation(self):self._Initiation()

    class Failure(Base):
        _transitions = ['Initiation']
        @handle_errors
        def to_Initiation(self):self._Initiation()

    ##############################  following code is an interactive controller with the above server

    class Initiation(Base):
        # These to_XXXX functions need to implement
        _transitions = ['WaitConnection', 'Failure']
        
        @handle_errors
        def __init__(self, controller: RequestFSMsController):
            super().__init__(controller)
            self.controller.init_socket()

        @handle_errors
        def to_WaitConnection(self):
            self.controller.set_state(RequestState.WaitConnection)
            self.controller.connect()
            
        def to_Failure(self):self._Failure()

    class WaitConnection(Base):
        _transitions = ['WaitSearching', 'Close', 'Failure']
        
        @handle_errors
        def to_WaitSearching(self):
            self.controller.send()
            self.controller.set_state(RequestState.WaitSearching)
        
        @handle_errors
        def to_Close(self):self._Close()

        def to_Failure(self):self._Failure()

    class WaitSearching(Base):
        _transitions = ['ResponseReceived', 'Close', 'Failure']
        
        @handle_errors
        def to_ResponseReceived(self):
            self.controller.recieve()
            print('receive_body = ',self.model.receive_body)
            self.controller.set_state(RequestState.ResponseReceived)
        
        @handle_errors
        def to_Close(self):self._Close()

        def to_Failure(self):self._Failure()

    class ResponseReceived(Base):
        _transitions = ['Close', 'Failure']

        @handle_errors
        def to_Close(self):self._Close()

        def to_Failure(self):self._Failure()
```


```python
print('```')
'Before running this code, we need to start up the previous server code!'
# Example resumability with real server
search_request = RequestFSMsController(RequestModel(request_body='ap'),View())
search_request.resume_state(target_state = RequestState.States.ResponseReceived)
print('```')
```

    ```
    Set target state: ResponseReceived ( current is Initiation)
    Current: Initiation, try to_WaitConnection
    Current: WaitConnection, try to_WaitSearching
    Current: WaitSearching, try to_ResponseReceived
    [WaitSearching]: recieve invalid data (empty) from server!
    Current: Failure, try to_Initiation
    Current: Initiation, try to_WaitConnection
    Current: WaitConnection, try to_WaitSearching
    Current: WaitSearching, try to_ResponseReceived
    receive_body =  ["apple", "grape"]
    Success to target state: ResponseReceived
    ```
    

Let's take a look at the implementation conclusion.
First of all, we need to define our model clearly.
A model class can also be considered as a record of our data, or a schema.
In the model class, we do not perform hard operations (such as reading or writing database).

- **Hard operation**: something that will result in durability.
  - For example:
    - Database operations, such as writing, will change data durably. Sometimes, reading could be considered a soft operation, except when it changes model instance member information.
    - File or Internet I/O may cause changes to the program state. These changes are also considered hard operations, especially in case of failure.
    - Setter of the model member information.

- **Soft operation**: something that will not result in durability.
  - For example:
    - Creation of an instance which is not a singleton. This operation must ensure that it does not change data durably or alter the program state.
    - Getter of the member information.

We prefer to implement hard operations in the Controller ( with FSMs ) class. The implementation of FSMs will make the code redundant and complex. However, we will greatly benefit from **(auto) resumability**.

The following complete code provides additional functionality for interacting with the database (MongoDB).


```python
import socket
import json
import random
import time

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen()

    print("Server is listening on port 65432")

    def perform_search(query: str):
        # Simulate a random delay and occasional error in search
        if random.random() < 0.2:  # 20% chance to raise an error
            raise RuntimeError("Simulated search error")
        
        time.sleep(int(random.random() * 10))
        items = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
        results = [item for item in items if query.lower() in item.lower()]
        return results
    
    while True:
        try:
            # Simulate a random delay and occasional error in connection acceptance
            if random.random() < 0.2:  # 20% chance to raise an error
                raise RuntimeError("Simulated connection acceptance error")
            
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
        except Exception as e:
            print(f"Error during connection acceptance: {e}")
            client_socket.close()
            continue

        try:
            data = client_socket.recv(1024)
            if not data:
                raise ValueError("No data received from client")

            query = data.decode('utf-8')
            print(f"Received search query: {query}")

            results = perform_search(query)
            response = json.dumps(results)

            client_socket.sendall(response.encode('utf-8'))
            print(f"Sent results: {response}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()
            print("Connection closed")


from collections import deque
import socket
from functools import wraps
from dataclasses import dataclass
import uuid
from pymongo import MongoClient, errors

class MongoDBStorage:
    def __init__(self):        
        """ Create a database connection to a MongoDB database """
        try:
            self.conn = MongoClient('mongodb://localhost:27017/')
            self.db = self.conn.get_database('request_db')
            self.collection = self.db.get_collection('Request')
        except errors.ConnectionFailure as e:
            print("Connection error:", e)

    def _ID_KEY(self):return '_id'

    def exists(self, key: str)->bool:
        return self.collection.find_one({self._ID_KEY(): key}) is not None

    def set(self, key: str, value: dict):
        self.collection.update_one({self._ID_KEY(): key}, {"$set": value}, upsert=True)

    def get(self, key: str)->dict:
        res = self.collection.find_one({self._ID_KEY(): key})            
        if res: del res['_id']
        return res

    def delete(self, key: str):
        self.collection.delete_one({self._ID_KEY(): key})

    def keys(self, pattern: str = '*')->list[str]:
        regex = '^'+pattern.replace('*', '.*')
        return [doc['_id'] for doc in self.collection.find({self._ID_KEY(): {"$regex": regex}})]

database = MongoDBStorage()

class RequestModel:
    def __init__(self, request_body: str,
                 receive_body: str='NULL',  receive_sep:str = '\n',
                 url: str='localhost', port: int=65432, timeout=10,
                 _uuid=None):
        # useful for storing into database
        self.uuid = _uuid if _uuid else str(uuid.uuid4())
        self.url = url
        self.port = port
        self.timeout = timeout
        self.request_body = request_body
        self.receive_body = receive_body
        self.receive_sep = receive_sep
    
    @staticmethod
    def from_dict(uuid,d):
        return RequestModel(
             _uuid = uuid,
             url = d['url'],
             port = d['port'],
             timeout = d['timeout'],
             request_body = d['request_body'],
             receive_body = d['receive_body'],
             receive_sep = d['receive_sep'])

    def to_dict(self):
        return dict(
             uuid = self.uuid,
             url = self.url,
             port = self.port,
             timeout = self.timeout,
             request_body = self.request_body,
             receive_body = self.receive_body,
             receive_sep = self.receive_sep)

    # Soft creation, without database write or read operations.
    def get_socket(self):        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(self.timeout)
        return client_socket

# we do not use view, just a example
class View:
    def display_waiting_for_connection(self, model:RequestModel):
        print("Waiting for connection...")

    def display_searching(self, model:RequestModel):
        print("Searching...")

    def display_processing_start(self, model:RequestModel):
        print("Start received, processing...")

    def display_closed(self, model:RequestModel):
        print("Closed")

    def display_failure(self, model:RequestModel):
        print("Failure")

    def display_completed(self, model:RequestModel):
        print("Completed")

    def display_transaction_closed(self, model:RequestModel):
        print("Transaction closed")

    def display_initiation(self, model:RequestModel):
        print("Initiation")

    def display_error(self, model:RequestModel):
        print("Error occurred")

    def display_restart(self, model:RequestModel):
        print("Restarting...")
    
# a simpler combined implementation
class RequestFSMsController:
    # define states
    class States:
        Initiation='Initiation'
        WaitConnection='WaitConnection'
        WaitSearching='WaitSearching'
        ResponseReceived='ResponseReceived'
        Close='Close'
        Failure='Failure'

    _transitions = {
        States.Initiation:      [States.WaitConnection, States.Failure],
        States.WaitConnection:  [States.WaitSearching, States.Close, States.Failure],
        States.WaitSearching:   [States.ResponseReceived, States.Close, States.Failure],
        States.ResponseReceived:[States.Close, States.Failure],
        States.Close:           [States.Initiation],
        States.Failure:         [States.Initiation]
    }
    _states = list(_transitions.keys())

    def __init__(self, model:RequestModel, view):
        # private tmp var
        self._socket:socket.socket = None
        
        self.model = model
        self.view = view
        # self.state = RequestState.Initiation(self)
        database.set(model.uuid,model.to_dict())

        self.init_socket()
        self._state = RequestState.States.Initiation
    
    ################# public
    def get_transitions(self):        return RequestState._transitions
    def current_state(self):          return self._state

    def to_Failure(self):
        self._state = RequestState.States.Failure
    
    def handle_errors(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self:RequestState=self
            valid_transitions = self._transitions[self._state]
            target = func.__name__.replace('to_','')        
            if target not in valid_transitions:            
                raise ValueError(f"Invalid transition from [{self._state}] -> [{target}]")
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                print(f'[{self.__class__.__name__}]: {e}')
                self.to_Failure()
        return wrapper
    
    @handle_errors
    def to_Initiation(self):
        self.init_socket()
        self._state = RequestState.States.Initiation
    
    @handle_errors
    def to_Close(self):
        self.close()
        self._state = RequestState.States.Close

    @handle_errors
    def to_WaitConnection(self):
        self._state = RequestState.States.WaitConnection
        self.connect()

    @handle_errors
    def to_WaitSearching(self):
        self.send()
        self._state = RequestState.States.WaitSearching

    @handle_errors
    def to_ResponseReceived(self):
        self.recieve()
        print('receive_body = ',self.model.receive_body)
        self._state = RequestState.States.ResponseReceived

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
        def next_action(task:RequestState,target_state):
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

    ################# private
    ######################## socket controlls (will call from state controlls)
    def init_socket(self): self._socket=self.model.get_socket()
    def connect(self):     self._socket.connect((self.model.url, self.model.port))
    def send(self):        self._socket.send(self.model.request_body.encode())            
    def close(self):       self._socket.close()
    
    def recieve(self):
        # !!!! Write operation , maybe need database
        self.model.receive_body = self._socket.recv(1024).decode()
        if self.model.receive_body == '':
            raise ValueError('recieve invalid data (empty) from server!')
        database.set(self.model.uuid,self.model.to_dict())

```


```python
print('```')
# show database , it will be empty at first time
# maybe we can try implment class View instead of print method
print(f"show database keys : {database.keys('*')}\n")
# we can try sending 10 requests
for i in range(10):    
    try:
        # database will store model at controller init
        search_request = RequestFSMsController(RequestModel(request_body='ap'),View())
        search_request.to_WaitConnection()
        search_request.to_WaitSearching()
        # database will store model at ResponseReceived
        search_request.to_ResponseReceived()
        search_request.to_Close()
    except Exception as e:
        print(e)

# show failure requests
failures = [k for k in database.keys('*') if database.get(k)['receive_body']=='NULL']
print(f"show failures keys : {failures}\n")

for k in failures:
    print(f'\ntry resume request of {k}')
    model = RequestModel.from_dict(k,database.get(k))
    search_request = RequestFSMsController(model,View())
    # database will store model at ResponseReceived
    search_request.resume_state(target_state = RequestState.States.ResponseReceived)

# show database , and find failure requests, again
failures = [k for k in database.keys('*') if database.get(k)['receive_body']=='NULL']
print(f"\nshow failures keys : {failures}\n")

# delete all
for k in database.keys('*'):database.delete(k)
print('```')
```

    ```
    show database keys : []
    
    receive_body =  ["apple", "grape"]
    receive_body =  ["apple", "grape"]
    receive_body =  ["apple", "grape"]
    receive_body =  ["apple", "grape"]
    receive_body =  ["apple", "grape"]
    receive_body =  ["apple", "grape"]
    receive_body =  ["apple", "grape"]
    [RequestState]: recieve invalid data (empty) from server!
    Invalid transition from [Failure] -> [Close]
    receive_body =  ["apple", "grape"]
    [RequestState]: recieve invalid data (empty) from server!
    Invalid transition from [Failure] -> [Close]
    show failures keys : ['7f307946-893d-4cc2-b248-11792a0250d4', '82104289-a8cf-410e-8c67-f4167f813310']
    
    
    try resume request of 7f307946-893d-4cc2-b248-11792a0250d4
    Set target state: ResponseReceived ( current is Initiation)
    Current: Initiation, try to_WaitConnection
    Current: WaitConnection, try to_WaitSearching
    Current: WaitSearching, try to_ResponseReceived
    receive_body =  ["apple", "grape"]
    Success to target state: ResponseReceived
    
    try resume request of 82104289-a8cf-410e-8c67-f4167f813310
    Set target state: ResponseReceived ( current is Initiation)
    Current: Initiation, try to_WaitConnection
    Current: WaitConnection, try to_WaitSearching
    Current: WaitSearching, try to_ResponseReceived
    receive_body =  ["apple", "grape"]
    Success to target state: ResponseReceived
    
    show failures keys : []
    
    ```
    

### Section 3: Advance Resumable MVC&FSMs

- **Designing a advance Resumable System by MVC & FSMs** :
An advanced resumable system can be considered to have more transitions and states, especially passive states and dynamic transitions.

- **Passive transition and state** :

    Let's consider the following case: waiting for a signal via socket and changing the state accordingly.

    In this FSM, the system starts in the Idle state. It transitions to SignalReceivedState when it receive signal.

    **| IdleState | --ReceiveSignal--> | SignalReceivedState |**

    Here is the problem: the ReceiveSignal process will not end immediately, and we do not know the exact time it will take. 

    We usually prefer to perform transitions (to set the machine state) instantly, especially for asynchronous processing.

    The following is a design for passive states. We can split a passive state into a waiting part and a fixed part.

    **|IdleState| --StartListening--> | WaitingForSignalState | --ReceiveSignal--> | SignalReceivedState |**

- **Dynamic transition and state** :

    In previous examples, we consider that the list of states and the table of transitions would remain unchanged over time.

    In dynamic situations, transitions or states change over time. Consider this example:

    A robot is trying to clean a table that has many items on it. For instance, there is an apple, some waste paper, and other things on the table. The robot will move each item as follows:

    - Apple -> fridge
    - Waste paper -> trash bin

    We can define states and transitions as follows:

    - states: [idle, catch_apple, to_fridge, catch_waste_paper, to_trash_bin, place]
    - transitions: 
        - idle -> [catch_apple, catch_waste_paper, to_table]
        - catch_apple -> [to_fridge]
        - to_fridge -> [place]
        - catch_waste_paper -> [to_trash_bin]
        - to_trash_bin -> [place]
        - place -> [idle]

    Now, we want to add a process for handling a book, specifically "book -> bookshelf," when a book is on the table. In Python, we can easily modify the instance’s members to process the book with the following code:

    ```python
        robotA.add_state('catch_book')
        robotA.add_state('to_bookshelf')

        robotA.add_transition('catch_book', ['to_bookshelf'])
        robotA.add_transition('to_bookshelf', ['place'])

        robotA.add_transition_func('catch_book', lambda: 'try catching book')
        robotA.add_transition_func('to_bookshelf', lambda: 'try going to bookshelf')
    ```

    How do we handle an increasing number of transitions and states? 

    - We have a path solver of `find_path`! In the previous examples, we used a very simple one, but we can introduce much smarter solvers.

### Conclusion

Throughout this chapter, we've explored the integration of the Model-View-Controller (MVC) framework with Finite State Machines (FSMs) to enhance resumability in software systems. This combination provides a robust architecture for managing complex state transitions in a clear and maintainable manner. The practical examples and case studies illustrated not only the theoretical aspects of MVC and FSM integration but also demonstrated their practical applications in real-world scenarios.

#### Key Takeaways:
- **Structured System Design**: Combining MVC and FSMs helps in structuring applications that are both resilient and easy to manage. The MVC framework ensures a clear separation of concerns, while FSMs offer precise control over state transitions.

- **Enhanced Error Handling and Resilience**: The use of FSMs within the MVC architecture allows systems to handle errors gracefully and recover from unexpected states, thereby enhancing the resilience of the application.

- **Improved Maintainability and Scalability**: The clear demarcation of responsibilities and states leads to better maintainability. Systems designed with MVC and FSMs can be easily scaled and adapted to new requirements without extensive modifications.

### Additional Notes:
- **Future Directions**: As systems continue to grow in complexity and scale, the integration of MVC and FSMs will become increasingly crucial. Future research and development might focus on automating state management and further enhancing the scalability of these systems.

- **Implementation Challenges**: While the benefits are substantial, the implementation of FSMs within an MVC framework requires careful planning and understanding of both state management and application architecture. Developers must consider the specific needs of their applications and the potential complexity that FSMs might introduce.

- **Educational Opportunities**: There is a significant opportunity for educational programs to incorporate teaching modules that focus on advanced architectural patterns like MVC combined with FSMs. This knowledge will empower upcoming developers to build more robust and efficient systems.

- **Community Contributions**: Open-source contributions and community-driven projects can play a pivotal role in refining the MVC and FSM integration techniques. Sharing real-world problems and solutions can help in evolving these architectural patterns to better meet the needs of modern software development.

---

## Chapter 7: Practical Applications and Case Studies

### Introduction

In this chapter, we delve into the practical applications and case studies of resumable programming, showcasing real-world scenarios where the techniques and concepts discussed in the previous chapters are implemented effectively. Resumable programming is not just a theoretical concept but a vital tool in the development of robust, scalable, and fault-tolerant systems. By examining various case studies across different industries, this chapter aims to illustrate the diverse applications of resumability, demonstrating how it enhances system reliability, user experience, and overall performance.

**Objectives:**
- **Illustrate Real-World Implementation**: Provide insights into how resumable programming is integrated into commercial and open-source projects.
- **Demonstrate Benefits**: Highlight the tangible benefits that resumable programming brings to systems, including increased uptime, better error handling, and smoother user interactions.
- **Inspire Innovation**: Encourage readers to consider how the principles of resumability can be adapted and applied in their own projects.

Through a series of case studies, ranging from web applications to distributed systems and even embedded devices, this chapter will explore how developers around the world are leveraging resumable programming to solve complex challenges. Each case study will detail the problem faced, the resumability approach taken, and the outcomes achieved, providing a comprehensive overview of the practical deployment of resumable systems.

### Section 0: Preparation
In the previous example, we needed **persistent storage** to store states and data models. In this chapter, we will use the following NoSQL storage code.


```python
from pymongo import MongoClient, errors

# The following code is for those who want a ready-to-use production solution.
class MongoDBStorage:
    def __init__(self):        
        """ Create a database connection to a MongoDB database """
        try:
            # Please change following settings to MongoDB Atlas Cloud Platform
            # self.conn = MongoClient('mongodb+srv://**USER_NAME**:**PASSWORD**@atlascluster.xxxx.mongodb.net/')
            self.conn = MongoClient('mongodb://localhost:27017/')
            self.db = self.conn.get_database('ResumableProgramming')
            self.collection = self.db.get_collection('Chapter7')
        except errors.ConnectionFailure as e:
            print("Connection error:", e)

    def _ID_KEY(self):return '_id'

    def exists(self, key: str)->bool:
        return self.collection.find_one({self._ID_KEY(): key}) is not None

    def set(self, key: str, value: dict):
        self.collection.update_one({self._ID_KEY(): key}, {"$set": value}, upsert=True)

    def get(self, key: str)->dict:
        res = self.collection.find_one({self._ID_KEY(): key})            
        if res: del res['_id']
        return res

    def delete(self, key: str):
        self.collection.delete_one({self._ID_KEY(): key})

    def keys(self, pattern: str = '*')->list[str]:
        regex = '^'+pattern.replace('*', '.*')
        return [doc['_id'] for doc in self.collection.find({self._ID_KEY(): {"$regex": regex}})]
    
    def clean(self):
        for k in self.keys():self.delete(k)

# If you do not have MongoDB, we also provide the following simple local solution.
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

# test the storage
def test_storage():
    storage = ShelveStorage()
    # storage = MongoDBStorage()

    try:
        # Test set and get
        storage.set('key1', {'name': 'Alice', 'age': 30})
        result = storage.get('key1')
        assert result == {'name': 'Alice', 'age': 30}, f"Expected {{'name': 'Alice', 'age': 30}}, got {result}"

        # Test exists
        storage.set('key2', {'name': 'Bob', 'age': 25})
        assert storage.exists('key2'), "Expected key2 to exist"
        assert not storage.exists('key3'), "Expected key3 to not exist"

        # Test delete
        storage.set('key4', {'name': 'Charlie', 'age': 40})
        storage.delete('key4')
        assert not storage.exists('key4'), "Expected key4 to be deleted"
        assert storage.get('key4') is None, "Expected key4 to be None after deletion"
        storage.clean()

        # Test keys
        storage.set('keyA', {'value': 1})
        storage.set('keyB', {'value': 2})
        storage.set('keyC', {'value': 3})

        keys = storage.keys('key*')
        assert set(keys) == {'keyA', 'keyB', 'keyC'}, f"Expected keys {{'keyA', 'keyB', 'keyC'}}, got {set(keys)}"

        # Test close and persistence
        storage.set('key5', {'name': 'David', 'age': 50})
        del storage
        
        storage = ShelveStorage()
        # storage = MongoDBStorage()
        storage.get('key5') == {'name': 'David', 'age': 50}, f"Expected {{'name': 'David', 'age': 50}}, got {storage.get('key5')}"

        print("All tests passed successfully!")

    finally:
        storage.clean()

# Run the tests
test_storage()
```

    All tests passed successfully!
    

Furthermore, you can also try a cloud key-value solution like Firestore or AWS DynamoDB, which will make your solution global and highly resilient.

### Section 1: Resumable Large File Uploading Service
Let's consider a large file uploading service (in AWS Lambda and S3).

1. The user selects a large file and uploads it.
2. This service will upload the file as chunks into S3.
3. When the uploading is complete, we can merge all chuncks by using S3 SDK.
4. User can pause uploading any time and resume it.

Why do we need to record state for uploading (in AWS Lambda and S3)?
- Many cloud solutions, such as AWS Lambda, can only run for a maximum of 15 minutes.
- Sometimes the uploading will take longer than 15 minutes!
- S3 do not manage the file uploading states for user.

In this example, the server needs to track the state of the user's large file and uploading task. 

The possible states and transitions are like following python code:



```python
class S3LargeUploadingState:
    class States:
        idle = 'idle'
        recieving = 'recieving'
        recieved = 'recieved'
        recieve_failure = 'recieve_failure'
        merged = 'merged'
        merge_failure = 'merge_failure'

    _transitions = {
        States.idle:             [States.recieving],
        States.recieving:        [States.recieved, States.recieve_failure, States.idle],
        States.recieve_failure:  [States.recieving], # retry recieving
        States.recieved:         [States.merged, States.merge_failure],
        States.merge_failure:    [States.merged],
        States.merged:           [], # end of task life
        
    }
    _states = list(_transitions.keys())
```

Let's consider this service MVC(FSMs)'s Model and Controller.


```python
import os
from functools import wraps

# aws settings
import boto3
BUCKET_NAME = os.environ['AWS_S3_BUCKET_NAME']
def get_s3_client():
    return boto3.client(
        service_name='s3',
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
        region_name=os.environ['AWS_DEFAULT_REGION'])

# easy to change back end
class DBStorage(MongoDBStorage):
    pass

class S3LargeUploadingModel:
    def __init__(self,file_name=None,file_size=0,file_hash=None,
                upload_id=None,chunk_size = 5 * 1024 * 1024,
                parts = [],) -> None:
        
        # Initialize the file name as None, to be set when the upload process starts
        self.file_name = file_name
        
        # Initialize the file size as None, to be set when the file information is provided
        self.file_size = file_size
        
        # Initialize the file hash as None, can be used for data integrity checks
        self.file_hash = file_hash
        
        # Initialize the upload ID as None, which will be assigned once the upload session is initiated
        self.upload_id = upload_id
        
        # Set the chunk size to 5 MB (5 * 1024 * 1024 bytes); this size dictates how large each part of the file upload will be
        self.chunk_size = chunk_size
        
        # Initialize the total number of chunks as None, which will be calculated based on the file size and chunk size
        self.total_chunks = math.ceil(file_size / chunk_size)
        
        # Initialize an empty list to hold parts metadata, containing dictionaries with PartNumber and ETag for each uploaded chunk
        self.parts:list[str,dict] = parts  # List of dictionaries: [{'PartNumber': xxx, 'ETag': xxx}]

        self.FSMs_state=S3LargeUploadingFSMsController.S3LargeUploadingState.States.idle

    def is_recieved(self):
        return len(self.parts)==self.total_chunks

    # do not random gen id, for to identify file
    @staticmethod
    def gen_id(file_name,file_size,file_hash):
        return f'{file_name},{file_size},{file_hash}'
    
    def get_id(self):
        return S3LargeUploadingModel.gen_id(
                    self.file_name,self.file_size,self.file_hash)
    
    def to_dict(self):
        return self.__dict__
    
    def from_dict(self,data):
        for k in self.__dict__.keys():
            setattr(self,k,data[k])
        return self
    
class S3LargeUploadingFSMsController:
    
    class S3LargeUploadingState:
        class States:
            idle = 'idle'
            recieving = 'recieving'
            recieved = 'recieved'
            recieve_failure = 'recieve_failure'
            merged = 'merged'
            merge_failure = 'merge_failure'

        _transitions = {
            States.idle:             [States.recieving],
            States.recieving:        [States.recieved, States.recieve_failure, States.idle],
            States.recieve_failure:  [States.recieving], # retry recieving
            States.recieved:         [States.merged, States.merge_failure],
            States.merge_failure:    [States.merged],
            States.merged:           [], # end of task life
            
        }
        _states = list(_transitions.keys())
        
    def __init__(self,model:S3LargeUploadingModel) -> None:
        self.model = model
    
    # public
    @staticmethod
    def new_or_find_file_uploading(file_name,file_size,file_hash):
        # find the file is recorded
        id = S3LargeUploadingModel.gen_id(file_name,file_size,file_hash)
        model_data = DBStorage().get(id)
        if model_data: return S3LargeUploadingFSMsController(
                                    S3LargeUploadingModel(
                                        ).from_dict(model_data))

        # new request for file uploading, hard operation
        response = get_s3_client().create_multipart_upload(Bucket=BUCKET_NAME, Key=file_name)
        upload_id = response['UploadId']    
        model = S3LargeUploadingModel(file_name,file_size,file_hash,upload_id)
        return S3LargeUploadingFSMsController(model).save_model()
    
    def save_model(self):
        DBStorage().set(self.model.get_id(),self.model.to_dict())
        return self
        
    def delete_model(self):
        return DBStorage().delete(self.model.get_id())
    
    def current_state(self):
        return self.model.FSMs_state    

    def set_state(self,state):
        self.model.FSMs_state=state
        self.save_model()

    ################################# privates will use in it self or FSMs part
        
    def _merge_chunk(self):        
        # Complete the multipart upload
        response = get_s3_client().complete_multipart_upload(
            Bucket=BUCKET_NAME,
            Key=self.model.file_name,
            UploadId=self.model.upload_id,
            MultipartUpload={'Parts': self.model.parts}
        )
        print(f"File {self.model.file_name} has been uploaded and merged on S3 successfully.")

    def _append_chunk(self,chunk_data):
        this_chunk_No = len(self.model.parts) + 1

        # Upload the chunk as a part of the multipart upload
        part_response = get_s3_client().upload_part(
            Bucket=BUCKET_NAME,
            Key=self.model.file_name,
            PartNumber=this_chunk_No,
            UploadId=self.model.upload_id,
            Body=chunk_data
        )

        # Store part information to complete the multipart upload later
        self.model.parts.append({
            'PartNumber': this_chunk_No,
            'ETag': part_response['ETag']
        })
        self.save_model()

    ################## public FSMs part    
    def validate_transition(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self:S3LargeUploadingFSMsController=self
            valid_transitions = self.S3LargeUploadingState._transitions[self.current_state()]
            target_transition = func.__name__.replace('to_','')
            if target_transition not in valid_transitions:            
                raise ValueError(f"Invalid transition from [{self.current_state()}] -> [{target_transition}]")
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                print(f'[{self.__class__.__name__}]: {e}')
        return wrapper
    
    @validate_transition
    def to_idle(self):
        self.set_state(S3LargeUploadingState.States.idle)
        
    @validate_transition
    def to_recieving(self,chunk_data):
        # start recieving flows
        if chunk_data:
            self.set_state(S3LargeUploadingState.States.recieving)
            try:
                if not self.model.is_recieved():
                    self._append_chunk(chunk_data)
            except Exception as e:
                print(e)            
                self.to_recieve_failure()

    @validate_transition
    def to_recieve_failure(self):
        self.set_state(S3LargeUploadingState.States.recieve_failure)

    @validate_transition
    def to_recieved(self):
        if self.model.is_recieved():
            self.set_state(S3LargeUploadingState.States.recieved)
        else:
            self.to_idle()
            
    @validate_transition
    def to_merged(self):
        try:
            self._merge_chunk()
            self.set_state(S3LargeUploadingState.States.merged)
        except Exception as e:
            print(e)            
            self.to_merge_failure()

    @validate_transition
    def to_merge_failure(self):
        self.set_state(S3LargeUploadingState.States.merge_failure)
    
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
    
    def next_action(self,target_state):
        path = self.find_path(self.S3LargeUploadingState._transitions,
                              self.S3LargeUploadingState._states, target_state)
        if len(path)<=1: return None
        return path[1]

```


```python
# server by lib of fastapi
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()

@app.get("/")
def serve_html():
    return FileResponse("index.html")

def main_loop(file_name, file_size, file_hash, file:UploadFile=None):
    STATES = S3LargeUploadingState.States
    try:
        # Initialize the controller and determine the current state and next action
        controller = S3LargeUploadingFSMsController.new_or_find_file_uploading(
                        file_name, file_size, file_hash)
        chunk_data = file.file.read() if file else None # Read the chunk data
        current = controller.current_state()
        action = controller.next_action(target_state=STATES.merged)

        if current == STATES.merged and action is None:
            # If already merged and no further action needed, finish
            print({'message': f'Current: {current}, finish!'})
            # finish and delete the record in DB.
            controller.delete_model()
            return JSONResponse(content={'message': f'Current: {current}, finish!'})
        
        # Perform the next action based on the current state
        print(f'Current: {current}, try to_{action}')   
        if action == STATES.recieving:
            if chunk_data is not None:
                getattr(controller, f'to_{action}')(chunk_data)
        else:
            getattr(controller, f'to_{action}')()

        return JSONResponse(content={
            'data': controller.model.to_dict(),
            'message': f'Current: {current}, try to_{action}'
        })
        
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/start_upload/")
def start_upload(
    file_name: str = Form(...),
    file_size: int = Form(...),
    file_hash: str = Form(...)):
    return main_loop(file_name, file_size, file_hash)


@app.post("/upload_chunk/")
def upload_chunk(
    file: UploadFile = File(...),
    file_name: str = Form(...),
    file_size: int = Form(...),
    file_hash: str = Form(...)):
    return main_loop(file_name, file_size, file_hash, file)

```

Make sure you have Python and FastAPI installed. If you haven't installed FastAPI yet, run:

```bash
pip install fastapi[all] uvicorn
```

Run the server using `uvicorn` (the ASGI server used with FastAPI):

```bash
uvicorn <python source code >:app --reload
```

The source code consists of previous Python code blocks, which we can merge into one file.

This will start the FastAPI server on `http://127.0.0.1:8000`.

The server provides three endpoints:

1. **GET `/`**: Serves the HTML file (`index.html`). Make sure you have this file in the same directory as your server script.
   
2. **POST `/start_upload/`**: Initializes the upload process for a large file by recording metadata such as the file name, size, and hash.
   
3. **POST `/upload_chunk/`**: Handles uploading chunks of the file. Each chunk is processed and stored, and the state of the upload is managed.

The final step in our implementation is to develop the front-end `index.html`.

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chunked File Upload to S3</title>
</head>

<body>
    <div class="container">
        <input type="file" id="fileInput" />
        <progress id="progress" value="0" max="100"></progress>
    </div>
    <div id="status"></div>
    <div id="debugmsg" hidden></div>
    <script>
        var file_name = null;
        var file_size = null;
        var file_hash = null;
        var file_server_data = null;

        const requestForm = (file = null) => {
            const formData = new FormData();
            if (file) formData.append('file', file);
            formData.append('file_name', file_name);
            formData.append('file_size', file_size);
            formData.append('file_hash', file_hash);
            return formData;
        }

        document.getElementById('fileInput').addEventListener('change', function (event) {
            const file = event.target.files[0];
            if (!file) {
                return;
            }
            file_name = file.name;
            file_size = file.size;

            const chunkSize = 5 * 1024 * 1024; // 5MB chunks
            const chunks = Math.ceil(file.size / chunkSize);
            const progress = document.getElementById('progress');
            progress.value = 0;

            document.getElementById('status').innerText = 'Calculating SHA-256 Hash ...';

            calculateHash(file, chunkSize, chunks, progress).then(function (hashBuffer) {
                const hashArray = Array.from(new Uint8Array(hashBuffer));
                file_hash = hashArray.map(function (byte) {
                    return byte.toString(16).padStart(2, '0');
                }).join('');
                document.getElementById('status').innerText += 'end';
                document.getElementById('debugmsg').innerText += `${file_name} SHA-256 Hash: ${file_hash}\n`;
                document.getElementById('status').innerText = 'Uploading ...';
                startUpload().then(function (file_server_data) {
                    document.getElementById('debugmsg').innerText += JSON.stringify(file_server_data);
                    uploadChunk(file, file_server_data.chunk_size,
                        file_server_data.parts.length, file_server_data.total_chunks);
                });
            }).catch(function (error) {
                document.getElementById('debugmsg').innerText += `Error: ${error.message}\n`;
            });
        });

        function startUpload() {
            return new Promise(function (resolve, reject) {
                fetch('/start_upload/', {
                    method: 'POST',
                    body: requestForm()
                }).then(function (res) {
                    return res.json();
                }).then(function (data) {
                    resolve(data.data);
                }).catch(function (error) {
                    reject(error);
                });
            });
        }

        function uploadChunk(file, chunkSize, chunkNumber, totalChunks) {
            const progress = document.getElementById('progress');
            progress.value = (chunkNumber / totalChunks) * 100;
            if (chunkNumber >= totalChunks) {
                startUpload().then(function (file_server_data) {
                    document.getElementById('debugmsg').innerText += JSON.stringify(file_server_data) + '\n';
                    // file will be merged and record will be removed, undefined means end.
                    if (file_server_data !== undefined) {
                        uploadChunk(file, file_server_data.chunk_size, file_server_data.parts.length, file_server_data.total_chunks);
                    } else {
                        document.getElementById('status').innerText += 'end';
                    }
                });
                return;
            }
            const start = chunkNumber * chunkSize;
            const end = Math.min(start + chunkSize, file.size);
            const blob = file.slice(start, end);

            fetch('/upload_chunk/', {
                method: 'POST',
                body: requestForm(blob)
            }).then(function (res) {
                return res.json();
            }).then(function (data) {
                file_server_data = data.data;
                document.getElementById('debugmsg').innerText += JSON.stringify(file_server_data) + '\n';
                uploadChunk(file, file_server_data.chunk_size, file_server_data.parts.length, file_server_data.total_chunks);
            }).catch(function (error) {
                console.error('Error uploading chunk:', error);
                alert(`Failed to upload chunk ${chunkNumber + 1}. Please try again.`);
            });
        }

        function calculateHash(file, chunkSize, chunks, progress) {
            const crypto = window.crypto || window.msCrypto; // for IE 11
            const hashAlgorithm = 'SHA-256';

            return new Promise(function (resolve, reject) {
                var hashBuffer = new ArrayBuffer(0);
                function processChunk(i) {
                    if (i >= chunks) {
                        resolve(hashBuffer);
                        return;
                    }
                    const start = i * chunkSize;
                    const end = Math.min(start + chunkSize, file.size);
                    const chunk = file.slice(start, end);

                    chunk.arrayBuffer().then(function (chunkBuffer) {
                        crypto.subtle.digest(hashAlgorithm, new Uint8Array(chunkBuffer)).then(function (digest) {
                            hashBuffer = digest;
                            progress.value = ((i + 1) / chunks) * 100;
                            processChunk(i + 1);
                        }).catch(reject);
                    }).catch(reject);
                }
                processChunk(0);
            });
        }
    </script>
</body>

</html>
```

- **Key Features of This Resumable Implementation** :

   - **State Machine for Managing Upload States**:
      - A `S3LargeUploadingState` class implements a state machine to manage the different stages of the upload process. The states include `idle`, `receiving`, `received`, `receive_failure`, `merged`, and `merge_failure`. Transitions between these states are managed based on conditions and errors.
      - The state transition methods in `S3LargeUploadingState` are wrapped with a `validate_transition` decorator to validate transitions and handle exceptions. Invalid state transitions raise an error, and exceptions within a transition trigger specific failure states.

   - **Persistent Model Management with a Backend Database**:
      - The code leverages a `DBStorage` class (inherited from `MongoDBStorage`) for persisting the state of file uploads, such as file metadata and upload progress, enabling resumable uploads. This is crucial for handling large files that may require multiple sessions to complete the upload process.

      - The backend for managing storage can be easily replaced or extended, as demonstrated by the `DBStorage` class, which inherits from a more generic `MongoDBStorage`. This design allows for easy adaptation to different backend storage systems.

   - **Simplified API for External Use**:
      - The `S3LargeUploadingController` class provides a high-level API for interacting with the upload process, allowing external callers to trigger state transitions and manage uploads without needing to interact with lower-level details.

      - The `next_action` method in `S3LargeUploadingState` class finds the shortest path for transitioning from the current state to a **target** state, providing a clear mechanism for managing complex state transitions.

### Section 2: Video File Conversion Service
The previous example requires an AWS account, which can make it challenging to learn.
However, there's no need to worry if you find it difficult to understand.
In this section, we will introduce a simpler server-side service focused on large file conversion.
For example, many video sites use video thumbnails for previews, instead of displaying the entire large video file.

In this example, the server needs to track the state of a large video file conversion task to ensure a consistent workflow, even in case of unexpected interruptions. The task involves three key steps:

1. Reading chunks of the file, frame by frame and Resizing each frame.
2. Writing each resized frame into an output file.

To avoid restarting the task from the beginning after a crash, we need to manage its state effectively. The possible states and their transitions are illustrated in the following Python code:


```python
class VideoConversionState:
    class States:
        idle = 'idle'
        resize_stage = 'resize_stage'
        error = 'error'
        complete_mp4 = 'complete_mp4'

    _transitions = {
        States.idle:    [States.resize_stage],
        States.resize_stage:  [States.resize_stage,States.error,States.complete_mp4],
        States.error:   [States.idle],
        States.complete_mp4:[],

    }
    _states = list(_transitions.keys())
```

Let's consider this service MVC(FSMs)'s Model and basic Controller. And the Controller's states.


```python
"This model needs UUIDs to identify itself and related files."
"We also need to record the process to ensure the state can be restored."

from collections import deque
from functools import wraps
from typing import Callable
import uuid
import cv2
import os
import random
import numpy as np  # Assuming you are using OpenCV to work with videos

# easy to change back end ShelveStorage or MongoDBStorage( need mongoDB )
# Chapter 7. Section 0: Preparation
class DBStorage(ShelveStorage):
    pass

class VideoConversionModel:
    
    def __init__(self, uuid = None, filename=None, width_limit=320, fps_ratio=1/4, converted_count=-1, state=None):
        # conversion_task_uuid
        self.uuid = uuid
        self.filename = filename    
        self.filesize = self.get_filesize(filename)  # Placeholder for actual file size calculation

        if self.filesize <= 0:
            raise ValueError('File size must be greater than 0')
        
        cap = cv2.VideoCapture(filename)
        if not cap.isOpened(): raise RuntimeError(f"Failed to open video file: {filename}")
        
        # Get frame width and height, adjust width up to 320 for thumbnail
        ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH)/width_limit
        self.thumbnail_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/ratio)
        self.thumbnail_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)/ratio)
        self.thumbnail_fps_ratio = int(1/fps_ratio) # cap.get(cv2.CAP_PROP_FPS)*fps_ratio
        
        self.thumbnail_bin_path = f'{self.uuid}.thumbnail.{self.filename}.bin'
        self.thumbnail_mp4_path = f'thumbnail.{self.filename}'

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
    def from_dict(data:dict):
        model = VideoConversionModel(data['uuid'],data['filename'])
        for k,v in data.items():
            if hasattr(model,k):model.__dict__[k]=v

class VideoConversionFSMsController:
    
    class VideoConversionState:
        class States:
            idle = 'idle'
            resize_stage = 'resize_stage'
            error = 'error'
            complete_mp4 = 'complete_mp4'

        _transitions = {
            States.idle:    [States.resize_stage],
            States.resize_stage:  [States.resize_stage,States.error,States.complete_mp4],
            States.error:   [States.idle],
            States.complete_mp4:[],

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

        @handle_errors
        def to_resize_stage(self):
            self.set_state(VideoConversionFSMsController.VideoConversionState.States.resize_stage)
            try:
                while self.model.converted_count < self.model.total_count:

                    # Transition to reading state
                    ret, frame = self.controller.cap.read()
                    if not ret:
                        raise RuntimeError(f"can not read frame.")
                    
                    # skip images for small fps
                    if self.model.converted_count%self.model.thumbnail_fps_ratio==0:
                        # Transition to resizing state
                        frame = cv2.resize(frame, (self.model.thumbnail_width, self.model.thumbnail_height))
                        # Transition to writing state
                        with open(self.model.thumbnail_bin_path,'ab') as f: f.write(frame.tobytes())
                    
                    self.model.converted_count += 1
                    self.controller.save_model()
                        
            except Exception as e:
                self.to_error(f"{self.model.state} error [{self.model.filename}]: {e}")

        @handle_errors
        def to_error(self,e):
            self.set_state(VideoConversionFSMsController.VideoConversionState.States.error)
            print(e)

        @handle_errors
        def to_complete_mp4(self):
            try:
                if self.model.converted_count >= self.model.total_count:
                    # convert bin file into mp4
                    out = cv2.VideoWriter(
                        self.model.thumbnail_mp4_path,
                        cv2.VideoWriter_fourcc(*'mp4v'),  # Codec for mp4 files
                        self.controller.cap.get(cv2.CAP_PROP_FPS)/self.model.thumbnail_fps_ratio,
                        # self.model.thumbnail_fps_ratio,
                        (self.model.thumbnail_width, self.model.thumbnail_height)
                    )
                    with open(self.model.thumbnail_bin_path, 'rb') as f: raw_data = f.read()
                    # Read the frames data
                    frames = np.frombuffer(raw_data, dtype=np.uint8).reshape(
                        (-1, self.model.thumbnail_height, self.model.thumbnail_width, 3))
                    for frame in frames:
                        out.write(frame)
                    out.release()

                    os.remove(self.model.thumbnail_bin_path)
                    self.set_state(VideoConversionFSMsController.VideoConversionState.States.complete_mp4)
                else:
                    self.to_resize_stage()
            except Exception as e:
                self.to_error(f"{self.model.state} error [{self.model.filename}]: {e}")

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
        
        def resume_state(self,target_state, max_attempts=100,simulate_error=False):
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
                
                if simulate_error and random.random()>0.3:
                    print('simulate some error!')
                    continue
                
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
    def new_video_conversion(filename, width_limit=320, fps_ratio=1/4):
        # new request for file conversion, hard operation
        model = VideoConversionModel(uuid.uuid4(),filename,width_limit,fps_ratio)
        return VideoConversionFSMsController(model).save_model()
    
    @staticmethod
    def find_video_conversion(uuid):
        model = DBStorage().get(uuid)
        if model is None:raise ValueError(f'no such data of {uuid}')
        return VideoConversionFSMsController(VideoConversionModel.from_dict(model))
    
    def start_conversion(self,simulate_error=False):
        state:VideoConversionFSMsController.VideoConversionState = self.state
        state.resume_state(VideoConversionFSMsController.VideoConversionState.States.complete_mp4,simulate_error=simulate_error)

```


```python
print('```')
conversion = VideoConversionFSMsController.new_video_conversion('test.mp4',width_limit=320,fps_ratio=1/4)
print(f'start conversion of {conversion.model.uuid}')
conversion.start_conversion(simulate_error=True)
print('```')
```

    ```
    Set target state: complete_mp4 ( current is idle)
    Current: idle, try to_resize_stage
    Current: resize_stage, try to_complete_mp4
    Success to target state: complete_mp4
    ```
    





### Conclusion
...

### Additional Notes
...

---


## Chapter 8: Testing Resumable Systems

### Introduction
...

### Conclusion
...

### Additional Notes
...

---

## Chapter 9: Resumability in Task Systems ( Distributed )

### Introduction
...
### Section 0: Preparation
To design a task states

#### Updated States
1. **Created**:  
   - The initial state of a task after it is created but not yet acted upon.
2. **Assigned**:  
   - The task is assigned to a user, team, or system for action.  
3. **In Progress**:  
   - Work on the task has started.
4. **Paused**:  
   - The task is temporarily on hold but may resume later.
5. **Error**:
   - An error occurred (e.g., camera overheating). In this state, the error is analyzed to decide the next action.
6. **Completed**:  
   - The task has been successfully finished.
7. **Canceled**:  
   - The task has been terminated without completion.
8. **Failed**:  
   - The task could not be completed due to errors, issues, or other reasons.
9. **Closed**:  
   - The task is finalized and no further changes can be made.


#### Transitions
1. **Created → Assigned**:
   - The task to start the task is assigned to the control system.

2. **Assigned → In Progress**:
   - Attempting to start the task.

3. **In Progress → Error**:
   - The task encounters an error (e.g., camera overheating).

4. **Error → Paused**:
   - If the error is recoverable (e.g., camera overheating), the task transitions to `Paused` for a retry.

5. **Error → Failed**:
   - If the error is critical (e.g., hardware failure), the task transitions to `Failed`.

6. **Paused → Assigned**:
   - After a recovery period, the task retries.

7. **In Progress → Completed**:
   - The task starts successfully, and the task completes.

8. **Any State → Canceled**:
   - The task is manually or automatically canceled, halting retries.


#### FSM Diagram
```plaintext
[Created] --> [Assigned] --> [In Progress] --> [Completed]
                                |
                                v
                             [Error]
                              /   \
                 (Recoverable)   (Critical)
                    |               |
                    v               v
               [Paused]         [Failed]
                    |
          (Recovery Timer)
                    |
                    v
                [Assigned]
```


```python
from functools import wraps
from typing import Callable
from collections import deque
import random
import time

class TaskStateMachine:
    class States:
        created = 'created'
        assigned = 'assigned'
        in_progress = 'in_progress'
        error = 'error'
        paused = 'paused'
        failed = 'failed'
        completed = 'completed'
        canceled = 'canceled'

    _transitions = {
        States.created:      [States.assigned],
        States.assigned:     [States.in_progress, States.canceled],
        States.in_progress:  [States.error, States.completed, States.canceled],
        States.error:        [States.paused, States.failed, States.canceled],
        States.paused:       [States.assigned, States.canceled],
        States.failed:       [],  # End of task life
        States.completed:    [],  # End of task life
        States.canceled:     [],  # End of task life
    }

    _states = list(_transitions.keys())

    def __init__(self, state):
        if state not in self._states:
            raise ValueError(f"Invalid initial state: {state}")
        self._state = state

    def set_state(self,state):
        self._state=state
        
    def task_start(self):
        # Simulate task start logic
        return random.choice([True,True,True, False])  # Random success/failure for demonstration

    def simulate_error(self):
        # Simulate error detection
        return random.choice(["overheat", "hardware_failure",None])  # Random error type

    def wait_for_cool_down(self):
        print("wait for cool down ...")
        time.sleep(2)  # Simulate cooling down period

    def handle_errors(func:Callable):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            valid_transitions = self._transitions[self._state]
            target_transition = func.__name__.replace('to_','')
            if target_transition not in valid_transitions:            
                raise ValueError(f"Invalid transition from [{self._state}] -> [{target_transition}]")
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                print(f'[{self.__class__.__name__}]: {e}')
        return wrapper

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
    
    def resume_state(self,target_state, max_attempts=10):
        print(f'Set target state: {target_state} ( current is {self._state})')
        def next_action(task,target_state):
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

    # Transition methods
    @handle_errors
    def to_assigned(self):
        self.set_state(self.States.assigned)

    @handle_errors
    def to_in_progress(self):
        if self.task_start():
            self.set_state(self.States.in_progress)
        else:
            print('Can not start and remain state of assigned')
            return
                
        error = self.simulate_error()
        if error:
            self.to_error(error)

    @handle_errors
    def to_error(self,error_type):
        self.set_state(self.States.error)

        print(f"Error detected: {error_type}")
        if error_type == "hardware_failure":
            print("hardware critical failure!")
            self.to_failed()

    @handle_errors
    def to_paused(self):
        self.set_state(self.States.paused)
        self.wait_for_cool_down()

    @handle_errors
    def to_failed(self):
        self.set_state(self.States.failed)

    @handle_errors
    def to_completed(self):
        error_type = self.simulate_error()
        if error_type:
            self.to_error(error_type)
        else:
            self.set_state(self.States.completed)

    @handle_errors
    def to_canceled(self):
        self.set_state(self.States.canceled)

# Test cases for the TaskStateMachine
def test_task_state_machine():
    # Initialize the FSM in the 'created' state
    fsm = TaskStateMachine(state=TaskStateMachine.States.created)

    print("\n########### Test Case 1: Transition from 'created' to 'completed'")
    try:
        fsm.resume_state(TaskStateMachine.States.completed)
    except Exception as e:
        print(f"Test failed: {e}")

    print("\n########### Test Case 2: Transition from 'created' to 'failed' when task_start")
    fsm = TaskStateMachine(state=TaskStateMachine.States.created)
    try:
        # Force task_start to simulate failure
        def always_fail():
            return False
        fsm.task_start = always_fail  # Override method
        fsm.resume_state(TaskStateMachine.States.failed)
    except Exception as e:
        print(f"Test failed: {e}")

    print("\n########### Test Case 3: Transition from 'created' to 'paused' (recoverable error)")
    fsm = TaskStateMachine(state=TaskStateMachine.States.created)
    try:
        # Force simulate_error to simulate overheating
        def simulate_overheat():
            return "overheat"
        fsm.simulate_error = simulate_overheat  # Override method
        fsm.resume_state(TaskStateMachine.States.paused)
    except Exception as e:
        print(f"Test failed: {e}")

    print("\n########### Test Case 4: Transition from 'created' to 'canceled'")
    fsm = TaskStateMachine(state=TaskStateMachine.States.created)
    try:
        fsm.resume_state(TaskStateMachine.States.canceled)
    except Exception as e:
        print(f"Test failed: {e}")

# Run the tests
test_task_state_machine()
```

    
    ########### Test Case 1: Transition from 'created' to 'completed'
    Set target state: completed ( current is created)
    Current: created, try to_assigned
    Current: assigned, try to_in_progress
    Can not start and remain state of assigned
    Current: assigned, try to_in_progress
    Can not start and remain state of assigned
    Current: assigned, try to_in_progress
    Error detected: hardware_failure
    hardware critical failure!
    Test failed: no next acion! unreachable!
    
    ########### Test Case 2: Transition from 'created' to 'failed' when task_start
    Set target state: failed ( current is created)
    Current: created, try to_assigned
    Current: assigned, try to_in_progress
    Can not start and remain state of assigned
    Current: assigned, try to_in_progress
    Can not start and remain state of assigned
    Current: assigned, try to_in_progress
    Can not start and remain state of assigned
    Current: assigned, try to_in_progress
    Can not start and remain state of assigned
    Current: assigned, try to_in_progress
    Can not start and remain state of assigned
    Current: assigned, try to_in_progress
    Can not start and remain state of assigned
    Current: assigned, try to_in_progress
    Can not start and remain state of assigned
    Current: assigned, try to_in_progress
    Can not start and remain state of assigned
    Current: assigned, try to_in_progress
    Can not start and remain state of assigned
    Current: assigned, try to_in_progress
    Can not start and remain state of assigned
    Test failed: over max_attempts!
    
    ########### Test Case 3: Transition from 'created' to 'paused' (recoverable error)
    Set target state: paused ( current is created)
    Current: created, try to_assigned
    Current: assigned, try to_in_progress
    Can not start and remain state of assigned
    Current: assigned, try to_in_progress
    Error detected: overheat
    Current: error, try to_paused
    wait for cool down ...
    Success to target state: paused
    
    ########### Test Case 4: Transition from 'created' to 'canceled'
    Set target state: canceled ( current is created)
    Current: created, try to_assigned
    Current: assigned, try to_canceled
    Success to target state: canceled
    


#### Key Enhancements
1. **Error Evaluation**:
   - The `Error` state evaluates the severity of the issue and routes the task accordingly.
   - Example criteria:
     - Overheating: Recoverable, transition to `Paused`.
     - Hardware failure: Critical, transition to `Failed`.

2. **Retry Handling**:
   - `Paused → Assigned` loop ensures retries after recoverable errors.
   - Include a delay in the `Paused` state for recovery.

3. **Task Termination**:
   - Transition to `Failed` for unrecoverable errors, stopping the task.

4. **Manual Cancellation**:
   - A `Canceled` transition is available for external termination of the task.

This enhanced FSM design adds robustness by introducing error analysis and dynamic decision-making.
### Conclusion
...

### Additional Notes
...

---



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


