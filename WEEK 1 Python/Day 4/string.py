s1 = 'GfG'  
s2 = "GfG"  
print(s1)
print(s2)

s = "GeeksforGeeks"
print(s[0])   
print(s[4])

s = "GeeksforGeeks"
print(s[-10])  
print(s[-5]) # Accessing with negative indexes 

# STRING SLICING

s = "GeeksforGeeks"
print(s[1:4])    
print(s[:3])     
print(s[3:])    # Triming
# Reverse String 
print(s[::-1])   

s = "Python"
for char in s:
    print(char)

s = "geeksforGeeks"
s = "G" + s[1:]   # Strings are immutable 
print(s)

s = "GfG"
del s

s = "hello geeks"
s1 = "H" + s[1:]                  
s2 = s.replace("geeks", "GeeksforGeeks")  
print(s1)
print(s2)  # This creates new string as strings are immutable 


s = "GeeksforGeeks"
print(len(s))

s = "Hello World"
print(s.upper())    # UpperCase
print(s.lower())  # Lowercase

s = "   Gfg   "
print(s.strip())    # remove leading and trailing whitespaces

s = "Python is fun"
print(s.replace("fun", "awesome"))

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

s = "Hello " 
print(s * 3)

name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")

s = "My name is {} and I am {} years old.".format("Alice", 22) 
print(s)

s = "GeeksforGeeks" 
print("Geeks" in s) 
print("GfG" in s)    # String membership 