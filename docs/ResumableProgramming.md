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



```
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



```
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



```
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



```
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


```
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



```

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


```
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


```
class MyClass:
    # Attributes and methods go here
    pass

my_object = MyClass()
```


- **Defining Attributes and Methods** :
Attributes in a Python class are defined within the `__init__` method, which is the constructor method that is automatically called when a new instance is created. Methods are functions defined within the class body that operate on instances of the class.



```
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


```
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



```
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


```
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



```
class Bird(Animal):
    def __init__(self, name, can_fly=True):
        super().__init__(name)
        self.can_fly = can_fly
```

- **Special Methods and Operator Overloading** :
Python classes have special methods, also known as "dunder" methods (double underscore methods), like `__init__`, `__str__`, `__repr__`, and `__eq__`, which can be used to overload operators and provide custom behavior for common operations.



```

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


```
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


```
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


```
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


```
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


```
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


```
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


```
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


```
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


```
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


```
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


```
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


```
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


```
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



```
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


```
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


```
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


```
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


This example involves very simple sequential tasks, meaning its states and transitions are minimal. However, in many cases, our system has many more states and transitions, making it difficult to do **Resumability** in a single function.

As the following example shows, we will need a **solver** to auto **Resume**.


```
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



```
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


```
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


```
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
print('Following is possible transisitions table(dict).')
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



```
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
print('With a solver we will easy to find path from a state to certain goal.')
print('```')
print(f"Path from {class_str_map[start_state]} to {class_str_map[end_state]} : "+' -> '.join([class_str_map[p] for p in path]))
print('```')
```

    ```
    Path from FailureState to CommunicationState : FailureState -> InitiationState -> WaitingState -> ConnectionEstablishedState -> CommunicationState
    ```



```
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


```
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



```
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
print('Test 1 :')
controller = UserAuthFSMsController(
                User(username="admin", password="1234"),
                View()).login()  # Should log in successfully
controller.logout()

print('Test 2 :')
controller = UserAuthFSMsController(
                User(username="admin", password="wrongpassword"),
                View()).login()   # Should show login failed
controller.logout() # Should warning that cannot logout without login at first.

print('Test 3 :')
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


```
# this is a server code for starting independent.
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


```
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


```
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


```
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


```
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


```
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


```
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


```
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


```
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



```
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


```
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


```
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


```
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


```
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


    def __init__(self,model:VideoConversionModel) -> None:
        self.model = model
        self.FSMs_STATES = VideoConversionFSMsController.VideoConversionState.States
        self.set_state(self.FSMs_STATES.idle)
        
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
        # auto shift to complete_mp4 state by "resume"
        self.resume_state(self.FSMs_STATES.complete_mp4,simulate_error=simulate_error)

    def set_state(self,state):
        self.state=state
        self.model.state=state
        self.save_model()
    
    def handle_errors(func:Callable):
        @wraps(func)
        def wrapper(self:'VideoConversionFSMsController',
                    *args, **kwargs):
            valid_transitions = VideoConversionFSMsController.VideoConversionState._transitions[self.state]
            target_transition = func.__name__.replace('to_','')
            if target_transition not in valid_transitions:            
                raise ValueError(f"Invalid transition from [{self.state}] -> [{target_transition}]")
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                print(f'[{self.__class__.__name__}]: {e}')
        return wrapper

    @handle_errors
    def to_idle(self):
        self.set_state(self.FSMs_STATES.idle)

    @handle_errors
    def to_resize_stage(self):
        self.set_state(self.FSMs_STATES.resize_stage)
        try:
            while self.model.converted_count < self.model.total_count:

                # Transition to reading state
                ret, frame = self.cap.read()
                if not ret:
                    raise RuntimeError(f"can not read frame.")
                
                # skip images for small fps
                if self.model.converted_count%self.model.thumbnail_fps_ratio==0:
                    # Transition to resizing state
                    frame = cv2.resize(frame, (self.model.thumbnail_width, self.model.thumbnail_height))
                    # Transition to writing state
                    with open(self.model.thumbnail_bin_path,'ab') as f: f.write(frame.tobytes())
                
                self.model.converted_count += 1
                self.save_model()
                    
        except Exception as e:
            self.to_error(f"{self.model.state} error [{self.model.filename}]: {e}")

    @handle_errors
    def to_error(self,e):
        self.set_state(self.FSMs_STATES.error)
        print(e)

    @handle_errors
    def to_complete_mp4(self):
        try:
            if self.model.converted_count >= self.model.total_count:
                # convert bin file into mp4
                out = cv2.VideoWriter(
                    self.model.thumbnail_mp4_path,
                    cv2.VideoWriter_fourcc(*'mp4v'),  # Codec for mp4 files
                    self.cap.get(cv2.CAP_PROP_FPS)/self.model.thumbnail_fps_ratio,
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
                self.set_state(self.FSMs_STATES.complete_mp4)
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
        print(f'Set target state: {target_state} ( current is {self.state})')
        def next_action(task:VideoConversionFSMsController.VideoConversionState.States
                        ,target_state):
            path = self.find_path(VideoConversionFSMsController.VideoConversionState._transitions, task, target_state)
            if len(path)<=1: return None
            return path[1]
            
        while self.state != target_state:
            cls = next_action(self.state,target_state)
            if cls is None:raise ValueError('no next acion! unreachable!')
            if max_attempts<0:raise ValueError(f'over max_attempts!')
            print(f'Current: {self.state}, try to_{cls}')
            
            if simulate_error and random.random()>0.3:
                print('simulate some error!')
                continue
            
            getattr(self,f'to_{cls}')()
            max_attempts -= 1
        print(f'Success to target state: {self.state}')
       
```


```
print('```')
conversion = VideoConversionFSMsController.new_video_conversion('test.mp4',width_limit=320,fps_ratio=1/4)
print(f'start conversion of {conversion.model.uuid}')
conversion.start_conversion(simulate_error=True)
print('```')
```

    ```
    start conversion of 1bf370b5-4cd4-408f-bee5-7d9734c51fab
    Set target state: complete_mp4 ( current is idle)
    Current: idle, try to_resize_stage
    simulate some error!
    Current: idle, try to_resize_stage
    Current: resize_stage, try to_complete_mp4
    simulate some error!
    Current: resize_stage, try to_complete_mp4
    simulate some error!
    Current: resize_stage, try to_complete_mp4
    Success to target state: complete_mp4
    ```


### Section 3: AI Object Detection and Segmentation Service (SAM 3)

Another practical application of resumable programming is an AI object detection and segmentation service.

In recent years, foundation models for computer vision have made it possible to identify objects using natural-language prompts instead of relying only on a fixed collection of predefined object classes.

In this example, we use **Segment Anything Model 3 (SAM 3)**.

SAM 3 can detect and segment objects using prompts such as:

```text
person
red car
yellow school bus
dog
a person wearing a helmet
```

Instead of returning only a bounding box, SAM 3 can also return a segmentation mask describing the precise pixels belonging to each detected object.

This makes it useful for applications such as:

* video analysis,
* automatic video editing,
* surveillance analysis,
* autonomous systems,
* scientific image processing,
* robotics,
* media processing,
* and dataset generation.

However, processing a large video with an AI model can be expensive.

For example, consider a video containing 500,000 frames.

If our application successfully processes 350,000 frames and then the machine unexpectedly restarts, processing the entire video again would waste a significant amount of GPU computation.

Therefore, object segmentation is another good example of a task that should be **resumable**.

Instead of considering the entire video as one large operation, we divide it into many smaller operations:


Before designing the SAM 3 inference states, we first need to define how input data is provided to the task.

A SAM 3 task may receive different kinds of sources.

For example:

```text
Source
  |
  +-- Video
  |     |
  |     +-- frame 0
  |     +-- frame 1
  |     +-- frame 2
  |     +-- ...
  |
  +-- Image List
        |
        +-- image_001.jpg
        +-- image_002.jpg
        +-- image_003.jpg
        +-- ...
```

From SAM 3's point of view, both sources eventually produce the same thing:

```text
an image/frame
```

Therefore, the SAM 3 processor should not need to know whether the image came from:

```text
a video
```

or:

```text
a directory/list of images
```

Instead, a separate **Source Reader** is responsible for converting different source types into a common stream of frames.

The architecture becomes:

```text
                  Persistent Task
                        |
                        v
                +---------------+
                | Source Reader |
                +-------+-------+
                        |
                    Frame Data
                        |
                        v
                +---------------+
                |     SAM 3     |
                +-------+-------+
                        |
                        v
                +---------------+
                | Save Result   |
                +---------------+
```

This separation is important because source errors and SAM errors are fundamentally different.

For example:

```text
Cannot open video
```

is a source error.

```text
JPEG file is corrupted
```

is a source error.

```text
Cannot decode frame 1532
```

is a source error.

But:

```text
CUDA out of memory
```

is a SAM execution error.

And:

```text
SAM model inference failed
```

is also a SAM execution error.

These failures should not be represented by the same state.


```
from __future__ import annotations
"""
smart_sam3_separated_demo.py

Goal
====
Keep four responsibilities separate:

1. SAM3Segmentation / SmartSAM3Segmentation
   - Base class is ordinary usable SAM3 code.
   - Smart subclass adds @action + recovery through inheritance/super().
   - No state/current_cnt/retry/error history.

2. SAM3ProgressStore        <-- TASK AUTHOR OWNS THIS
   - Knows what "progress" means for SAM3.
   - Here it stores next_frame/completed.
   - SmartEngine never reads or writes it.

3. SmartEngine              <-- GENERIC
   - Wraps @action methods.
   - Catches ordinary exceptions.
   - Discovers recovery actions.
   - Applies guards.
   - Ranks by declared cost + learned action memory.
   - Uses softmax/random exploration.
   - Retries the original failed action.
   - Replans after another failure.

4. ActionRecorder / ActionMemory  <-- GENERIC PLUG-INS
   - Recorder observes engine events only.
   - Memory learns which recovery choices work.
   - Neither one knows SAM3 progress semantics.

Run:
    pip install pydantic
    python smart_sam3_separated_demo.py --reset

Hard-crash simulation:
    python smart_sam3_separated_demo.py --reset --hard-crash-rate 0.08
"""
import argparse
import contextvars
import hashlib
import json
import math
import random
import time
import uuid
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Literal, Protocol
from pydantic import BaseModel, PrivateAttr

# --- Generic utilities -------------------------------------------------------
def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def json_hash(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, ensure_ascii=False, default=repr, separators=(',', ':')).encode('utf-8')
    return hashlib.sha256(raw).hexdigest()

def short(value: Any, limit: int=180) -> str:
    text = repr(value)
    return text if len(text) <= limit else text[:limit - 3] + '...'

class JSONFile:
    """Tiny atomic JSON helper used by demo plug-ins."""

    def __init__(self, path: str | Path):
        self.path = Path(path)

    def read(self, default: Any) -> Any:
        if not self.path.exists():
            return default
        with self.path.open('r', encoding='utf-8') as f:
            return json.load(f)

    def write(self, data: Any) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temp = self.path.with_suffix(self.path.suffix + '.tmp')
        with temp.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, sort_keys=True)
            f.flush()
        temp.replace(self.path)

# --- Simulated failures ------------------------------------------------------
class FakeGPUError(RuntimeError):
    pass

class SimulatedHardCrash(BaseException):
    """
    BaseException deliberately bypasses SmartEngine's Exception handler.
    This imitates process death / kill / native crash.
    """
    pass

# --- Generic action metadata -------------------------------------------------
@dataclass(frozen=True)
class ActionSpec:
    name: str
    raw: Callable[..., Any]
    cost: float = 1.0
    recovery: bool = False
    guard: str | Callable[[Any, 'FailureContext'], bool] | None = None
    prior_success: float = 0.5

def action(
    *, cost: float = 1.0, recovery: bool = False,
    guard: str | Callable[[Any, "FailureContext"], bool] | None = None,
    prior_success: float = 0.5,
):
    """
    Decorate an ordinary method.

    If no SmartEngine is active:
        method behaves normally.

    If SmartEngine is active:
        engine.invoke(...) wraps the call.
    """

    def decorate(func: Callable[..., Any]):
        spec = ActionSpec(
            func.__name__, func, float(cost), recovery, guard, float(prior_success)
        )

        def wrapper(self, *args, **kwargs):
            engine = SmartEngine.current()
            if engine is None:
                return func(self, *args, **kwargs)
            return engine.invoke(obj=self, spec=spec, args=args, kwargs=kwargs, allow_recovery=not spec.recovery)
        wrapper.__name__ = func.__name__
        wrapper.__qualname__ = func.__qualname__
        wrapper.__doc__ = func.__doc__
        wrapper.__wrapped__ = func
        wrapper.__action_spec__ = spec
        return wrapper
    return decorate

# --- Engine events / recorder plug-ins --------------------------------------
@dataclass(frozen=True)
class ActionEvent:
    event_id: str
    task_key: str
    task_type: str
    action: str
    recovery: bool
    phase: Literal['started', 'succeeded', 'failed', 'recovery_chosen']
    timestamp: str
    parent_event_id: str | None = None
    error_type: str | None = None
    error_message: str | None = None
    details: dict[str, Any] | None = None

class ActionRecorder(Protocol):
    """
    Generic observer interface.

    IMPORTANT:
    This interface says nothing about:
        frame numbers
        upload chunks
        DB primary keys
        workflow completion
        checkpoints

    It only observes engine/action facts.
    """

    def record(self, event: ActionEvent) -> None:
        ...

class NullActionRecorder:

    def record(self, event: ActionEvent) -> None:
        pass

class ConsoleActionRecorder:

    def record(self, event: ActionEvent) -> None:
        if event.phase == 'started':
            return
        print(f'[REC   ] {event.phase:15s} {event.action}')

class JSONActionRecorder:
    """
    Generic append-only-ish event recorder.

    It records engine events only. It does NOT store SAM3 progress.
    """

    def __init__(self, path: str | Path):
        self.file = JSONFile(path)

    def record(self, event: ActionEvent) -> None:
        data = self.file.read({'events': []})
        data['events'].append(asdict(event))
        self.file.write(data)

class MultiRecorder:

    def __init__(self, *recorders: ActionRecorder):
        self.recorders = recorders

    def record(self, event: ActionEvent) -> None:
        for recorder in self.recorders:
            recorder.record(event)

# --- Failure context ---------------------------------------------------------
@dataclass(frozen=True)
class FailureContext:
    failed_action: str
    error_type: str
    error_message: str
    features: dict[str, Any]
    recovery_round: int = 0
ContextProvider = Callable[[Any, ActionSpec, Exception, Any], dict[str, Any]]

def default_context_provider(obj: Any, failed_spec: ActionSpec, error: Exception, runtime: Any) -> dict[str, Any]:
    return {}

# --- Learned recovery memory -------------------------------------------------
@dataclass
class MemoryStats:
    attempts: int = 0
    successes: int = 0
    total_actual_cost: float = 0.0

class ActionMemory(Protocol):

    def success_probability(self, context: FailureContext, action_name: str, prior_success: float) -> float:
        ...

    def learned_cost(self, context: FailureContext, action_name: str) -> float | None:
        ...

    def update(self, context: FailureContext, action_name: str, *, success: bool, actual_cost: float) -> None:
        ...

class InMemoryActionMemory:

    def __init__(self, prior_strength: float=2.0):
        self.prior_strength = prior_strength
        self.stats: dict[str, MemoryStats] = {}

    @staticmethod
    def _context_key(context: FailureContext) -> str:
        return json_hash({
            "failed_action": context.failed_action, "error_type": context.error_type,
            "features": context.features,
        })

    def _key(self, context: FailureContext, action_name: str) -> str:
        return f'{self._context_key(context)}::{action_name}'

    def _stats(self, context: FailureContext, action_name: str, *, create: bool=False) -> MemoryStats:
        key = self._key(context, action_name)
        if create:
            return self.stats.setdefault(key, MemoryStats())
        return self.stats.get(key, MemoryStats())

    def success_probability(self, context: FailureContext, action_name: str, prior_success: float) -> float:
        stats = self._stats(context, action_name)
        return (stats.successes + self.prior_strength * prior_success) / (stats.attempts + self.prior_strength)

    def learned_cost(self, context: FailureContext, action_name: str) -> float | None:
        stats = self._stats(context, action_name)
        if not stats.attempts:
            return None
        return stats.total_actual_cost / stats.attempts

    def update(self, context: FailureContext, action_name: str, *, success: bool, actual_cost: float) -> None:
        stats = self._stats(context, action_name, create=True)
        stats.attempts += 1
        stats.successes += int(success)
        stats.total_actual_cost += actual_cost

class JSONActionMemory(InMemoryActionMemory):
    """
    Same generic learning logic, persisted to JSON.

    Still knows nothing about SAM3 progress.
    """

    def __init__(self, path: str | Path, prior_strength: float=2.0):
        self.file = JSONFile(path)
        super().__init__(prior_strength=prior_strength)
        self._load()

    def _load(self) -> None:
        data = self.file.read({'stats': {}})
        self.stats = {key: MemoryStats(**raw) for key, raw in data['stats'].items()}

    def _save(self) -> None:
        self.file.write({'stats': {key: asdict(stats) for key, stats in self.stats.items()}})

    def update(self, context: FailureContext, action_name: str, *, success: bool, actual_cost: float) -> None:
        super().update(context, action_name, success=success, actual_cost=actual_cost)
        self._save()

    def pretty_print(self) -> None:
        print('\n=== GENERIC RECOVERY MEMORY ===')
        if not self.stats:
            print('(empty)')
            return
        for key, stats in sorted(self.stats.items()):
            rate = stats.successes / stats.attempts if stats.attempts else 0.0
            print(f'{key[-46:]:46s} attempts={stats.attempts:3d} successes={stats.successes:3d} rate={rate:.3f}')

# --- Generic smart recovery engine ------------------------------------------
@dataclass
class RecoveryCandidate:
    spec: ActionSpec
    p_success: float
    expected_cost: float
    selection_probability: float = 0.0
_CURRENT_ENGINE: contextvars.ContextVar['SmartEngine | None'] = contextvars.ContextVar('smart_engine', default=None)

class SmartEngine:
    """
    Generic adaptive recovery engine.

    This class deliberately does NOT contain:
        run store
        checkpoint
        frame index
        iterator resume
        task completion
        upload chunk progress
        DB cursor progress

    Task-specific progress belongs outside.
    """

    def __init__(
        self, *, task_key: str, runtime: Any = None,
        recorder: ActionRecorder | None = None, memory: ActionMemory | None = None,
        context_provider: ContextProvider | None = None, temperature: float = 1.5,
        max_recovery_attempts: int = 10, random_seed: int | None = None,
    ):
        self.task_key = task_key
        self.runtime = runtime
        self.recorder = recorder if recorder is not None else NullActionRecorder()
        self.memory = memory if memory is not None else InMemoryActionMemory()
        self.context_provider = context_provider if context_provider is not None else default_context_provider
        self.temperature = max(float(temperature), 1e-06)
        self.max_recovery_attempts = int(max_recovery_attempts)
        self.random = random.Random(random_seed)
        self._token = None

    @classmethod
    def current(cls) -> 'SmartEngine | None':
        return _CURRENT_ENGINE.get()

    def __enter__(self) -> 'SmartEngine':
        self._token = _CURRENT_ENGINE.set(self)
        return self

    def __exit__(self, exc_type, exc, tb):
        if self._token is not None:
            _CURRENT_ENGINE.reset(self._token)
        return False

    def _record(
        self, *, obj: Any, action_name: str, recovery: bool,
        phase: Literal["started", "succeeded", "failed", "recovery_chosen"],
        parent_event_id: str | None = None, error: Exception | None = None,
        details: dict[str, Any] | None = None, event_id: str | None = None,
    ) -> str:
        eid = event_id or str(uuid.uuid4())
        event = ActionEvent(
            eid, self.task_key, type(obj).__name__, action_name, recovery, phase, utc_now(),
            parent_event_id, type(error).__name__ if error is not None else None,
            str(error) if error is not None else None, details,
        )
        self.recorder.record(event)
        return eid

    def invoke(
        self, *, obj: Any, spec: ActionSpec, args: tuple[Any, ...],
        kwargs: dict[str, Any], allow_recovery: bool,
    ) -> Any:
        event_id = self._record(
            obj=obj, action_name=spec.name, recovery=spec.recovery, phase="started",
            details={"args": short(args), "kwargs": short(kwargs)},
        )
        print(f'\n[ACTION] {spec.name} cost={spec.cost:g}')
        try:
            result = spec.raw(obj, *args, **kwargs)
        except Exception as exc:
            self._record(
                obj=obj, action_name=spec.name, recovery=spec.recovery, phase="failed",
                parent_event_id=event_id, error=exc,
            )
            print(f'[ERROR ] {spec.name}: {type(exc).__name__}: {exc}')
            if not allow_recovery:
                raise
            return self._recover(
                obj=obj, failed_spec=spec, original_args=args, original_kwargs=kwargs,
                initial_error=exc, parent_event_id=event_id,
            )
        else:
            self._record(
                obj=obj, action_name=spec.name, recovery=spec.recovery, phase="succeeded",
                parent_event_id=event_id,
            )
            return result

    @staticmethod
    def _action_specs(obj: Any) -> list[ActionSpec]:
        found: dict[str, ActionSpec] = {}
        for cls in type(obj).__mro__:
            for value in cls.__dict__.values():
                spec = getattr(value, '__action_spec__', None)
                if spec is not None:
                    found.setdefault(spec.name, spec)
        return list(found.values())

    @staticmethod
    def _guard_passes(obj: Any, spec: ActionSpec, context: FailureContext) -> bool:
        guard = spec.guard
        if guard is None:
            return True
        if isinstance(guard, str):
            return bool(getattr(obj, guard)(context))
        return bool(guard(obj, context))

    def _enabled_recovery_actions(self, obj: Any, context: FailureContext) -> list[ActionSpec]:
        enabled: list[ActionSpec] = []
        for spec in self._action_specs(obj):
            if not spec.recovery:
                continue
            try:
                if self._guard_passes(obj, spec, context):
                    enabled.append(spec)
            except Exception as exc:
                print(f'[GUARD ] {spec.name} disabled: {type(exc).__name__}: {exc}')
        return enabled

    def _failure_context(
        self, obj: Any, failed_spec: ActionSpec, error: Exception, recovery_round: int
    ) -> FailureContext:
        features = self.context_provider(obj, failed_spec, error, self.runtime)
        return FailureContext(
            failed_spec.name, type(error).__name__, str(error), features, recovery_round
        )

    def _rank(
        self, enabled: list[ActionSpec], context: FailureContext,
        episode_counts: dict[str, int],
    ) -> list[RecoveryCandidate]:
        candidates: list[RecoveryCandidate] = []
        for spec in enabled:
            p_success = self.memory.success_probability(context, spec.name, spec.prior_success)
            learned_cost = self.memory.learned_cost(context, spec.name)
            cost = learned_cost if learned_cost is not None else spec.cost
            repeat_count = episode_counts.get(spec.name, 0)
            repeat_penalty = 1.0 + 0.75 * repeat_count
            expected_cost = cost * repeat_penalty / max(p_success, 0.02)
            candidates.append(RecoveryCandidate(spec=spec, p_success=p_success, expected_cost=expected_cost))
        best = min((c.expected_cost for c in candidates))
        weights = [math.exp(-(candidate.expected_cost - best) / self.temperature) for candidate in candidates]
        total = sum(weights)
        for candidate, weight in zip(candidates, weights):
            candidate.selection_probability = weight / total
        candidates.sort(key=lambda c: c.expected_cost)
        return candidates

    def _choose(self, candidates: list[RecoveryCandidate]) -> RecoveryCandidate:
        return self.random.choices(candidates, weights=[c.selection_probability for c in candidates], k=1)[0]

    def _recover(
        self, *, obj: Any, failed_spec: ActionSpec, original_args: tuple[Any, ...],
        original_kwargs: dict[str, Any], initial_error: Exception, parent_event_id: str,
    ) -> Any:
        error = initial_error
        episode_counts: dict[str, int] = {}
        for recovery_round in range(1, self.max_recovery_attempts + 1):
            context = self._failure_context(obj, failed_spec, error, recovery_round)
            enabled = self._enabled_recovery_actions(obj, context)
            if not enabled:
                raise RuntimeError(f'No recovery action is enabled for failed action {failed_spec.name!r}') from error
            ranked = self._rank(enabled, context, episode_counts)
            print('\n[PLAN] recovery candidates:')
            for candidate in ranked:
                print(
                    f"       {candidate.spec.name:18s} cost={candidate.spec.cost:6.2f} "
                    f"P(success)={candidate.p_success:5.3f} "
                    f"score={candidate.expected_cost:7.2f} "
                    f"P(select)={candidate.selection_probability:5.3f}"
                )
            chosen = self._choose(ranked)
            chosen_spec = chosen.spec
            episode_counts[chosen_spec.name] = episode_counts.get(chosen_spec.name, 0) + 1
            self._record(
                obj=obj, action_name=chosen_spec.name, recovery=True,
                phase="recovery_chosen", parent_event_id=parent_event_id,
                details={
                    "failed_action": failed_spec.name, "round": recovery_round,
                    "expected_cost": chosen.expected_cost, "p_success": chosen.p_success,
                    "p_select": chosen.selection_probability,
                },
            )
            print(f'[CHOOSE] {chosen_spec.name} (round {recovery_round})')
            recovery_event_id = self._record(
                obj=obj, action_name=chosen_spec.name, recovery=True, phase="started",
                parent_event_id=parent_event_id,
            )
            started = time.perf_counter()
            try:
                chosen_spec.raw(obj, context)
            except Exception as recovery_error:
                actual_cost = chosen_spec.cost + max(time.perf_counter() - started, 0.001)
                self._record(
                    obj=obj, action_name=chosen_spec.name, recovery=True, phase="failed",
                    parent_event_id=recovery_event_id, error=recovery_error,
                )
                self.memory.update(context, chosen_spec.name, success=False, actual_cost=actual_cost)
                print(f'[LEARN ] {chosen_spec.name} itself failed.')
                error = recovery_error
                continue
            else:
                self._record(
                    obj=obj, action_name=chosen_spec.name, recovery=True, phase="succeeded",
                    parent_event_id=recovery_event_id,
                )
            retry_event_id = self._record(
                obj=obj, action_name=failed_spec.name, recovery=False, phase="started",
                parent_event_id=recovery_event_id, details={"retry_after": chosen_spec.name},
            )
            try:
                result = failed_spec.raw(obj, *original_args, **original_kwargs)
            except Exception as retry_error:
                actual_cost = chosen_spec.cost + max(time.perf_counter() - started, 0.001)
                self._record(
                    obj=obj, action_name=failed_spec.name, recovery=False, phase="failed",
                    parent_event_id=retry_event_id, error=retry_error,
                )
                self.memory.update(context, chosen_spec.name, success=False, actual_cost=actual_cost)
                print(f'[LEARN ] {chosen_spec.name} did NOT recover {failed_spec.name}: {type(retry_error).__name__}')
                error = retry_error
                continue
            else:
                actual_cost = chosen_spec.cost + max(time.perf_counter() - started, 0.001)
                self._record(
                    obj=obj, action_name=failed_spec.name, recovery=False, phase="succeeded",
                    parent_event_id=retry_event_id,
                )
                self.memory.update(context, chosen_spec.name, success=True, actual_cost=actual_cost)
                print(f'[LEARN ] {chosen_spec.name} recovered {failed_spec.name}.')
                return result
        raise RuntimeError(
            f"Failed to recover {failed_spec.name!r} "
            f"after {self.max_recovery_attempts} attempts."
        ) from error

# --- SAM3 runtime (task-specific) -------------------------------------------
@dataclass
class SAM3Runtime:
    """
    Disposable process-local resources.

    SmartEngine stores this object opaquely but does not understand it.
    """
    model: Any = None
    frame: Any = None
    infer_result: Any = None
    current_frame: int | None = None

    def clear_frame(self) -> None:
        self.frame = None
        self.infer_result = None
        self.current_frame = None

    def clear_all(self) -> None:
        self.model = None
        self.clear_frame()

# --- SAM3 progress (task-specific) ------------------------------------------
class SAM3Progress(BaseModel):
    """
    This is deliberately NOT part of SAM3Segmentation and NOT part
    of SmartEngine.

    The SAM3 author decides what resumable progress means.
    """
    next_frame: int = 0
    completed: bool = False

class SAM3ProgressStore:
    """
    SAM3-specific persistence semantics.

    Another task can implement a completely different progress store.
    """

    def __init__(self, path: str | Path):
        self.file = JSONFile(path)

    def load(self, task_key: str) -> SAM3Progress:
        data = self.file.read({'tasks': {}})
        raw = data['tasks'].get(task_key)
        if raw is None:
            return SAM3Progress()
        return SAM3Progress.model_validate(raw)

    def save(self, task_key: str, progress: SAM3Progress) -> None:
        data = self.file.read({'tasks': {}})
        data['tasks'][task_key] = progress.model_dump(mode='json')
        self.file.write(data)

    def commit_frame(self, task_key: str, progress: SAM3Progress, frame_index: int) -> None:
        progress.next_frame = frame_index + 1
        self.save(task_key, progress)
        print(f'[PROGRESS] next_frame={progress.next_frame}')

    def mark_complete(self, task_key: str, progress: SAM3Progress) -> None:
        progress.completed = True
        self.save(task_key, progress)

# --- SAM3 task model ---------------------------------------------------------
class SAM3Segmentation(BaseModel):
    """Ordinary SAM3 implementation. No SmartEngine/@action/recovery dependency."""
    source: list[str] | str
    sam3_model_path: str
    prompt: str

    _runtime: SAM3Runtime = PrivateAttr(default_factory=SAM3Runtime)
    _random: random.Random = PrivateAttr(default_factory=random.Random)
    _hard_crash_rate: float = PrivateAttr(default=0.0)

    @property
    def runtime(self) -> SAM3Runtime:
        return self._runtime

    def configure_simulation(self, *, seed: int | None=None, hard_crash_rate: float=0.0) -> 'SAM3Segmentation':
        if seed is not None:
            self._random.seed(seed)
        self._hard_crash_rate = hard_crash_rate
        return self

    def _maybe_fail(self, operation: str, rate: float) -> None:
        if self._random.random() >= rate:
            return
        exc_type = self._random.choice([RuntimeError, OSError, TimeoutError, FakeGPUError])
        raise exc_type(f'simulated unknown error during {operation}')

    def _maybe_hard_crash(self, operation: str, rate: float) -> None:
        if rate > 0 and self._random.random() < rate:
            print(f'\n[CRASH!] simulated hard crash during {operation}')
            raise SimulatedHardCrash(f'hard crash during {operation}')

    def load_sam3(self) -> None:
        print(f'         pseudo load model {self.sam3_model_path!r}')
        self._maybe_fail('load_sam3', 0.12)
        self.runtime.model = {'path': self.sam3_model_path}

    def read_frame(self, index: int) -> None:
        self.runtime.current_frame = index
        source_name = self.source[index] if isinstance(self.source, list) else self.source
        print(f'         pseudo read frame {index}: {source_name}')
        self._maybe_fail('read_frame', 0.18)
        self.runtime.frame = {'index': index, 'source': source_name, 'pixels': f'<fake pixels {index}>'}
        self.runtime.infer_result = None

    def infer(self) -> dict[str, Any]:
        if self.runtime.model is None:
            raise RuntimeError('SAM3 model is missing from runtime')
        if self.runtime.frame is None:
            raise RuntimeError('frame is missing from runtime')
        print(f'         pseudo infer frame {self.runtime.current_frame} prompt={self.prompt!r}')
        self._maybe_fail('infer', 0.28)
        self._maybe_hard_crash('infer', self._hard_crash_rate)
        result = {
            'frame_index': self.runtime.current_frame, 'prompt': self.prompt,
            'mask_score': round(0.7 + self._random.random() * 0.29, 4),
        }
        self.runtime.infer_result = result
        return result

    def save_result(self, index: int) -> str:
        if self.runtime.infer_result is None:
            raise RuntimeError('no inference result to save')
        output_dir = Path('demo_outputs_separated')
        output_dir.mkdir(parents=True, exist_ok=True)
        task_key = json_hash(self.model_dump(mode='json'))
        output_path = output_dir / f'{task_key[:12]}_frame_{index:06d}.json'
        if output_path.exists():
            print(f'         reuse existing output: {output_path}')
            return str(output_path)
        print(f'         pseudo save frame {index}: {output_path}')
        self._maybe_fail('save_result', 0.1)
        with output_path.open('w', encoding='utf-8') as f:
            json.dump(self.runtime.infer_result, f, indent=2)
        self._maybe_hard_crash('save_result_after_write', self._hard_crash_rate * 0.35)
        return str(output_path)

    def unload_sam3(self) -> None:
        print('         pseudo unload SAM3')
        self.runtime.clear_all()


class SmartSAM3Segmentation(SAM3Segmentation):
    """Same public API + SmartEngine actions/recovery. super().xxx() bypasses the engine."""

    @action(cost=10)
    def load_sam3(self) -> None:
        return super().load_sam3()

    @action(cost=2)
    def read_frame(self, index: int) -> None:
        return super().read_frame(index)

    @action(cost=5)
    def infer(self) -> dict[str, Any]:
        return super().infer()

    @action(cost=1)
    def save_result(self, index: int) -> str:
        return super().save_result(index)

    @action(cost=1)
    def unload_sam3(self) -> None:
        return super().unload_sam3()

    def can_retry(self, context: FailureContext) -> bool:
        return True

    def can_reread_frame(self, context: FailureContext) -> bool:
        return context.failed_action in {'read_frame', 'infer'} and context.features.get('frame_index') is not None

    def can_reload_model(self, context: FailureContext) -> bool:
        return context.failed_action in {'load_sam3', 'infer'} and bool(self.sam3_model_path)

    def can_restart_runtime(self, context: FailureContext) -> bool:
        return context.failed_action in {'load_sam3', 'read_frame', 'infer'}

    @action(recovery=True, cost=1, guard='can_retry', prior_success=0.45)
    def retry(self, context: FailureContext) -> None:
        print('         recovery: retry original action')

    @action(recovery=True, cost=3, guard='can_reread_frame', prior_success=0.7)
    def reread_frame(self, context: FailureContext) -> None:
        index = context.features['frame_index']
        print(f'         recovery: reread frame {index}')
        return super().read_frame(index)

    @action(recovery=True, cost=12, guard='can_reload_model', prior_success=0.85)
    def reload_model(self, context: FailureContext) -> None:
        print('         recovery: reload model')
        self.runtime.model = None
        return super().load_sam3()

    @action(recovery=True, cost=30, guard='can_restart_runtime', prior_success=0.95)
    def restart_runtime(self, context: FailureContext) -> None:
        print('         recovery: rebuild runtime')
        index = context.features.get('frame_index')
        self.runtime.clear_all()
        super().load_sam3()
        if index is not None:
            super().read_frame(index)

# --- SAM3 recovery context ---------------------------------------------------
def sam3_context_provider(
    task: SAM3Segmentation, failed_spec: ActionSpec, error: Exception, runtime: SAM3Runtime
) -> dict[str, Any]:
    """
    SmartEngine does not know what these features mean.

    The task author chooses useful context for recovery learning.
    """
    if isinstance(task.source, list):
        source_kind = 'images'
        total = len(task.source)
    else:
        source_kind = 'video'
        total = None
    index = runtime.current_frame
    if index is None or total is None or total == 0:
        progress_bucket = 'unknown'
    else:
        ratio = index / total
        if ratio < 0.25:
            progress_bucket = '0-25%'
        elif ratio < 0.5:
            progress_bucket = '25-50%'
        elif ratio < 0.75:
            progress_bucket = '50-75%'
        else:
            progress_bucket = '75-100%'
    return {
        "frame_index": index, "source_kind": source_kind,
        "progress_bucket": progress_bucket, "model_loaded": runtime.model is not None,
        "frame_loaded": runtime.frame is not None, "result_available": runtime.infer_result is not None,
    }

# --- Task identity -----------------------------------------------------------
def sam3_task_key(task: SAM3Segmentation) -> str:
    """
    The application chooses task identity semantics.

    This demo hashes the declarative task specification.
    """
    return json_hash(task.model_dump(mode='json'))

# --- Application workflow ----------------------------------------------------
def run_sam3_job(task: SAM3Segmentation, *, progress_store: SAM3ProgressStore, task_key: str) -> None:
    """
    Notice:
      - SmartEngine is not passed in.
      - Progress is explicitly task-specific.
      - No generic engine.iterate()/commit().
      - The author controls resume semantics.
    """
    progress = progress_store.load(task_key)
    if progress.completed:
        print('\n[PROGRESS] task already complete.')
        return
    print(f'\n[PROGRESS] resume from frame {progress.next_frame}')
    task.load_sam3()
    if isinstance(task.source, list):
        total_frames = len(task.source)
    else:
        total_frames = 8
    for index in range(progress.next_frame, total_frames):
        task.read_frame(index)
        task.infer()
        task.save_result(index)
        progress_store.commit_frame(task_key, progress, index)
    task.unload_sam3()
    progress_store.mark_complete(task_key, progress)
    print('\n=== SAM3 JOB COMPLETE ===')

# --- Demo / supervisor -------------------------------------------------------
def build_demo_task() -> SmartSAM3Segmentation:
    return SmartSAM3Segmentation(
        source=[f"{i:03d}.jpg" for i in range(1, 9)],
        sam3_model_path="sam3_fake.pt", prompt="car",
    )

def reset_demo_files() -> None:
    paths = [Path('sam3_progress.json'), Path('generic_action_events.json'), Path('generic_action_memory.json')]
    for path in paths:
        if path.exists():
            path.unlink()
    out = Path('demo_outputs_separated')
    if out.exists():
        for child in out.glob('*.json'):
            child.unlink()

def run_demo(*, reset: bool, hard_crash_rate: float, seed: int, max_process_restarts: int=20) -> None:
    if reset:
        reset_demo_files()
    memory = JSONActionMemory('generic_action_memory.json')
    recorder = MultiRecorder(ConsoleActionRecorder(), JSONActionRecorder('generic_action_events.json'))
    progress_store = SAM3ProgressStore('sam3_progress.json')
    for generation in range(max_process_restarts + 1):
        task = build_demo_task().configure_simulation(
            seed=seed + generation * 101, hard_crash_rate=hard_crash_rate,
        )
        task_key = sam3_task_key(task)
        engine = SmartEngine(
            task_key=task_key, runtime=task.runtime, recorder=recorder, memory=memory,
            context_provider=sam3_context_provider, temperature=2.0,
            max_recovery_attempts=12, random_seed=seed + generation * 101,
        )
        try:
            with engine:
                run_sam3_job(task, progress_store=progress_store, task_key=task_key)
        except SimulatedHardCrash as exc:
            print('\n========================================')
            print('[SUPERVISOR] simulated process died:')
            print(f'             {exc}')
            print('[SUPERVISOR] SmartEngine has no progress state to restore.')
            print('[SUPERVISOR] The SAM3-specific progress store decides where the new run resumes.')
            print('========================================\n')
            continue
        else:
            break
    else:
        raise RuntimeError('Exceeded simulated process restart limit')
    memory.pretty_print()
    final_progress = progress_store.load(sam3_task_key(build_demo_task()))
    print('\n=== TASK-SPECIFIC FINAL PROGRESS ===')
    print(final_progress.model_dump_json(indent=2))

# def main() -> None:
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--reset', action='store_true')
#     parser.add_argument(
#         "--hard-crash-rate", type=float, default=0.0,
#         help="Try 0.05-0.10 to demonstrate task-specific crash resume.",
#     )
#     parser.add_argument('--seed', type=int, default=7)
#     args = parser.parse_args()
#     run_demo(reset=args.reset, hard_crash_rate=args.hard_crash_rate, seed=args.seed)
# if __name__ == '__main__':
#     main()

```


```
from typing import List, Union
from functools import wraps

class DBStorage(ShelveStorage):
    pass


class SAM3SegmentationModel:
    def __init__(self,
                 source:Union[List[str],str], # list of image path or one mp4 path str
                 sam3_model_path:str,
                 prompt:str,
                 current_cnt=0, # for resume to certain idx
                 ) -> None:
        self.FSMs_state=SAM3SegmentationFSMsController.SAM3SegmentationState.States.idle
        self.source = source
        self.current_cnt = current_cnt

    # do not random gen id, for to identify file
    @staticmethod
    def gen_id(file_name,file_size,file_hash):
        return f'{file_name},{file_size},{file_hash}'
    
    def get_id(self):
        pass
    
    def to_dict(self):
        return self.__dict__
    
    def from_dict(self,data):
        for k in self.__dict__.keys():
            setattr(self,k,data[k])
        return self

    def is_video_src(self):
        return isinstance(self.source,str)
    
class SAM3SegmentationFSMsController:
    
    class SAM3SegmentationState:
        class States:
            idle = 'idle'
            loaded_model = 'loaded_model'
            read_frame_stage = 'read_frame_stage'
            infer_frame_stage = 'infer_frame_stage'
            frame_complete = 'frame_complete'

            error_read_frame = 'error_read_frame'
            error_sam3_load_model = 'error_sam3_load_model'
            error_sam3_infer = 'error_sam3_infer'
            # error_other = 'error_other' # add more detailed errors will be better

            all_complete = 'all_complete'
        
        _transitions = {
            States.idle:                    [States.loaded_model],

            States.loaded_model:            [States.read_frame_stage, States.error_sam3_load_model],
            States.error_sam3_load_model:   [States.idle],

            States.read_frame_stage:        [States.infer_frame_stage, States.error_read_frame],
            States.error_read_frame:        [States.loaded_model, States.idle],
            
            States.infer_frame_stage:       [States.frame_complete, States.error_sam3_infer],
            States.error_sam3_infer:        [States.read_frame_stage, States.idle],
            
            States.frame_complete:          [States.read_frame_stage, States.all_complete],

        }
        _states = list(_transitions.keys())


    def __init__(self, model:'SAM3SegmentationModel'):
        self.model = model
        self.FSMs_STATES = SAM3SegmentationFSMsController.SAM3SegmentationState.States
        self.transitions = SAM3SegmentationFSMsController.SAM3SegmentationState._transitions

        # private placeholders
        self._frame_array = None
        self._sam3_model = None

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


    ################## private part
    @staticmethod
    def _read_img_frame():pass
    @staticmethod
    def _read_video_frame():pass
    @staticmethod
    def _load_sam3():pass


    ################## public FSMs part
    def valid_transition(func:Callable):
        @wraps(func)
        def wrapper(self:'SAM3SegmentationFSMsController',
                    *args, **kwargs):
            valid_transitions = self.transitions[self.current_state()]
            target_transition = func.__name__.replace('to_','')
            if target_transition not in valid_transitions:
                raise ValueError(f"Invalid transition from [{self.current_state()}] -> [{target_transition}]")
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                print(f'[{self.__class__.__name__}]: {e}')
        return wrapper

    @valid_transition
    def to_idle(self):
        self.set_state(self.FSMs_STATES.idle)

    @valid_transition
    def to_loaded_model(self):
        try:
            # try to load SAM3 model
            pass        
        except Exception as e:
            self.to_error_sam3_load_model(f"{e}")
            return

        self.set_state(self.FSMs_STATES.loaded_model)

    @valid_transition
    def to_error_sam3_load_model(self, error_msg):
        self.set_state(self.FSMs_STATES.error_sam3_load_model)

    @valid_transition
    def to_read_frame_stage(self):
        try:
            # try to read frame
            if self.model.is_video_src():
                pass
            else:
                img_path = self.model.source[self.model.current_cnt]
                self._frame_array = cv2.imread(img_path)                    
        except Exception as e:
            self.to_error_read_frame(f"{e}")
            return

        # complete read frame
        self.set_state(self.FSMs_STATES.read_frame_stage)

    @valid_transition
    def to_error_read_frame(self, error_msg):
        self.set_state(self.FSMs_STATES.error_read_frame)

    @valid_transition
    def to_infer_frame_stage(self, img):
        try:
            # try to do SAM3 infer
            pass        
        except Exception as e:
            self.to_error_sam3_infer(f"{e}")
            return
            
        self.set_state(self.FSMs_STATES.infer_frame_stage)
        self.to_frame_complete()

    @valid_transition
    def to_error_sam3_infer(self, error_msg):
        self.set_state(self.FSMs_STATES.error_sam3_infer)
           
    @valid_transition
    def to_frame_complete(self):
        self.model.current_cnt += 1
        
        if self.model.is_video_src():
            pass
        else:
            if self.model.current_cnt==len(self.model.source):
                return self.to_all_complete()
            
        self.set_state(self.FSMs_STATES.frame_complete)
        self.to_read_frame_stage()

    @valid_transition
    def to_all_complete(self):
        self.set_state(self.FSMs_STATES.all_complete)

    ################## public FSMs solver part
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
        print(f'Set target state: {target_state} ( current is {self.current_state()})')
        def next_first_action(task:VideoConversionFSMsController.VideoConversionState.States
                        ,target_state):
            path = self.find_path(VideoConversionFSMsController.VideoConversionState._transitions, task, target_state)
            if len(path)<=1: return None
            return path[1]
            
        while self.current_state() != target_state:
            cls = next_first_action(self.current_state(),target_state)
            if cls is None:raise ValueError('no next acion! unreachable!')
            if max_attempts<=0:raise ValueError(f'over max_attempts!')
            print(f'Current: {self.current_state()}, try to_{cls}')
            
            if simulate_error and random.random()>0.3:
                print('simulate some error!')
                continue
            
            getattr(self,f'to_{cls}')()
            max_attempts -= 1
        print(f'Success to target state: {self.current_state()}')
```

### Conclusion

The examples in this chapter demonstrate that resumable programming is not limited to one particular technology, framework, or type of application. The same basic idea can be applied to file uploads, media processing, AI inference, distributed services, and many other long-running or failure-prone tasks.

Although these applications are very different, they share a common structure:

```text
Task
  |
  v
Perform some work
  |
  v
Save meaningful progress
  |
  v
Continue
  |
  +---- failure ----> recover / restart
                         |
                         v
                  restore progress
                         |
                         v
                      continue
```

The central principle is simple:

> **Do not require a task to start from the beginning when enough information exists to continue from where it stopped.**

In the large-file upload example, this information is the list of successfully uploaded parts.

In the video conversion example, it is the number of frames that have already been processed.

In the AI segmentation example, it is the next frame that needs to be processed.

The meaning of *progress* is therefore application-specific.

This is an important lesson. A generic resumability framework can provide useful mechanisms for persistence, recovery, retries, event recording, and state transitions, but it cannot automatically decide what progress means for every possible application.

The application developer must define the **semantic checkpoint**.

For example:

```text
File Upload
    progress = uploaded parts

Video Conversion
    progress = converted frame index

AI Processing
    progress = next frame to process

Database Migration
    progress = last successfully migrated record

Web Crawler
    progress = visited URLs + pending URLs
```

Once this progress is stored persistently, the running process itself becomes much less important.

A machine may restart.

A container may disappear.

A network request may fail.

A GPU may run out of memory.

A worker may be replaced.

But if the important state survives, another process can continue the work.

This changes the way we think about reliability.

Traditional programs are often designed around the lifetime of a process:

```text
start program
    |
    v
perform work
    |
    v
finish
```

A resumable system is designed around the lifetime of a **task** instead:

```text
                 Persistent Task
                       |
          +------------+------------+
          |            |            |
          v            v            v
      Process A    Process B    Process C
          |            |            |
        crash        restart      continue
          |            |            |
          +------------+------------+
                       |
                       v
                    complete
```

The task can therefore live longer than any individual process executing it.

This is particularly valuable in modern computing environments. Cloud functions have execution limits, containers are disposable, distributed workers can fail, network connections are temporary, and AI workloads can consume significant amounts of computation.

In such environments, interruption should be considered a normal operating condition rather than an exceptional event.

Resumable programming gives us a systematic way to design for that reality.

---

Another important lesson from this chapter is that **resuming progress and recovering from errors are related, but they are not the same problem**.

Consider an AI inference task.

A progress store may tell us:

```text
next_frame = 350001
```

This tells the application **where to continue**.

But suppose processing frame 350001 produces:

```text
CUDA out of memory
```

The progress store cannot decide whether the best response is to:

```text
clear temporary tensors
```

or:

```text
reload the model
```

or:

```text
restart the GPU runtime
```

These are recovery decisions.

We can therefore think about a robust resumable architecture as having several separate responsibilities:

```text
+--------------------------------------------------+
|                  Application                     |
|                                                  |
|  Defines what the task means                     |
|  Defines what successful progress means          |
+--------------------------+-----------------------+
                           |
                           v
+--------------------------------------------------+
|               Progress / State Store             |
|                                                  |
|  Persists checkpoints                            |
|  Restores task progress                          |
+--------------------------+-----------------------+
                           |
                           v
+--------------------------------------------------+
|                  Recovery Logic                  |
|                                                  |
|  Detects failures                                |
|  Selects recovery actions                        |
|  Retries failed operations                       |
+--------------------------+-----------------------+
                           |
                           v
+--------------------------------------------------+
|                    Runtime                       |
|                                                  |
|  Files / Network / CPU / GPU / Database / Cloud  |
+--------------------------------------------------+
```

Keeping these responsibilities separate makes the system easier to understand, test, extend, and reuse.

The final AI example extends this idea further. Recovery does not necessarily have to follow a single hard-coded path. Different recovery actions can have different costs and different probabilities of success. By observing previous recovery attempts, a system can gradually learn which actions tend to work best under particular conditions.

This suggests an evolution from simple resumable programs toward **adaptive resumable systems**:

```text
Checkpoint
    +
State Machine
    +
Error Handling
    +
Recovery Actions
    +
Recovery History
    +
Adaptive Decision Making
```

The important point, however, is that increasingly intelligent recovery does not remove the need for correct persistence.

No matter how intelligent a recovery engine becomes, it still needs a reliable answer to one fundamental question:

> **What work has already been completed successfully?**

That question remains the foundation of resumable programming.

The goal is therefore not to create software that never fails.

Such software does not exist.

The more practical goal is to create software in which failure does not automatically mean losing all previous work.

A well-designed resumable system can fail, restart, restore its progress, recover its resources, and continue moving toward its target state.

That is the essential idea explored throughout this chapter:

> **Reliable software is not software that never stops. It is software that knows how to continue.**

### Additional Notes

- **FastAPI Documentation** ([fastapi.tiangolo.com](https://fastapi.tiangolo.com/)): FastAPI is used in the resumable large-file uploading example. Its official documentation provides detailed guidance on building APIs, handling uploaded files, validating requests, managing errors, and deploying Python web services.

- **Amazon S3 Documentation** ([docs.aws.amazon.com/s3](https://docs.aws.amazon.com/s3/)): Amazon S3 provides multipart upload functionality that is particularly useful for large and resumable file transfers. The documentation explains multipart uploads, upload IDs, individual parts, completion operations, and failure handling.

- **MongoDB Documentation** ([mongodb.com/docs](https://www.mongodb.com/docs/)): MongoDB is used in this chapter as one possible persistent backend for storing task state and progress. Its documentation covers document storage, update operations, indexing, transactions, replication, and other features useful when building larger resumable systems.

- **OpenCV Documentation** ([docs.opencv.org](https://docs.opencv.org/)): OpenCV is used in the video-processing examples. Its documentation provides further information about reading videos, accessing individual frames, image resizing, video encoding, and other computer-vision operations that can be combined with resumable workflows.

- **Pydantic Documentation** ([docs.pydantic.dev](https://docs.pydantic.dev/)): Pydantic is useful for defining structured task models, progress records, configuration objects, and persistent application data. It is especially helpful when resumable systems become large enough that explicit data validation and schema management are needed.

- **AWS Step Functions** ([aws.amazon.com/step-functions](https://aws.amazon.com/step-functions/)): AWS Step Functions is a useful real-world reference for understanding state-based and long-running workflows. It demonstrates how tasks, retries, errors, branches, and workflow state can be coordinated across distributed cloud services.

- **Temporal Documentation** ([docs.temporal.io](https://docs.temporal.io/)): Temporal is a workflow platform built around durable execution. It is an excellent resource for readers who want to explore how resumability, retries, persistent workflow state, timers, and failure recovery are handled in production-scale distributed systems.

- **Celery Documentation** ([docs.celeryq.dev](https://docs.celeryq.dev/)): Celery is a widely used distributed task queue for Python. Its documentation provides practical examples of background jobs, retries, task states, workers, scheduling, and failure handling, making it a useful reference when extending the examples in this chapter into distributed applications.

- **Finite-State Machine Concepts** ([Wikipedia — Finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine)): Readers who want to deepen their understanding of the state-machine approach used throughout this chapter can review the fundamental concepts of states, transitions, events, and terminal states before designing more complicated resumable workflows.

- **Segment Anything Research** ([Meta AI Research](https://ai.meta.com/research/)): The AI segmentation example demonstrates how expensive AI workloads can benefit from persistent progress and recovery. Meta AI's research resources provide further background on segmentation models and related computer-vision systems.

---


## Chapter 8: Testing Resumable Systems

### Introduction

Testing is one of the areas where resumable programming provides a surprisingly large advantage.

At first, a resumable system may appear more complicated than an ordinary program because it contains:

- persistent state,
- checkpoints,
- state transitions,
- retry logic,
- error states,
- and recovery paths.

However, these additional structures also make the behavior of the system much more explicit.

Consider an ordinary long-running function:

```python
def process_everything():
    load_data()
    process_data()
    save_result()
    send_notification()
```

If an error occurs somewhere in the middle, testing all possible situations can become difficult.

For example:

```text
What happens if load_data() succeeds,
but process_data() fails?

What happens if save_result() succeeds,
but the process crashes immediately afterward?

What happens if the program restarts?

Which operations should run again?

Which operations should not run again?
```

Much of the program's progress exists only implicitly inside the call stack and local variables.

A resumable program changes this.

Instead of representing a workflow as one large execution:

```text
A -> B -> C -> D
```

we explicitly represent its states and transitions:

```text
idle
  |
  v
loaded
  |
  v
processing
  |
  v
saved
  |
  v
complete
```

The transitions are usually implemented as ordinary functions:

```python
to_loaded()
to_processing()
to_saved()
to_complete()
```

This produces an important consequence:

> **Each transition can be tested independently as a normal function.**

Even better, because the possible transitions are explicitly defined, we can automatically test the transition graph itself.

We can also deliberately inject failures at different points and verify that the task can still restore its state and eventually reach the target state.

Therefore, resumability does not only improve runtime reliability.

It also improves **testability**.

- Objectives
    - test individual state transitions;
    - automatically test valid and invalid transitions;
    - test complete workflow paths;
    - test persistent checkpoints and restoration;
    - inject simulated failures;
    - use randomized failures to explore many recovery cases;
    - simulate hard crashes and process restarts;
    - and verify that important system invariants remain correct throughout recovery.

The key idea of this chapter is:

> **If a workflow is explicitly represented as states and transitions, much of its behavior becomes finite, visible, and automatically testable.**


### Section 1: State Transitions Make Natural Unit Tests

Consider a simple task with the following states:

```text
idle
  |
  v
prepared
  |
  v
processing
  |
  v
saved
  |
  v
complete
```

We can represent this workflow as:

```python
class TaskState:

    class States:
        idle = "idle"
        prepared = "prepared"
        processing = "processing"
        saved = "saved"
        complete = "complete"

    transitions = {
        States.idle: [
            States.prepared,
        ],

        States.prepared: [
            States.processing,
        ],

        States.processing: [
            States.saved,
        ],

        States.saved: [
            States.complete,
        ],

        States.complete: [],
    }
```

The legal workflow is now visible in one data structure.

We know exactly which transitions should succeed:

```text
idle       -> prepared
prepared   -> processing
processing -> saved
saved      -> complete
```

We also know which transitions should fail:

```text
idle       -> complete
idle       -> saved
prepared   -> complete
saved      -> processing
complete   -> anything
```

The state graph therefore acts almost like a testing specification.

Now implement a simple controller:

```python
class TaskModel:

    def __init__(self):
        self.state = TaskState.States.idle
        self.result = None


class TaskController:

    def __init__(self, model=None):
        self.model = model or TaskModel()

    def current_state(self):
        return self.model.state

    def set_state(self, state):
        self.model.state = state

    def transition_to(self, target):
        current = self.current_state()

        valid = TaskState.transitions[current]

        if target not in valid:
            raise ValueError(
                f"Invalid transition: {current} -> {target}"
            )

        self.set_state(target)

    def to_prepared(self):
        self.transition_to(TaskState.States.prepared)

    def to_processing(self):
        self.transition_to(TaskState.States.processing)

    def to_saved(self):
        self.transition_to(TaskState.States.saved)

    def to_complete(self):
        self.transition_to(TaskState.States.complete)
```

Each transition is now a small function.

Testing one transition is simple:

```python
def test_idle_to_prepared():

    controller = TaskController()

    assert controller.current_state() == "idle"

    controller.to_prepared()

    assert controller.current_state() == "prepared"
```

Another transition can be tested independently:

```python
def test_processing_to_saved():

    controller = TaskController()

    controller.set_state(
        TaskState.States.processing
    )

    controller.to_saved()

    assert controller.current_state() == "saved"
```

This is one of the important advantages of resumable programming.

Instead of testing:

```text
one enormous workflow
```

we test:

```text
many small transitions
```

Each transition normally has:

```text
known starting state
        +
known action
        +
known expected state
```

This creates very clear unit tests.


### Section 2: Automatically Testing the Whole State Graph

Because the state machine already defines all allowed transitions, we do not need to write every test case manually.

We can generate them automatically.

First, generate every valid transition:

```python
VALID_TRANSITIONS = [
    (start, target)
    for start, targets in TaskState.transitions.items()
    for target in targets
]
```

Then use `pytest`:

```python
import pytest


@pytest.mark.parametrize(
    "start_state,target_state",
    VALID_TRANSITIONS,
)
def test_all_valid_transitions(
    start_state,
    target_state,
):

    controller = TaskController()

    controller.set_state(start_state)

    controller.transition_to(target_state)

    assert controller.current_state() == target_state
```

Now every declared transition is automatically tested.

Suppose we later add:

```text
processing -> paused
paused -> processing
```

and update the transition table:

```python
States.processing: [
    States.saved,
    States.paused,
],

States.paused: [
    States.processing,
],
```

those transitions automatically become part of the test suite.

The workflow definition itself becomes test input.

We can do the same thing for invalid transitions.

```python
ALL_STATES = list(
    TaskState.transitions.keys()
)

INVALID_TRANSITIONS = []

for start in ALL_STATES:

    valid_targets = TaskState.transitions[start]

    for target in ALL_STATES:

        if target not in valid_targets:

            INVALID_TRANSITIONS.append(
                (start, target)
            )
```

Then:

```python
@pytest.mark.parametrize(
    "start_state,target_state",
    INVALID_TRANSITIONS,
)
def test_all_invalid_transitions(
    start_state,
    target_state,
):

    controller = TaskController()

    controller.set_state(start_state)

    with pytest.raises(ValueError):
        controller.transition_to(target_state)

    assert controller.current_state() == start_state
```

Now we test both:

```text
all legal transitions
```

and:

```text
all illegal transitions
```

For the declared state graph, this can be exhaustive.

This is an important distinction.

Randomized testing can explore many runtime failures, but the finite transition graph itself can often be tested completely.

We should also test complete workflow paths.

```python
def test_complete_workflow():

    controller = TaskController()

    controller.to_prepared()
    controller.to_processing()
    controller.to_saved()
    controller.to_complete()

    assert controller.current_state() == "complete"
```

Unit tests verify individual edges:

```text
A -> B
```

while integration tests verify paths:

```text
A -> B -> C -> D -> E
```

Both are important.




### Section 3: Testing Persistent State and Resuming After Restart

Testing transitions alone is not enough.

A resumable system must also survive the loss of its runtime process.

Consider a task that processes several items.

```python
class TaskModel:

    def __init__(
        self,
        state="idle",
        current_item=0,
        total_items=10,
        results=None,
    ):
        self.state = state
        self.current_item = current_item
        self.total_items = total_items
        self.results = (
            results if results is not None else {}
        )

    def to_dict(self):
        return {
            "state": self.state,
            "current_item": self.current_item,
            "total_items": self.total_items,
            "results": self.results.copy(),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
```

For testing, we can use a lightweight storage implementation:

```python
class MemoryStorage:

    def __init__(self):
        self.data = {}

    def save(self, key, value):
        self.data[key] = value.copy()

    def load(self, key):
        value = self.data.get(key)

        if value is None:
            return None

        return value.copy()
```

A real application may instead use:

```text
Shelve
MongoDB
PostgreSQL
Redis
DynamoDB
Firestore
S3
```

But the testing principle is the same.

Now we can simulate a process restart:

```python
def test_resume_after_restart():

    storage = MemoryStorage()

    # First runtime
    model = TaskModel(
        state="processing",
        current_item=4,
    )

    storage.save(
        "task-001",
        model.to_dict(),
    )

    # Old runtime disappears.
    del model

    # New runtime restores the task.
    restored = TaskModel.from_dict(
        storage.load("task-001")
    )

    assert restored.state == "processing"
    assert restored.current_item == 4
```

This test asks an important question:

> **Can a completely new runtime reconstruct enough information to continue the task?**

Testing whether the same Python object can continue is not sufficient.

True resumability means:

```text
old runtime disappears
        |
        v
persistent state remains
        |
        v
new runtime starts
        |
        v
task continues
```

This is one of the most important tests in a resumable system.


### Section 4: Failure Injection and Checkpoint Testing

A resumable system should not wait for real production failures before its recovery logic is tested.

Instead, we should create failures deliberately.

Define a simulated error:

```python
class SimulatedError(RuntimeError):
    pass
```

A simple function can then expose an artificial failure:

```python
def process_item(simulate_error=False):

    if simulate_error:
        raise SimulatedError(
            "Simulated processing failure"
        )

    return "success"
```

And test it:

```python
def test_simulated_failure():

    with pytest.raises(SimulatedError):
        process_item(
            simulate_error=True
        )
```

For larger systems, adding `simulate_error=True` to every function becomes inconvenient.

A reusable failure injector is better:

```python
import random


class FailureInjector:

    def __init__(
        self,
        probability=0.0,
        seed=None,
    ):
        self.probability = probability
        self.random = random.Random(seed)

    def check(self, location):

        if self.random.random() < self.probability:

            raise SimulatedError(
                f"Simulated failure at: {location}"
            )
```

Now we can add explicit failure points:

```python
def process_one(
    model,
    storage,
    failure_injector,
):

    index = model.current_item

    failure_injector.check(
        "before_processing"
    )

    result = index * 10

    failure_injector.check(
        "before_saving_result"
    )

    model.results[index] = result
    model.current_item += 1

    storage.save(
        "task-001",
        model.to_dict(),
    )

    failure_injector.check(
        "after_checkpoint"
    )
```

The location of a failure matters.

Consider:

```text
perform work
    |
    v
save result
    |
    v
update checkpoint
```

If the program crashes before doing the work:

```text
CRASH
  |
  v
perform work
```

nothing has been completed, so retrying is simple.

If the work succeeds but the checkpoint is not saved:

```text
perform work
    |
    v
CRASH
    |
    X
checkpoint
```

the operation may run again after restart.

This is why idempotent operations are extremely useful.

If the checkpoint is saved and the program crashes afterward:

```text
perform work
    |
    v
checkpoint
    |
    v
CRASH
```

the new runtime should load the checkpoint and continue with the next operation.

Failure injection makes these normally difficult situations easy to reproduce.


### Section 5: Randomized Failure Testing

We can now extend failure injection into randomized testing.

For example:

```python
failure = FailureInjector(
    probability=0.20,
    seed=123,
)
```

Every call to:

```python
failure.check(...)
```

now has a 20% probability of raising a simulated error.

During one execution, failures might occur like this:

```text
item 3   -> failure before processing
item 7   -> failure before checkpoint
item 15  -> failure after checkpoint
item 18  -> failure before processing
item 31  -> failure after checkpoint
```

Another random seed produces a different sequence.

We can automatically restart the task whenever a simulated failure occurs.

```python
def run_with_restarts(
    storage,
    failure,
    max_restarts=1000,
):

    task_key = "task-001"

    if storage.load(task_key) is None:

        model = TaskModel(
            state="processing",
            current_item=0,
            total_items=20,
        )

        storage.save(
            task_key,
            model.to_dict(),
        )

    for restart_count in range(max_restarts):

        model = TaskModel.from_dict(
            storage.load(task_key)
        )

        try:

            while (
                model.current_item
                < model.total_items
            ):

                process_one(
                    model,
                    storage,
                    failure,
                )

            model.state = "complete"

            storage.save(
                task_key,
                model.to_dict(),
            )

            return model

        except SimulatedError as e:

            print(
                f"restart={restart_count}, "
                f"error={e}"
            )

            # The runtime is considered lost.
            # A new one will restore from storage.
            continue

    raise RuntimeError(
        "Task did not finish "
        "within restart limit."
    )
```

The test becomes:

```python
def test_random_failures():

    storage = MemoryStorage()

    failure = FailureInjector(
        probability=0.20,
        seed=123,
    )

    result = run_with_restarts(
        storage,
        failure,
    )

    assert result.state == "complete"
    assert result.current_item == 20
    assert len(result.results) == 20
```

The important result is not that no error occurred.

Many errors may occur.

What matters is:

```text
errors occurred
      +
runtime restarted
      +
state restored
      +
work continued
      =
task completed correctly
```

This is exactly what a resumable system is designed to achieve.

We can run many different failure patterns:

```python
@pytest.mark.parametrize(
    "seed",
    range(100),
)
def test_many_random_failure_patterns(seed):

    storage = MemoryStorage()

    failure = FailureInjector(
        probability=0.20,
        seed=seed,
    )

    result = run_with_restarts(
        storage,
        failure,
    )

    assert result.state == "complete"
    assert result.current_item == 20

    assert result.results == {
        i: i * 10
        for i in range(20)
    }
```

Now the system executes under:

```text
seed 0
seed 1
seed 2
...
seed 99
```

Each seed gives us a different deterministic failure sequence.

This can expose problems such as:

```text
failure immediately after checkpoint

multiple consecutive failures

failure during the first operation

failure near completion

failure after repeated resumptions
```

Randomized testing cannot mathematically prove that every possible runtime failure has been tested.

However, it can explore a very large number of combinations automatically.


### Section 6: Reproducible Random Tests and Invariants

Random testing should never mean unreproducible testing.

This is why the previous examples use:

```python
seed=123
```

Suppose continuous integration reports:

```text
test_many_random_failure_patterns[73] FAILED
```

We know exactly which sequence caused the failure.

We can reproduce it:

```python
failure = FailureInjector(
    probability=0.20,
    seed=73,
)
```

A useful randomized test should record:

```text
random seed
failure location
current state
current progress
exception type
```

For example:

```text
seed=73
state=processing
current_item=14
failure_location=after_checkpoint
exception=SimulatedError
```

This turns a random failure into a deterministic debugging case.

We should also verify more than the final result.

A resumable system has important **invariants** that should remain true even after failure.

For example:

```text
current_item >= 0

current_item <= total_items

every item before current_item has a result

completed task ->
current_item == total_items
```

We can express them directly:

```python
def assert_task_invariants(model):

    assert model.current_item >= 0

    assert (
        model.current_item
        <= model.total_items
    )

    for i in range(
        model.current_item
    ):
        assert i in model.results

    if model.state == "complete":

        assert (
            model.current_item
            == model.total_items
        )
```

Now test the state after every failure:

```python
for restart in range(1000):

    model = TaskModel.from_dict(
        storage.load("task-001")
    )

    assert_task_invariants(model)

    try:

        continue_task(model)

    except SimulatedError:

        restored = TaskModel.from_dict(
            storage.load("task-001")
        )

        assert_task_invariants(
            restored
        )

        continue

    break
```

This is stronger than asking only:

```text
Did the task eventually complete?
```

We also ask:

```text
Was the persisted state correct after every failure?
```

That is a much stronger reliability test.



### Section 7: Testing Hard Crashes and Recovery Functions

Ordinary exceptions are not the only possible failures.

Sometimes the process disappears without application code having an opportunity to catch the error.

We can simulate this with:

```python
class SimulatedHardCrash(BaseException):
    pass
```

Why use `BaseException` instead of `Exception`?

Because application code often contains:

```python
try:
    ...
except Exception:
    ...
```

A custom `BaseException` can bypass those normal handlers.

Therefore:

```python
raise SimulatedHardCrash()
```

can imitate situations such as:

```text
process termination
container restart
native-library crash
machine restart
```

For example:

```python
def maybe_hard_crash(
    random_generator,
    probability,
):

    if (
        random_generator.random()
        < probability
    ):
        raise SimulatedHardCrash(
            "Simulated process death"
        )
```

A supervisor can then recreate the task:

```python
try:

    run_task()

except SimulatedHardCrash:

    # Old runtime is gone.
    # Create a new runtime and restore progress.
    restart_task()
```

This verifies the most important architectural property:

```text
runtime may disappear
```

while:

```text
persistent progress survives
```

Recovery actions themselves can also be tested independently.

For example:

```python
def clear_cache():
    ...

def reconnect_database():
    ...

def reload_model():
    ...

def restart_runtime():
    ...
```

Suppose an AI service has:

```python
def reload_model(self):
    self.runtime.model = None
    self.load_model()
```

The test is straightforward:

```python
def test_reload_model():

    service = FakeAIService()

    old_model = service.runtime.model

    service.reload_model()

    assert service.runtime.model is not None
    assert service.runtime.model is not old_model
```

This is another benefit of separating:

```text
persistent progress
recovery behavior
runtime resources
```

Each responsibility can be tested independently.


### Section 8: Applying the Method to Real Resumable Systems

The same testing strategy can be applied to the practical examples from the previous chapter.

#### Large File Upload

A large-file upload task may store:

```text
upload_id
parts
total_chunks
state
```

Useful invariants include:

```python
assert len(parts) <= total_chunks
```

and:

```python
for index, part in enumerate(
    parts,
    start=1,
):
    assert (
        part["PartNumber"]
        == index
    )
```

Possible failure points include:

```text
before upload_part()

after upload_part()

before recording ETag

after recording ETag

before complete_multipart_upload()

after complete_multipart_upload()
```

The test repeatedly restarts the controller until the expected final state is reached:

```text
all chunks uploaded

parts are correct

no required chunk is missing

final object is complete

state == merged
```

#### Video Conversion

For video conversion, progress may contain:

```text
converted_count
total_count
state
```

Useful invariants include:

```python
assert converted_count >= 0
assert converted_count <= total_count
```

When complete:

```python
assert converted_count == total_count
```

Possible simulated failures include:

```text
before reading frame

after reading frame

before resizing

after resizing

before writing output

after writing output

before checkpoint

after checkpoint
```

The test repeatedly:

```text
runs
fails
restores
continues
```

until:

```text
state == complete_mp4
```

#### AI Processing

AI workloads are particularly suitable for this approach because they may encounter:

```text
CUDA out of memory

model loading failure

corrupted image

video decoding error

GPU runtime failure

result-writing failure
```

Persistent progress may be as simple as:

```text
next_frame = 350001
```

while runtime resources may include:

```text
model
frame
inference result
GPU memory
```

Recovery actions might include:

```text
clear_frame

clear_cache

reload_model

restart_runtime
```

Random failures can be injected into:

```text
load model

read frame

run inference

save result

checkpoint progress
```

The test can then verify:

```text
committed work is not lost

progress remains valid

results correspond to committed progress

recovery does not corrupt state

task eventually completes
```

The same idea can also scale from unit testing to larger fault-injection systems.

At the smallest level:

```text
raise SimulatedError()
```

At a larger level:

```text
terminate worker process
```

At an even larger level:

```text
disconnect network

restart database

kill container

remove worker

delay messages

make storage temporarily unavailable
```

This connects resumable-system testing with ideas such as:

```text
fault injection
chaos testing
chaos engineering
```

The scale changes, but the principle remains the same:

> **Create failures deliberately and verify that the system preserves valid progress and continues correctly.**


### Conclusion

At first glance, adding explicit state, checkpoints, error states, and recovery logic may seem to make a program more complicated.

From the perspective of testing, however, these structures can make the system easier to reason about.

Instead of one large operation:

```text
do everything
```

we have:

```text
state
  +
transition
  +
checkpoint
  +
recovery
```

A transition is usually an ordinary function.

Therefore, it can be unit tested.

The transition graph is explicit.

Therefore, all declared valid and invalid transitions can be tested automatically.

Progress is persistent.

Therefore, we can destroy the runtime and verify that a new runtime restores the task correctly.

Failures are expected.

Therefore, we can deliberately inject them.

And because simulated failures are inexpensive, we can run the same workflow hundreds or thousands of times using different failure sequences.

The core idea can be summarized as:

```text
Explicit States
      +
Small Transition Functions
      +
Persistent Checkpoints
      +
Failure Injection
      +
Automatic Restart
      =
Highly Testable Resumable System
```

There are two especially powerful forms of testing here.

The first is **exhaustive transition testing**:

```text
all valid transitions
+
all invalid transitions
```

The second is **randomized failure testing**:

```text
many failure positions
+
many retry sequences
+
many restart sequences
```

The transition graph is finite, so it can often be tested completely.

Runtime failure combinations may be much larger, so random failure injection helps explore them automatically.

Together, these approaches provide strong confidence in the behavior of a resumable system.

More importantly, they change our attitude toward failure.

Instead of asking:

> **Will this system work if nothing goes wrong?**

we can ask:

> **How many things can we deliberately make go wrong while the system still completes correctly?**

That is a much stronger test of reliability.

A well-designed resumable system should repeatedly demonstrate that it can:

```text
run
fail
restore
recover
continue
complete
```

And because those behaviors are explicit parts of the architecture, they can themselves become ordinary automated tests.

### Additional Notes

- **Pytest Documentation** ([docs.pytest.org](https://docs.pytest.org/)): Pytest is a popular Python testing framework and works particularly well for testing state transitions, parameterized transition tables, exceptions, fixtures, and repeated test cases.

- **Python `unittest` Documentation** ([docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)): Python's built-in `unittest` framework provides test cases, assertions, setup and teardown mechanisms, and mocking support without requiring an additional testing package.

- **Hypothesis** ([hypothesis.readthedocs.io](https://hypothesis.readthedocs.io/)): Hypothesis is a property-based testing framework for Python. Instead of manually specifying every input, developers describe properties that should remain true and Hypothesis automatically generates many test cases. This approach fits especially well with state-machine invariants and resumable-system testing.

- **Hypothesis Stateful Testing** ([hypothesis.readthedocs.io/en/latest/stateful.html](https://hypothesis.readthedocs.io/en/latest/stateful.html)): Hypothesis provides dedicated support for rule-based state-machine testing. This is particularly relevant to resumable programming because state transitions and invariants can be expressed directly and automatically explored through many action sequences.

- **Coverage.py** ([coverage.readthedocs.io](https://coverage.readthedocs.io/)): Coverage.py measures which parts of Python code are executed by tests. It is useful for checking whether transition functions, failure states, and recovery paths are actually exercised.

- **Python `random` Documentation** ([docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html)): Python's random-number utilities can create reproducible simulated failures. Recording and reusing the random seed is especially important when randomized testing discovers a failure.

- **Python `unittest.mock` Documentation** ([docs.python.org/3/library/unittest.mock.html](https://docs.python.org/3/library/unittest.mock.html)): Mock objects are useful for simulating databases, network APIs, cloud services, GPUs, file systems, and other dependencies without requiring real external failures.

- **Principles of Chaos Engineering** ([principlesofchaos.org](https://principlesofchaos.org/)): Chaos engineering extends failure injection from unit tests to complete running systems. It deliberately introduces failures to verify that distributed applications remain reliable and recover correctly.

---

## Chapter 9: Architectural Considerations for Resumability

### Introduction

* Position this chapter as the **bridge between code-level patterns** (FSM, MVC, SQL vs KV, etc.) and **system-level architecture**.
* Emphasize: *“Resumability is not just a function feature; it’s a system property.”*

### Section 1: When Do We Save Progress?

> **When should we persist progress so that a task can safely resume?**

Saving too often wastes I/O and slows the system. Saving too rarely means a crash forces you to redo a lot of work. Resumability is basically the art of choosing **good checkpoints**.

In this section, we’ll look at common strategies and trade-offs.


#### 1.1 Coarse-Grained vs Fine-Grained Checkpoints

For any resumable task, you can decide to checkpoint at different “resolutions”:

* **Coarse-Grained Checkpoints**
  You only save state at *high-level steps*.

  * Examples:

    * Checkout flow: `"step = 'payment'"`, `"step = 'review'"`, `"step = 'complete'"`.
    * User registration: `"step = 'email_verified'"`.
  * If you crash mid-step, you redo that whole step.
  * **Good when**:

    * Each step is relatively cheap.
    * The user can tolerate redoing the step.

* **Fine-Grained Checkpoints**
  You save progress frequently, e.g. per chunk, per frame, per record.

  * Examples:

    * S3 upload: `"parts_uploaded = 37 of 100"`.
    * Video conversion: `"converted_count = 1200 of 5423 frames"`.
  * If you crash, you lose at most a small piece of work.
  * **Good when**:

    * Each unit of work is expensive.
    * Task runs for minutes or hours.
    * Retrying a big chunk is painful (or costly).

A practical way to decide:

> **Ask: “How much work is acceptable to lose after a crash?”**
> That answer defines your checkpoint granularity.


#### 1.2 Common Triggers for Saving Progress

Architecturally, you rarely “just save whenever”. You usually anchor checkpoints to **specific events**:

1. **On State Transition (FSM-Level Checkpoint)**

   * Every time your FSM state changes, you persist:

     * `current_state`,
     * key progress fields,
     * timestamps / last error.
   * Example:

     * `idle → receiving`
       Save: upload metadata, initialized parts list.
     * `receiving → received`
       Save: final parts array (`[PartNumber, ETag, ...]`), ready to merge.
   * **Pros**: Simple, predictable, aligns with your conceptual model.
   * **Cons**: If a state encapsulates a lot of work internally, you may still lose progress inside that state.

2. **Every N Units of Work (Loop-Level Checkpoint)**

   * In long loops, save after processing N items:

     * N frames, N records, N chunks.
   * Example (video conversion):
     Save every 50 frames:

     ```python
     for frame_idx in range(model.converted_count, model.total_count):
         # process frame...
         model.converted_count = frame_idx + 1
         if frame_idx % 50 == 0:
             controller.save_model()
     ```
   * **Pros**: Tunable trade-off between overhead and possible rework.
   * **Cons**: Requires careful choice of N; too small = heavy I/O, too large = painful rework.

3. **On External Boundaries (Time / Size / API Limits)**

   * Save when:

     * A **time budget** is nearly exhausted (e.g. AWS Lambda’s ~15 minutes).
     * A **size threshold** is reached (e.g. local file size, memory usage).
     * An **API limit** is close (e.g. N API calls per run).
   * Example:

     * In a Lambda, stop work if you are close to timeout:

       * Write current progress,
       * Return control, let the next invocation resume.

4. **On “Risky” Operations**

   * Before:

     * Deleting the only copy of something,
     * Merging partial uploads,
     * Switching to a new state that is hard to roll back,
   * You save a checkpoint you can roll back to if things go wrong.


#### 1.3 Balancing Overhead vs Safety

Saving progress has a cost:

* Extra DB writes,
* Extra filesystem writes,
* More contention on shared resources.

But not saving enough has a different cost:

* CPU/GPU time wasted recomputing work,
* Money (cloud compute),
* User frustration (having to restart).

A simple mental model:

* **Checkpoint Cost**: `C_save` (time + money)
* **Work Lost on Crash**: `C_redo` (average cost to redo between checkpoints)
* **Crash Likelihood**: `p_crash` in that window

Expected cost per window ≈
`C_save + p_crash * C_redo`

You don’t need precise numbers, but this tells you:

* If failures are common or expensive → more frequent checkpoints.
* If failures are rare and work is cheap → fewer checkpoints.

A practical engineering heuristic:

* For **CPU-heavy** or **I/O-heavy** long tasks:
  Checkpoint per **1–5 seconds** of work, or per **small batch**.
* For **user-driven low-cost steps** (forms, short interactions):
  Checkpoint per **step** or per **screen**.


#### 1.4 Example: Tuning a Resumable Loop

Consider a simplified pseudo-loop for a resumable job:

```python
class JobModel:
    def __init__(self, job_id, offset=0, total=0):
        self.job_id = job_id
        self.offset = offset  # how many items processed
        self.total = total

    def to_dict(self): return self.__dict__

class JobController:
    CHECKPOINT_EVERY = 100  # tune this

    def __init__(self, model, storage):
        self.model = model
        self.storage = storage

    def save(self):
        self.storage.set(self.model.job_id, self.model.to_dict())

    def run(self, items):
        for idx in range(self.model.offset, len(items)):
            item = items[idx]
            self.process(item)
            
            self.model.offset = idx + 1

            if self.model.offset % self.CHECKPOINT_EVERY == 0:
                self.save()  # checkpoint

        # final checkpoint
        self.save()

    def process(self, item):
        # heavy work here
        pass
```

Architectural tuning knobs:

* **`CHECKPOINT_EVERY = 1`**

  * Very safe, minimal lost work.
  * DB-heavy, may throttle throughput.

* **`CHECKPOINT_EVERY = 1000`**

  * Light on DB, but a crash means reprocessing up to 1000 items.

In a real system, you adjust `CHECKPOINT_EVERY` based on:

* Average item processing cost,
* DB capacity,
* Observed crash frequency / node churn,
* SLAs (how much rework is acceptable).


#### 1.5 Design Heuristics: When to Save

When you design a resumable workflow, it helps to explicitly answer:

1. **What is the “unit of progress”?**

   * A step, a chunk, a frame, a record, an API call?
2. **What is the worst-case rework if we crash between checkpoints?**

   * Is that acceptable for:

     * CPU time?
     * Money?
     * User patience?
3. **Where is the natural “safe” boundary?**

   * At FSM state transitions?
   * At the end of a loop batch?
   * After writing a stable intermediate file?
4. **What does rollback look like if a checkpoint is “bad”?**

   * Can we safely rerun from the last checkpoint?
   * Do we need compensating actions (e.g., delete partial uploads, discard broken temp files)?

If you can answer these questions for each major process, you are no longer “just retrying and hoping”. You are *choosing* when to save progress to balance performance, cost, and reliability.

### Section 2: Where Does State Live?

Resumability always starts with one core question:

> **If the process dies *right now*, where does the truth live?**

In previous chapters, we stored state in different places:

* SQL / key-value databases (Chapter 2),
* Models controlled by FSMs (Chapter 6),
* MongoDB / Shelve-based storage plus S3, local files, etc. (Chapter 7).

In this section, we step back and classify the main **locations of state** and their implications for resumability.

#### 2.1 In-Memory State (Process Memory)

This is the fastest, most convenient place for state — local variables, objects, caches.

* **Pros**

  * Extremely fast reads and writes.
  * Simple to manipulate with normal language features (objects, lists, dicts).
* **Cons**

  * Disappears on crash, restart, or redeploy.
  * Hard to share across processes / machines.
* **Consequence for Resumability**

  * Any critical state that *only* exists in memory is **not resumable**.
  * In-memory state is fine as a *working copy*, but not as the **system of record**.

In a resumable design, think of in-memory state as “scratch space” between durable checkpoints.

#### 2.2 Durable Databases (SQL and NoSQL)

Databases are the most common place to keep resumable state:

* **Relational (SQL)**: tables, rows, transactions.
* **Key-Value / Document (NoSQL)**: flexible schemas, high scalability.

Typical patterns:

* A **task table / collection**:

  * `id`, `current_state`, `progress`, `last_error`, `updated_at`.

* A **model document** per unit of work:

  * As in `S3LargeUploadingModel` or `VideoConversionModel`.

* **Pros**

  * Durable, crash-safe (when configured properly).
  * Good query capabilities (e.g., “all tasks in error state”).
  * Easy to integrate with monitoring and admin UIs.

* **Cons**

  * Writing too often can become a bottleneck.
  * Schema and migration management (for SQL).

* **Consequence for Resumability**

  * The database is usually the **canonical place** to resume from.
  * Every important transition in your FSM should be reflected here:

    * New row/document created at start,
    * Progress/offset updated,
    * Final state marked (`completed`, `failed`, `canceled`).

A good rule of thumb:

> If you need to answer “where did this task stop?” tomorrow, it belongs in the database.

#### 2.3 Message Queues and Event Logs

Some systems rely heavily on:

* Message queues (e.g., RabbitMQ, SQS, Kafka topics),
* Event logs / streams.

Here, resumability can be based on:

* **Offsets / positions** in a topic,

* “At-least-once” handlers that can be **replayed**.

* **Pros**

  * Built-in buffering, retry, and decoupling between producer/consumer.
  * Natural way to model long-running workflows (“one message per step”).

* **Cons**

  * The queue itself usually does **not** know semantic progress (only that messages were delivered).
  * You still need an external “task state” somewhere if you care about higher-level workflow state.

* **Consequence for Resumability**

  * Queues help you *resume processing work*, but you still need:

    * Either an offset,
    * Or a task record, to know *what* has been done and *what* remains.

For complex workflows, queues are best combined with **FSM + DB**, not used as the only state store.

#### 2.4 Files, Object Storage, and External Services

Examples already use:

* **S3** multipart uploads,
* Local files (`*.bin` for frames, final thumbnails).

These are also part of system state:

* Uploaded parts in S3,

* Temporary binary files,

* Final output files.

* **Pros**

  * Suitable for large binary data (videos, images, archives).
  * Often cheaper and more scalable than storing blobs in a database.

* **Cons**

  * Harder to query (“Which uploads are half-done?”).
  * Operations are usually not transactional with your database.

* **Consequence for Resumability**

  * Treat file/object storage as **payload storage**, not the main source of *workflow state*.
  * Use the DB/model to record:

    * Which parts have been uploaded,
    * Which intermediate files exist,
    * Where the final output lives.

S3 upload example does this nicely: S3 holds chunks; Mongo/Shelve holds *which* chunks are done.

#### 2.5 Client-Side State (Browser, Mobile, Desktop)

Sometimes the **client itself** (browser, mobile app) holds part of the resumable state:

* Selected file, last played position, in-progress form, local drafts.

* Stored via:

  * `localStorage`, `IndexedDB`,
  * Mobile app local DB,
  * Desktop config / cache files.

* **Pros**

  * Reduces load on the server.
  * Can provide offline progress.

* **Cons**

  * Not reliable for critical tasks (user can clear storage, change devices, etc.).
  * Harder to coordinate across devices and sessions.

* **Consequence for Resumability**

  * Client-side state is excellent for **user convenience** (drafts, last position),
  * But **critical business workflows** should still be resumable based on server-side durable state.

#### 2.6 Design Guideline: System of Record vs. Cache

To keep your architecture clear, distinguish:

* **System of Record (SoR)**:

  * The one place that defines the “true” state of a resumable task.
  * Usually a database row/document for the task.
* **Caches / Derived State**:

  * Everything else that can be recomputed or repaired from the SoR:

    * In-memory structures,
    * Temporary files,
    * Queues containing “work items” derived from the task state.

A quick checklist for each piece of state:

1. **If it’s lost, can we recompute it from something else?**

   * Yes → cache / derived state.
   * No → put it in your SoR.

2. **If the process crashes halfway, what must we read to decide the next step?**

   * That must live in durable, queryable storage (DB, etc.).

By answering *“Where does state live?”* carefully for each subsystem, you create a solid foundation for all the other architectural decisions in this chapter: when to checkpoint, how to retry, how to scale, and how to operate the system.


### Section 3: Who Orchestrates Resumability?

Once you know **where** state lives and **when** to save progress, the next architectural question is:

> **Who is actually responsible for driving the workflow forward and resuming it after interruptions?**

In other words: *who* looks at the current state, decides the next step, and executes it?

Different architectures answer this question differently. In resumable systems, being explicit about “who orchestrates” is critical for clarity, debuggability, and failure handling.

#### 3.1 Controller-Driven Orchestration (Local MVC + FSM)

In many of the examples in this book, the **Controller + FSM** is the main orchestrator:

* The **Controller**:

  * Knows the *current* state (from the Model / DB).
  * Chooses the next transition (`to_recieving`, `to_merged`, `to_resize_stage`, `to_complete_mp4`, etc.).
  * Performs the **hard operations** (I/O, S3 calls, video encoding).
* The **FSM**:

  * Restricts what transitions are legal.
  * Encodes the process logic as a transition graph.
  * Provides helpers like `find_path(...)` or `resume_state(...)` to move toward a target state.

**Characteristics:**

* Orchestration is **local** to the service or process.
* Easy to reason about in code:

  * “Given state X and target Y, call the controller; it will figure out the next step.”
* Great for:

  * Single-service flows,
  * Background workers,
  * Simple APIs that “do the next step” on each call (like `/start_upload/` and `/upload_chunk/`).

**Trade-offs:**

* If logic spans multiple services, each service needs its own FSM, or you end up with one “God-controller” service.
* For very large workflows, you may want a more visible, centralized orchestration layer.

#### 3.2 Client-Driven Orchestration (Browser / Mobile / External Caller)

Sometimes the **client** plays an active orchestration role:

* The browser or mobile app:

  * Knows it must:

    1. `/start_upload/`
    2. Loop `/upload_chunk/` until completion
    3. Poll for final status
  * Decides when to pause, resume, or cancel based on user actions.
* A command-line tool or external script:

  * Repeatedly calls your API,
  * Inspects the current state,
  * Decides the next call.

In this style, the server is more like a **stateful engine** with simple APIs:

* “Do one step and tell me the new state.”
* “Give me the current state of task X.”

The **client orchestrates**, the **server enforces** correctness and persistence.

**Pros:**

* Very flexible: different clients can orchestrate the same backend in different ways.
* Great for interactive UX (pause/resume buttons, progress bars).

**Cons:**

* If client logic is wrong, you get strange usage patterns or stuck flows.
* If multiple clients can touch the same task, you’ll need extra safeguards (locking, ownership checks).

#### 3.3 Central Orchestrator Services (Workflow Engines)

In more complex systems, especially microservice architectures, you might introduce a dedicated **orchestrator**:

* Workflow engines like:

  * “Job runners”, “pipeline engines”, or external tools (e.g., Airflow-like, Step Functions-like concepts).
* The orchestrator:

  * Stores the **global workflow definition** (steps, branches, timeouts).
  * Keeps track of **per-task state**.
  * Calls into individual services to perform steps (“send email”, “charge card”, “generate thumbnail”).
  * Decides what to do on failure (retry, compensation, mark as failed).

Here, *who orchestrates* is:

* A **separate service** whose only job is to manage long-running workflows.

**Pros:**

* Good visibility: a single place to inspect the progress of all workflows.
* Easier cross-service coordination (Sagas, compensating actions).
* Each individual service can stay simpler: “do step X when asked” and report success/failure.

**Cons:**

* Another component to design, maintain, secure, and scale.
* Tight coupling between orchestrator and services if not designed carefully (e.g., hard-coded step names or payload formats).

#### 3.4 Autonomous Services (Choreography Instead of Orchestration)

The opposite of a central orchestrator is a **choreographed** system:

* There is **no single “boss”**.
* Each service:

  * Listens to events,
  * Updates its own state,
  * Emits new events when it finishes something.
* The whole workflow emerges from:

  * “When event A happens and my state is S, I emit B,”
  * “When I see B and my state is T, I emit C,” etc.

Resumability here depends heavily on:

* **Per-service FSMs** and their persisted state,
* **Event logs** and idempotent event handlers.

**Pros:**

* Very decoupled, services know as little as possible about each other.
* Easy to add new reactions by adding new consumers.

**Cons:**

* It’s harder to answer “What is the current global state of workflow #123?” unless you build special aggregators.
* Debugging and reasoning about end-to-end behavior can be complex.

In this architecture, “who orchestrates?” is answered with:

> “No one; the system as a whole choreographs itself via events.”

#### 3.5 Design Guideline: Make “Who Drives the Next Step?” Explicit

Regardless of style, a resilient resumable architecture should be able to answer clearly:

* **Who** decides what the next step is?
* **Where** is that decision encoded? (Controller code? Workflow engine? Client?)
* **How** is that component restarted or scaled?
* **What happens** if that orchestrator crashes in the middle of a decision?

A simple rule of thumb:

1. Pick **one primary orchestrator** per workflow:

   * Controller FSM, client app, workflow engine, or event choreography.
2. Make orchestration behavior **visible in code**:

   * Explicit FSM transitions,
   * Clear API contracts,
   * Centralized workflow definition where appropriate.
3. Ensure the orchestrator itself is **restartable and stateless**:

   * All real state must live in durable storage (Chapter 10, Section 1),
   * The orchestrator only *reads state, decides, and writes back*.

Once you know **who orchestrates resumability**, you can reason about how failures are handled, how to test complex flows, and where to add new behaviors without turning the system into a ball of mud.


### Section 4: What Patterns Keep Retries Safe?

Once you start making things resumable, you almost always end up adding **retries**:

* The network is flaky → retry the HTTP call.
* S3 upload fails mid-chunk → retry the upload.
* Video conversion crashes → re-run the step.

But naive retries can be dangerous:

* Double-charging a customer,
* Uploading the same chunk twice and corrupting the merge,
* Writing duplicate rows or emitting duplicate events.

So the architectural question becomes:

> **What patterns allow us to retry safely without breaking correctness?**

This section introduces a small toolbox of patterns you can apply on top of your MVC + FSM designs to make “retry until success” compatible with correctness and resumability.


#### 4.1 Idempotent Operations

**Idempotent** means:

> Running the same operation once or multiple times produces the **same final state**.

For example:

* “Set `task.state = 'completed'`” is idempotent.
* “Insert new row into `payments` table” is *not* idempotent if you call it twice.

In resumable systems, you often design your “steps” (FSM transitions) to be idempotent:

* In the S3 upload example:

  * Instead of “append some unknown chunk”, you do:

    * “Upload **part number N** for file `file_id`”
    * State is tracked per `(file_id, part_number)`.
* In the video conversion example:

  * Instead of “process some frames again and again”:

    * You track `converted_count`.
    * Each call processes *from* `converted_count` onward.

**Typical idempotency techniques:**

1. **Use natural or composite keys**
   Example: `(file_name, file_size, file_hash)` as a unique ID for the upload task.
   Calling “create upload” twice with the same triple returns the same record, not two.

2. **Upsert instead of insert**

   * “Insert, or update if already exists.”
   * In SQL: `INSERT ... ON CONFLICT (...) DO UPDATE ...`
   * In NoSQL: `update_one(..., upsert=True)`

3. **Set vs increment**

   * Prefer operations like:

     * `state = 'merged'`
     * `progress = max(progress, new_progress)`
   * Avoid blind increments when the same operation might run multiple times.

Architecture guideline:

> Design each FSM transition as a well-defined, *named* idempotent operation if possible.


#### 4.2 Idempotency Keys for External Requests

When external clients (browsers, mobile apps, other services) call your API, they might:

* Retry the same request due to network failure,
* Click the same button twice,
* Replay requests after a timeout.

To maintain resumability and correctness, you can introduce **idempotency keys**:

* Client generates a unique key per logical operation:

  * `X-Idempotency-Key: <uuid>`
  * Or a structured key like `upload:<user_id>:<file_hash>`.
* Server stores:

  * The key,
  * The resulting state / response.

On receiving the same idempotency key again:

* If the operation was already completed → return the **same result**.
* If it’s still running → return a “still processing” status or current state.

This pattern is especially important for:

* Payment APIs,
* “Create resource” endpoints,
* Any operation where double execution is unacceptable.


#### 4.3 Outbox and Inbox Patterns (for Events and Messages)

In distributed systems, resumability and retries often involve queues and events:

* You write to the DB,
* You send an event or a message to a queue,
* Either one can fail independently.

To avoid losing or duplicating events when you retry, you can use:

##### Outbox Pattern (Sender Side)

* When you update your main model (e.g. upload state, conversion state), you **also** write an “event” into an **outbox table/collection** in the same transaction:

  * Example: `upload_completed` event with `task_id`.
* A background worker:

  * Polls the outbox,
  * Sends events to Kafka/SQS/Webhooks,
  * Marks them as “sent”.

**Benefit:**
If your service crashes:

* The DB update and the outbox insert succeed or fail together.
* On restart, unsent events are still in the outbox, and you can safely resend.

##### Inbox / Processed-Event Log (Receiver Side)

* When a service consumes events, it keeps an **inbox table** or a list of processed event IDs.
* Before handling an event:

  * Check if you’ve already processed `event_id`.
  * If yes → skip (the event is a duplicate).
  * If no → process and record `event_id` as processed.

**Benefit:**
You can safely do **at-least-once delivery** but still process each event **exactly once** from a business-logic perspective.


#### 4.4 Sagas and Compensating Actions

Sometimes an operation spans multiple components:

* Reserve inventory,
* Charge payment,
* Generate invoice,
* Send confirmation email.

If step 3 fails after step 1 and 2 succeeded, how do you “resume” without leaving a mess?

This is where **Saga** and **compensating actions** help:

* A Saga is a long-running workflow split into multiple steps.
* Each step has:

  * A **forward action** (do something),
  * A **compensating action** (undo or logically reverse it).

Example:

* Forward:

  * `reserve_item(item_id)`
  * `charge_card(amount)`
* Compensating:

  * `release_item(item_id)`
  * `refund_card(amount)`

In a resumable architecture:

* If a Saga fails at step N:

  * You can resume by:

    * Either retrying step N (if safe),
    * Or triggering compensations for steps 1..N-1.
* The Saga’s state (including which steps are done, which compensations are pending) is persisted and resumable.

This pattern is especially useful in microservice architectures where:

* No single DB transaction spans all services,
* You still need a consistent *business* result after failures and retries.


#### 4.5 Timeouts, Backoff, and Circuit Breakers

Safe retries are not just about data correctness; they’re also about **protecting your system**.

Common patterns:

1. **Timeouts**

   * Don’t let a call hang forever; bound the time.
   * If a call times out, you may:

     * Retry,
     * Mark the state as “error” and wait for a manual or automatic resume.

2. **Exponential Backoff**

   * On repeated failures, wait longer between retries:

     * 1s, 2s, 4s, 8s, …
   * Reduces pressure on a struggling dependency.

3. **Circuit Breaker**

   * If a dependency keeps failing:

     * “Open” the circuit (stop calling it for a while).
     * Return fast errors or alternate behavior.
   * After a cooldown, try again and “close” if it recovers.

In terms of resumability:

* These patterns prevent your FSM from hammering failing resources.
* Your persisted state should capture:

  * Failure reason,
  * Next allowed retry time,
  * Number of attempts so far.


#### 4.6 Design Checklist: Is This Step Retry-Safe?

For each FSM transition or architectural step in your resumable system, ask:

1. **If this step is executed twice, what happens?**

   * Is it idempotent?
   * If not, can we make it idempotent with:

     * A natural key / idempotency key,
     * Upsert semantics,
     * A more explicit state representation?

2. **If the process crashes halfway through this step, what will we see in the persisted state?**

   * Can we detect partial changes?
   * Will we retry safely, or risk double effects?

3. **If messages/events are duplicated, can we detect and ignore duplicates?**

   * Outbox pattern used?
   * Inbox / processed log present?

4. **If external APIs fail or are slow, do we have:**

   * Timeouts and backoff,
   * Limits on the number of retries,
   * A way to surface “stuck in error” states to operators?

5. **Is the semantics of “success” clear?**

   * Do we have a well-defined terminal state (`merged`, `complete_mp4`, `failed`, `canceled`)?
   * Once we reach it, retries should be a no-op.

If you can answer these questions clearly for each major step, your architecture is not only resumable — it is also **retry-safe**, which is a fundamental requirement for real-world reliability.


### Section 5: Why Resumability Changes Your Design Priorities

Up to this point, we’ve asked **where** state lives, **when** to save progress, **who** orchestrates the flow, and **what** patterns keep retries safe. This section takes a step back and asks:

> **Why does caring about resumability fundamentally change the way we design systems?**

Resumability is not just a “nice-to-have reliability feature”. Once you take it seriously, it starts to reorder your priorities: how you model data, how you split services, how you treat failures, and even how you think about “done”.

#### 5.1 Why “Just Retry” Is Not Enough

Many systems start with a very simple reliability strategy:

> “If it fails, we’ll just retry.”

This works for:

* **Read-only** operations,
* Non-critical, idempotent actions,
* Small scripts and internal tools.

But as soon as you have:

* Payments, file uploads, long-running conversions,
* Multi-step flows (registration, onboarding, content pipelines),
* Expensive work (GPU jobs, video processing, ML training),

“Just retry” becomes dangerous:

* Retrying can **duplicate side effects** (double charge, double notification).
* Simple retries ignore **progress** (you always start from zero).
* They don’t answer: *“Where exactly did we stop?”*

Resumability forces you to move from:

* “Try again and hope it works this time”
  **to**
* “Pick up precisely from the last known consistent point.”

That shift requires architectural support: explicit FSMs, persisted models, idempotency, and careful state location.

#### 5.2 Why You Must Make State Explicit

In a non-resumable system, a lot of state is **implicit**:

* Hidden in local variables,
* Spread across in-memory objects,
* Implied by logs or queue contents.

This is often “good enough” until:

* The process crashes,
* You need to move workloads between machines,
* You have to explain to someone **what the system is doing right now**.

Resumability pushes you to:

* Put the **current state** of workflows in a **single, explicit form**:

  * A row or document describing the task,
  * A clear `state` field reflecting the FSM,
  * Additional fields like `progress`, `last_step`, `last_error`.

Why?

* Because **only explicit state can be safely recovered**.
* Because explicit state becomes a **contract** between:

  * Orchestrator and worker,
  * Frontend and backend,
  * Human operator and system.

It’s the difference between “somewhere in the code we know this” and “you can query the database and see exactly where we are”.

#### 5.3 Why User Experience Depends on Resumability

From the user’s perspective, resumability often looks like:

* “I can pause the upload and resume it later.”
* “If the browser crashes, my form / draft is still there.”
* “When I refresh the page, the video conversion shows progress, not zero.”

Modern users implicitly expect:

* **Continuity**: the system remembers them and their work.
* **Forgiveness**: network glitches and reloads are not fatal.
* **Transparency**: they can see what’s happening and what’s left.

Architecturally, this means:

* You treat workflows as **long-lived tasks**, not one-shot API calls.
* You persist both:

  * The *machine-visible* state (FSM),
  * And the *user-visible* status (percentage, step name, ETA-ish info).
* You design APIs and frontends in terms of:

  * “Create task → poll/subscribe → resume/cancel”,
    instead of “do everything immediately in one request”.

Resumability is therefore not just about backend safety; it is a direct driver of **better UX**.

#### 5.4 Why Operations and Compliance Care About Resumability

Resumable systems are also easier to **operate** and **audit**:

* Operators can:

  * See which tasks are stuck (`error` state),
  * Retry, cancel, or move them manually,
  * Inspect the history of transitions.
* Compliance and auditing are easier:

  * You can show **what happened when**, especially if you log state transitions.
  * You can demonstrate that:

    * No task was “lost” in the middle,
    * Failures were handled in controlled ways,
    * Certain steps (e.g., approvals, checks) were actually executed.

From an architectural perspective, this is why you:

* Treat **state transitions as first-class events** (sometimes even storing them as a history),
* Design FSMs and models so they can be inspected externally,
* Make it possible to **replay**, **compensate**, or **explain** the behavior of the system.

Resumability and observability naturally reinforce each other.

#### 5.5 Why Not Everything Should Be Fully Resumable

There is also an important negative lesson:

> You *could* make everything perfectly resumable — but you **shouldn’t**.

Full, fine-grained resumability has costs:

* More state to design, store, and migrate.
* More complex FSMs and controllers.
* More edge cases around partial progress.
* More clean-up tasks for old / abandoned state.

Some operations are cheap enough that restarting them from scratch is acceptable. For example:

* Quick, idempotent cache refresh jobs,
* Very small tasks that complete in milliseconds,
* Internal analytics jobs where partial loss is acceptable.

Architecturally, this leads to a pragmatic principle:

* **Make resumable what is:**

  * Expensive (time, money, CPU/GPU),
  * User-facing and long-running,
  * Critical to correctness (e.g., payments, external side effects).

* **Allow restart from scratch where:**

  * Work is cheap and quick,
  * Or the result is non-critical / best-effort.

Resumability is a **design choice**, not a dogma.
The “Why” here is about *prioritizing* where to invest complexity.

#### 5.6 Why Resumable Thinking Scales with System Complexity

As systems grow:

* More services,
* More steps,
* More failure modes,

Ad-hoc error handling and ad-hoc “retry here and there” logic becomes unmanageable.

By contrast, **resumable thinking** scales because it gives you:

* A uniform way to think about workflows:

  * FSM for states,
  * Durable SoR for task models,
  * Clear orchestrator roles,
  * Safe retry patterns.
* A common vocabulary for the team:

  * “What state is this task in?”
  * “Which transition failed?”
  * “Where is the checkpoint?”

This uniformity is exactly why mature systems (cloud platforms, payment gateways, large SaaS products) invest so heavily in resumability-oriented architectures.

In short, **why** you design for resumability is not just “to handle failures better”; it’s because:

* It improves **correctness**,
* It improves **user experience**,
* It improves **operability and auditability**,
* And it provides a **scalable mental model** for complex systems.

The rest of this chapter’s sections (and this book) are about giving you the concrete tools so that, once you decide *why* you care about resumability, you already know **how** to build it in.


### Section 5: How to Review an Architecture for Resumability (Checklist)

By this point, we have discussed:

* **Where** state lives,
* **When** to save progress,
* **Who** orchestrates the flow,
* **What** patterns keep retries safe,
* (And later: **Why** this all changes your priorities).

This section is about something very practical:

> **How can you systematically review (or design) a system to ensure it is truly resumable?**

To make this actionable, we provide a **checklist** you can apply to:

* A single feature (e.g., large file upload),
* A background job (e.g., video thumbnail conversion),
* Or a full cross-service workflow.

You don’t have to achieve “perfect” resumability everywhere, but you should be able to answer these questions consciously.

---

#### 5.1 How to Use This Checklist

1. Pick a **specific workflow or feature** (e.g., “S3 multipart upload”, “video conversion job”).
2. Identify its **start** and **end** states (what does “not started” and “done” mean?).
3. Go through each checklist group below:

   * If you can clearly answer “yes” → great.
   * If “no” or “not sure” → that’s a design gap to address.

You can treat this section as a **design review ritual**: run it for each major resumable feature before shipping.

---

#### 5.2 Checklist – Modeling & State

**[ ] 1. Do you have a single, explicit System of Record (SoR) for this workflow?**

* Example: a `S3LargeUploadingModel`, `VideoConversionModel`, or a `task` table row.
* This SoR should answer:

  * What is the task?
  * What is its current state?

**[ ] 2. Is the current state represented by a clear field (or FSM state) in the model?**

* e.g., `FSMs_state = 'idle' | 'recieving' | 'recieved' | 'merged'` or `state = 'resize_stage' | 'error' | 'complete_mp4'`.

**[ ] 3. Is all critical progress stored durably, not only in memory?**

* For uploads: which chunks are done (`parts` list).
* For conversion: how many frames are processed (`converted_count`).
* If the process dies, can you recompute everything from this stored state?

**[ ] 4. Is it clear what counts as a terminal state?**

* e.g., `merged`, `complete_mp4`, `failed`, `canceled`.
* Once the task is in a terminal state, further actions should be no-ops or clearly rejected.

---

#### 5.3 Checklist – Transitions, FSM, and Orchestration

**[ ] 5. Do you have an explicit set of allowed transitions (an FSM)?**

* e.g., `_transitions = { 'idle': ['recieving'], 'recieving': ['recieved', 'recieve_failure', 'idle'], ... }`.
* Illegal transitions should be blocked (e.g., via `validate_transition` / `handle_errors` decorators).

**[ ] 6. Is it clear *who* drives the next step?**

* Controller (`RequestFSMsController`, `S3LargeUploadingFSMsController`, `VideoConversionFSMsController`)?
* Client (browser / CLI)?
* Central workflow engine?
* Event choreography?
* You should be able to point to **one main orchestrator** per workflow.

**[ ] 7. Can the orchestrator be restarted without losing context?**

* All needed information must be in the SoR, not hidden in temporary variables.
* After restart, it should be able to read state and continue.

**[ ] 8. Do you have a way to “drive” the system toward a target state?**

* e.g., `find_path(...)` + `next_action(...)`, or `resume_state(target_state=...)`.
* This is the core of declarative resumability:

  * “Given current state and target, how do we step-by-step move there?”

---

#### 5.4 Checklist – Persistence, Idempotency, and Retries

**[ ] 9. Is each major step safe to retry?**

* If the same transition runs twice (by bug or retry), does the final result remain correct?
* If not, can you:

  * Use idempotency keys / unique constraints?
  * Change the operation from “do something” to “set state to X”?

**[ ] 10. Are hard operations (I/O, external APIs, DB writes) in controllers, not models?**

* Models should primarily hold data.
* Controllers / FSMs should own:

  * S3 calls,
  * File writes,
  * DB writes, etc.

**[ ] 11. Is checkpoint granularity intentional?**

* Do you know how much work might be redone after a crash?

  * For uploads: maybe 1 chunk.
  * For video: maybe a few frames.
* Is this amount acceptable in terms of time and cost?

**[ ] 12. Are errors captured as part of state?**

* e.g., a state like `recieve_failure`, `error`, or fields like `last_error`.
* After failure, the system can:

  * Retry,
  * Or present a clear status for human intervention.

---

#### 5.5 Checklist – Observability & Operations

**[ ] 13. Can operators see the current state and progress of a task?**

* e.g., via:

  * A DB query (admin console),
  * A `/status/<id>` API,
  * Logs that include `task_id` and `state`.

**[ ] 14. Can operators safely retry, cancel, or purge a task?**

* Is there a defined way to:

  * Move a task from `error` → `idle` (retry),
  * Mark it `canceled`,
  * Delete records and temporary files after completion?

**[ ] 15. Are logs and metrics connected to states?**

* Logs should mention:

  * Task ID,
  * Old state → new state,
  * Reason for transition.
* Metrics:

  * Count tasks in each state,
  * Time spent in each state,
  * Number of errors / retries.

---

#### 5.6 Checklist – Security, Cleanup, and Lifecycle

**[ ] 16. Is access to resumable state properly authorized?**

* Can one user/tenant only see and resume **their own** tasks?
* Are sensitive fields (file names, hashes, user info) protected?

**[ ] 17. Do you have a cleanup strategy?**

* What happens to:

  * Old upload records,
  * Old temporary files (`*.bin`),
  * Old conversion tasks,
  * Zombie tasks stuck in `error`?
* Is there:

  * Time-to-live (TTL) logic,
  * A background job,
  * Or manual tools?

**[ ] 18. Is the lifecycle clearly defined?**

* From `created` → `in progress` → `terminal state` → `archived/deleted`.
* Each step of the lifecycle should be:

  * Represented in your state model,
  * And supported by your code.

---

#### 5.7 How to Decide “Good Enough”

You do **not** need to check every box for every feature. Instead:

* For **critical, long-running, and expensive** workflows:

  * Aim to satisfy as many checklist items as possible.
* For **cheap, short, or low-risk** workflows:

  * You might accept:

    * Less detailed state,
    * Coarser checkpoints,
    * Simple “retry from scratch”.

The important part is:
You **consciously decide** where resumability matters, and you have a **systematic way** to check that your architecture actually supports it.

This checklist should give you a concrete “How”:

* How to review a design,
* How to refine an existing system,
* How to ensure that your use of MVC, FSMs, and storage backends really results in a resilient, resumable architecture—not just in theory, but in running, maintainable code.




---
## Conclusion (of this Book)

Throughout this book, we have explored a simple but powerful idea: **a program should not have to lose all its progress simply because its execution is interrupted**. What began with a small Python example gradually became a way of thinking about state, software architecture, error recovery, and long-running workflows.

Resumable programming is not a single library, algorithm, or framework. It is a design approach that asks us to make progress visible, preserve the information required for recovery, and define what should happen when something goes wrong.

### Recap of Key Points

Let us revisit the most important lessons from our journey:

- **Start with the meaning of resumability.** In Chapter 2, the Fibonacci example introduced persistent results, while `MachineA` demonstrated two ways to recover progress: saving the machine's current state and recording completed actions for later replay. Both approaches teach us to identify what must survive an interruption. They also reveal different trade-offs in storage, replay cost, and recovery complexity.

- **Treat persistent state as a foundation.** Chapter 3 compared SQL and key-value databases. SQL systems, including SQLite, provide transactions and structured records; key-value approaches, such as Python's `shelve` and MongoDB-based storage, offer flexible ways to persist task data. The right choice depends on the data model, consistency requirements, recovery needs, and operational environment. No database can make an unsafe external action automatically safe to repeat.

- **Separate responsibilities with MVC.** Chapter 4 showed how the Model-View-Controller pattern helps organize a resumable application. The model represents the task and its data, the controller coordinates operations, and the view presents information to users. Clear responsibilities make state easier to save, restore, inspect, and test.

- **Make progress explicit with Finite State Machines.** Chapter 5 introduced states, transitions, and valid paths between them. Chapter 6 combined FSMs with MVC to build more advanced resumable controllers. Instead of relying on an invisible sequence of function calls, a state machine lets us ask: *Where is the task now, which transitions are allowed, and what must happen next?*

- **Choose checkpoints that represent completed work.** Chapter 7 applied these ideas to a large-file uploading service, video conversion, and AI object detection and segmentation. For an upload, progress may mean successfully stored parts; for video and AI processing, it may mean completed frames. The checkpoint must describe meaningful, recoverable progress, not merely the line of code the program reached.

- **Prove recovery through testing.** Chapter 8 demonstrated that resumability must be verified rather than assumed. Testing state transitions, persistent restoration, intentional crashes, randomized failures, and invariants helps answer the essential question: *Can a fresh process continue correctly after the old one disappears?*

- **Design the entire system for safe recovery.** Chapter 9 connected code-level techniques to architecture. It examined checkpoint frequency, the system of record, orchestration, idempotent operations, retries, timeouts, outbox/inbox patterns, compensating actions, observability, and operational concerns. A successful retry is not simply an operation that runs again; it is one that continues without producing an incorrect duplicate effect.

These lessons can be summarized as a recurring process:

```text
Understand the task
       |
       v
Define states and meaningful checkpoints
       |
       v
Perform a step and confirm its outcome
       |
       v
Persist completed progress
       |
       v
Continue the workflow
       |
       +---- interruption ----> Restore saved progress
                                      |
                                      v
                              Recover or safely retry
                                      |
                                      +----> Continue
```

The details vary from one application to another, but the central question stays the same:

> **What work has already been completed successfully, and what information do we need to continue safely?**

### Encouragement to Experiment

Reading about resumability is an important first step. The next step is to experience it in your own programs.

Begin with something small. Take a Python script that processes a list of files, downloads data, or performs a sequence of calculations. Add a persistent progress record. Stop the program halfway through, start it again, and verify that it continues from the correct point. You do not need a distributed system or a complex framework to learn the essential ideas.

Then make the experiment more demanding. Introduce random failures, restart the process at different transitions, corrupt a temporary output, or simulate an unavailable external service. Observe what happens to the saved state. Ask whether an operation is repeated, whether the result remains correct, and whether the system can explain its own progress.

Once a simple example works, try the MVC and FSM approach developed in this book. Represent the task using a model, define its valid transitions, and use a controller to move toward the desired state. Experiment with SQLite and key-value storage, compare checkpoint frequencies, and measure the amount of work that must be repeated after a failure.

An especially useful exercise is to test the difficult moment between **performing an external action** and **recording its success**. A crash at that moment may leave the program uncertain whether the action completed. Explore idempotency keys, result verification, or compensating actions rather than assuming a blind retry is harmless.

Not every experiment will succeed on the first attempt, and that is valuable. A failure discovered during testing is an opportunity to improve the recovery design before users depend on it. Start with one meaningful checkpoint, make recovery observable, and refine the system as its requirements grow.

### Looking Forward

As software increasingly relies on cloud services, distributed components, autonomous devices, and computationally expensive AI workloads, the need to preserve progress across interruptions is likely to grow.

We can expect several directions to become especially important. Workflow engines may make durable execution and state transitions easier to express. Development tools may help generate state diagrams, identify missing recovery paths, and test failure scenarios automatically. Better observability may allow developers and operators to inspect not only whether a task has failed, but also exactly what has been completed and which recovery action is appropriate.

AI and machine-learning workloads provide another compelling area for resumability. Long-running data preparation, video analysis, inference pipelines, and model-related processing can involve substantial CPU, GPU, storage, and network resources. Recovering completed units of work can reduce unnecessary recomputation, although correctness still depends on well-defined outputs, repeatable operations where required, and durable progress records.

A further possibility is **adaptive recovery**: systems that use execution history, failure patterns, and workload costs to choose checkpoint intervals or recovery strategies. Such systems may become more efficient, but intelligent decision-making cannot replace the basic requirement for reliable state. A system must still know what has actually succeeded.

The technologies will change. New databases, orchestration frameworks, programming languages, and deployment environments will appear. Yet the core principles explored in this book—explicit state, durable progress, safe transitions, controlled retries, and verifiable recovery—are likely to remain useful across those changes.

### Final Thoughts

At the beginning of this book, we looked at programs that performed useful work but could lose their progress when execution was interrupted. By the end, we have a different perspective: an interruption is not necessarily the end of a task. With the right design, it can be an event the system recognizes, records, and recovers from.

This does not mean every application must be fully resumable. Saving state introduces storage costs, additional logic, maintenance responsibilities, and new failure cases. For a short, inexpensive operation, starting over may be the simplest and most reasonable choice. For a costly, long-running, user-facing, or correctness-critical workflow, however, resumability can fundamentally change the reliability and experience of the system.

The goal is not to build software that never fails. The goal is to build software that **can fail without unnecessarily losing completed work, and can recover without compromising correctness**.

Perhaps the most important change is therefore a change in mindset. Instead of asking only, *How do I make this task run?*, ask:

*How will this task continue if the process, the machine, or the network disappears halfway through?*

When that question becomes part of the design process, resumability is no longer an afterthought. It becomes a natural property of the software we build.

## Closing

Thank you for reading *Resumable Programming* and for exploring its concepts, examples, and design patterns with us.

We hope this book has provided not only practical techniques for saving state and recovering tasks, but also a useful way to think about reliability in everyday software development. Whether your next project is a small Python script, a file-processing service, an AI pipeline, or a large distributed application, we encourage you to begin with a simple question: *What should happen if this task is interrupted?*

Keep experimenting, testing, and refining your designs. Every carefully chosen checkpoint and every recovery path you verify is a step toward software that is more dependable, maintainable, and useful to the people who rely on it.

**Thank you, and happy coding!**

