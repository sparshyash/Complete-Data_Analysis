def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator # Applying the decorator to a function
def greet():
    print("Hello, World!")

greet() # This will call the wrapper function created by the decorator

def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a, b):
    return a + b

print(add(5,3))

# Assigning a function to a variable
def greet(n):
    return f"Hello, {n}!"
say_hi = greet  # Assign the greet function to say_hi
print(say_hi("Alex")) 

# Passing a function as an argument
def apply(f, v):
    return f(v)
res = apply(say_hi, "Elon")
print(res) 

# Returning a function from another function
def make_mult(f):
    def mult(x):# The inner function "remembers" the value of f even after make_mult has finished running. This is called a Closure.
        
        return x * f
    return mult
dbl = make_mult(2)
print(dbl(5))


# Higher Order functions are functions that can take other functions as arguments or return them as results. They are a powerful feature in Python that allows for more flexible and reusable code.
def fun(f, x):
    return f(x)
# Known as closure 
def square(x):
    return x * x
res = fun(square, 5)
print(res)

# TYPES OF DECORATORS 

# 1.  Function decorators  used to wrap and enhance functions by adding extra behavior before or after the original function runs.

def simple_decorator(func):
    def wrapper():
        print(">>> Starting function")
        func()
        print(">>> Function finished")
    return wrapper

@simple_decorator
def greet():
    print("Hello, World!")
greet()

#  simple_decorator(func): This decorator takes the function greet as an argument (func) and returns a new function (wrapper) that adds some functionality before and after calling original function.
#  @simple_decorator: This is the decorator syntax. It applies simple_decorator to greet function.
#  Calling greet(): When greet() is called, it doesn't just execute original function but first runs added behavior from wrapper function.

# 2. Method Decorators : Special decorators used for methods inside a class. They work like function decorators but handle the self parameter for instance methods.
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")
obj = MyClass()
obj.say_hello()

# method_decorator(func): The decorator takes method (say_hello) as an argument (func). It returns a wrapper function that adds behavior before and after calling original method.
#wrapper(self, *args, **kwargs): wrapper must accept self because it is a method of an instance. self is instance of class and *args and **kwargs allow for other arguments to be passed if needed.
#@method_decorator: This applies method_decorator to say_hello method of MyClass.
# Calling obj.say_hello(): say_hello method is now wrapped with additional behavior.

# Example: Here, a decorator prints a message before and after a method is executed, while correctly handling self argument.


def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")
obj = MyClass()
obj.say_hello()

# method_decorator(func): The decorator takes method (say_hello) as an argument (func). It returns a wrapper function that adds behavior before and after calling original method.
# wrapper(self, *args, **kwargs): wrapper must accept self because it is a method of an instance. self is instance of class and *args and **kwargs allow for other arguments to be passed if needed.
# @method_decorator: This applies method_decorator to say_hello method of MyClass.
# Calling obj.say_hello(): say_hello method is now wrapped with additional behavior.

# 3. Class Decorators: used to modify or enhance behavior of a class. Like function decorators, class decorators are applied to class definition. They work by taking class as an argument and returning a modified version of class.

# Example: This code demonstrates a class decorator that adds a class_name attribute to a class, storing class’s name.

def fun(cls):
    cls.class_name = cls.__name__
    return cls

@fun
class Person:
    pass
print(Person.class_name)

fun(cls)
    
# This decorator adds a new attribute, class_name, to class cls. The value of class_name is set to the name of class (cls.__name__).
# @add_class_name: This applies the add_class_name decorator to the Person class.


# Built In Decorators 

# 1. @staticmethod: used to define a method that doesn't operate on an instance of class (i.e., it doesn't use self). Static methods are called on class itself, not on an instance of class.

# Example: This example shows how to define and use a @staticmethod inside a class.

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

# Using the static method
res = MathOperations.add(5, 3)
print(res)

# Explanation:

# add is a static method defined with @staticmethod decorator.
# It can be called directly on class MathOperations without creating an instance.

# 2. @classmethod: used to define a method that operates on class itself (i.e., it uses cls). Class methods can access and modify class state that applies across all instances of class.

# Example: This code defines a class Employee with a class variable raise_amount and a class method set_raise_amount that updates this variable for entire class.


class Employee:
    raise_amount = 1.05
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# Using the class method
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)

# set_raise_amount is a class method defined with @classmethod decorator.
# It can modify class variable raise_amount for class Employee and all its instances.

# 3. @property: used to define a method as a property, which allows to access it like an attribute. This is useful for encapsulating implementation of a method while still providing a simple interface.

# Example: This code defines a circle class demonstrating @property for controlled attribute access, allowing safe updates to radius.
import math
class Circle:
    def __init__(self, radius):
        self._radius = radius  # underscore matlab protected hai, direct access nahi karna chahiye, isliye _radius use kiya hai.

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

    @property
    def area(self):
        return math.pi * (self._radius ** 2)

c = Circle(5)
print(c.radius) 
print(c.area)    
c.radius = 10
print(c.area)

## CHaining Multiple Decorators 


