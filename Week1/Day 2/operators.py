# ARithmetic 

# Variables
a = 15
b = 4

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)

# COmparison Operators 

a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Logical Operators 

a = True
b = False
print(a and b)
print(a or b)
print(not a)

# Bitwise Operators 

a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print("a XOR b:", a ^ b)  # XOR  different pe 1 , same pe 0
print("a RIGHT SHIFT 2:", a >> 2)  # RIGHT SHIFT DIVIDE BY 2^2
print("a LEFT SHIFT 2:", a << 2)  # LEFT SHIFT MUTIPLY BY 2^2

# Assignment Operator 

a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

# Identify operators 

a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# Membership

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
# Ternary 

a, b = 10, 20
min = a if a < b else b

print(min)

# Precendence and Associativity

expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2: # L to R
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

print(100 / 10 * 10) 
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)   # R to L


