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