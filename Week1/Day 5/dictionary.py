# Python Dictionary

# A Python dictionary is a data structure that stores data in key-value pairs, where each key is unique and is used to retrieve its associated value. It is mainly used when you want to store and access data by a name (key) instead of by position like in a list.

#  Example: This example shows how a dictionary stores data using keys and values.

data = { "name": "Jake", "age": 22 }
print(data)

d1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d1)

# using dict() constructor
d2 = dict(a = "Geeks", b = "for", c = "Geeks")
print(d2)

d = { "name": "Kat", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 22

# Updating an existing value
d[1] = "Python dict"
print(d)

d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del 
del d["age"]
print(d)

# Using pop() 
val = d.pop(1)
print(val)

# Using popitem()
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Using clear()
d.clear()
print(d)

d = {1: 'Geeks', 2: 'For', 'age':22}
print("age" in d)

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")

    

