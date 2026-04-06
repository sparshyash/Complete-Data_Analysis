def fun():
    print("Welcome to GFG")

def myFun(x, y=50): # default args
    print("x: ", x)
    print("y: ", y)

myFun(10)  

def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks') # Keyword args

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Suraj", 27)

print("\nCase-2:")
nameAge(27, "Suraj") # position args

def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')  

# In Python Arbitrary Keyword Arguments, *args and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:

# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)
# This code separately shows non-keyword (*args) and keyword (**kwargs) arguments in the same function.


# Anonymous functions 

def cube(x): return x*x*x   # without lambda
cube_l = lambda x : x*x*x  # with lambda

print(cube(7))
print(cube_l(7))

#  Pass by Reference and Pass by Value
# In Python, variables are references to objects. When we pass them to a function, the behavior depends on whether the object is mutable (like lists, dictionaries) or immutable (like integers, strings, tuples).

# Mutable objects: Changes inside the function affect the original object.
# Immutable objects: The original value remains unchanged.

def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))