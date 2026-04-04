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
print (S._asdict())   # OrderedDict to NamedTuple 