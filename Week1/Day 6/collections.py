# The collections module in Python provides specialized containers (different from general purpose built-in containers like dict, list, tuple and set). These specialized containers are designed to address specific programming needs efficiently and offer additional functionalities.

# Counters
# A counter is a sub-class of the dictionary. It is used to keep the count of the elements in an iterable in the form of an unordered dictionary where the key represents element in the iterable and value represents the count of that element in the iterable.


from collections import Counter 
  
# Creating Counter from a list (sequence of items)  
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
  
# Creating Counter from a dictionary
print(Counter({'A':3, 'B':5, 'C':2}))
  
# Creating Counter using keyword arguments
print(Counter(A=3, B=5, C=2))

from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = Counter(data)

# Retrieve the top 2 most common elements
print(counts.most_common(2)) 
# Output: [('apple', 3), ('banana', 2)]

from collections import Counter

# Initial counts
c = Counter(a=4, b=2, c=0)
d = Counter(a=1, b=2, c=3, d=1)

# Apply subtract
c.subtract(d)

print(c)
# Output: Counter({'a': 3, 'b': 0, 'c': -3, 'd': -1})

# OrderedDict
# An OrderedDict is a dictionary that preserves the order in which keys are inserted. While regular dictionaries do this from Python 3.7+, OrderedDict also offers extra features like moving re-inserted keys to the end making it useful for order-sensitive operation

from collections import OrderedDict 
print("This is a Dict:\n") 
d = {} 
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
  
for key, value in d.items(): 
    print(key, value) 
  
print("\nThis is an Ordered Dict:\n") 
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
for key, value in od.items(): 
    print(key, value)


from collections import OrderedDict 
od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
print('Before Deleting')
for key, value in od.items(): 
    print(key, value) 
    
# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items(): 
    print(key, value)

# DefaultDict
# A DefaultDict is also a sub-class to dictionary. It is used to provide some default values for the key that does not exist and never raises a KeyError.

from collections import defaultdict 

# Creating a defaultdict with default value of 0 (int)
d = defaultdict(int) 
L = [1, 2, 3, 4, 2, 4, 1, 2] 

# Counting occurrences of each element in the list
for i in L: 
    d[i] += 1  # No need to check key existence; default is 0

print(d)

# ChainMap
#  A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.

from collections import ChainMap 
   
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap 
c = ChainMap(d1, d2, d3) 
print(c)

#  Accessing Keys and Values from ChainMap
#  Values from ChainMap can be accessed using the key name. They can also be accessed by using the keys() and values() method.

# Adding New Dictionary using new_child() method

import collections 
  
# initializing dictionaries 
dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'b' : 3, 'c' : 4 } 
dic3 = { 'f' : 5 } 
  
# initializing ChainMap 
chain = collections.ChainMap(dic1, dic2) 
  
# printing chainMap 
print ("All the ChainMap contents are: ") 
print (chain) 
  
# using new_child() to add new dictionary 
chain1 = chain.new_child(dic3) 
  
# printing chainMap
print ("Displaying new ChainMap : ") 
print (chain1)

#   NamedTuple a normal tuple but with namedFIlrds index ke jagah pe aap sidha name use kr skte ho filed ka 

from collections import namedtuple
  
# Declaring namedtuple() 
Student = namedtuple('Student',['name','age','DOB']) 
  
# Adding values 
S = Student('Nandini','19','2541997') 
  
# Access using index 
print ("The Student age using index is : ",end ="") 
print (S[1]) 
  
# Access using name  
print ("The Student name using keyname is : ",end ="") 
print (S.name)
print(S.age)

from collections import namedtuple
  
# Declaring namedtuple() 
Student = namedtuple('Student',['name','age','DOB']) 
  
# Adding values 
S = Student('Nandini','19','2541997') 
  
# initializing iterable  
li = ['Manjeet', '19', '411997' ] 
  
# initializing dict 
di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' } 
  
# using _make() to return namedtuple() 
print ("The namedtuple instance using iterable is  : ") 
print (Student._make(li))   # Iterable to NamedTuple
  
# using _asdict() to return an OrderedDict() 
print ("The OrderedDict instance using namedtuple is  : ") 
print (S._asdict())   # NmaedTuple converted to OrdderedDict

#  DEQUE
## Deque (Doubly Ended Queue) is the optimized list for quicker append and pop operations from both sides of the container. It provides O(1) time complexity for append and pop operations as compared to list with O(n) time complexity.

from collections import deque
  
# Declaring deque
queue = deque(['name','age','DOB']) 
print(queue)

# Inserting Elements in a deque

from collections import deque 
  
# Initializing deque with initial values
de = deque([1, 2, 3]) 
  
# Append 4 to the right end of deque
de.append(4) 
  
# Print deque after appending to the right
print("The deque after appending at right is :") 
print(de) 
  
# Append 6 to the left end of deque
de.appendleft(6) 
  
# Print deque after appending to the left
print("The deque after appending at left is :") 
print(de)

# Deleting Elements 

from collections import deque

# Initialize deque with initial values
de = deque([6, 1, 2, 3, 4])

# Delete element from the right end (removes 4)
de.pop()

# Print deque after deletion from the right
print("The deque after deleting from right is :") 
print(de)

# Delete element from the left end (removes 6)
de.popleft()

# Print deque after deletion from the left
print("The deque after deleting from left is :") 
print(de)

# USERDICT
# UserDict is a dictionary-like container that acts as a wrapper around the dictionary objects. This container is used when someone wants to create their own dictionary with some modified or new functionality. 

from collections import UserDict 

# Creating a dictionary where deletion is not allowed
class MyDict(UserDict): 
      
    # Prevents using 'del' on dictionary
    def __del__(self): 
        raise RuntimeError("Deletion not allowed") 
          
    # Prevents using pop() on dictionary
    def pop(self, s=None): 
        raise RuntimeError("Deletion not allowed") 
          
    # Prevents using popitem() on dictionary
    def popitem(self, s=None): 
        raise RuntimeError("Deletion not allowed") 
      
# Create an instance of MyDict
d = MyDict({'a': 1, 'b': 2, 'c': 3})
# d.pop(1)  this creates traceback error 

# USERLIST

# UserList is a list like container that acts as a wrapper around the list objects. This is useful when someone wants to create their own list with some modified or additional functionality.

from collections import UserList 

# Creating a list where deletion is not allowed
class MyList(UserList): 
      
    # Prevents using remove() on list
    def remove(self, s=None): 
        raise RuntimeError("Deletion not allowed") 
          
    # Prevents using pop() on list
    def pop(self, s=None): 
        raise RuntimeError("Deletion not allowed") 
      
# Create an instance of MyList
L = MyList([1, 2, 3, 4]) 
print("Original List") 

# Append 5 to the list
L.append(5) 
print("After Insertion") 
print(L) 
# Attempt to remove an item (will raise error)
#  L.remove()  this creates error 

# UserString 

# UserString is a string like container and just like UserDict and UserList it acts as a wrapper around string objects. It is used when someone wants to create their own strings with some modified or additional functionality. 

from collections import UserString 
   
# Creating a Mutable String 
class Mystring(UserString): 
      
    # Function to append to string
    def append(self, s): 
        self.data += s 
          
    # Function to remove from string 
    def remove(self, s): 
        self.data = self.data.replace(s, "") 
      
# Driver's code 
s1 = Mystring("Geeks") 
print("Original String:", s1.data) 
  
# Appending to string 
s1.append("s") 
print("String After Appending:", s1.data) 
  
# Removing from string 
s1.remove("e") 
print("String after Removing:", s1.data)


