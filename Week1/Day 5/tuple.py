# A tuple in Python is an immutable ordered collection of elements.

# Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
# Tuples can hold elements of different data types.
# The main characteristics of tuples are being ordered, heterogeneous and immutable.

tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)

tup=("geeks") # treated as string
print(type(tup))

tup=("Geeks",) # treated as tuple
print(type(tup))

tup = (5, 'Welcome', 7, 'Geeks')
print(tup)

# Creating a Tuple with nested tuples
tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)
print(tup3)

# Creating a Tuple with repetition
tup1 = ('Geeks',) * 3
print(tup1)

# Creating a Tuple with the use of loop
tup = ('Geeks')
n = 5
for i in range(int(n)):
    tup = (tup,)
    print(tup)

# Accessing Tuple with Indexing
tup = tuple("Geeks")
print(tup[0])

# Accessing a range of elements using slicing
print(tup[1:4])  
print(tup[:3])

# Tuple unpacking
tup = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)

# Concatenation of tuples
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')

tup3 = tup1 + tup2
print(tup3)

# Slicing

tup = tuple('GEEKSFORGEEKS')

# Removing First element
print(tup[1:])

# Reversing the Tuple
print(tup[::-1])

# Printing elements of a Range
print(tup[4:9])

# Deletion

#tup = (0, 1, 2, 3, 4)
#del tup

#print(tup)

# Unpacking with * Asterisk 

tup = (1, 2, 3, 4, 5)

a, *b, c = tup

print(a) 
print(b) 
print(c)

ytup=tuple((x for x in range(1,4)))
print(ytup)
# ytup.append(5)  # This will raise an AttributeError since tuples are immutable

print(type(ytup))