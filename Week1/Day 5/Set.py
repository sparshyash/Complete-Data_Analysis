# A Set in Python is used to store a collection of items with the following properties.

#  duplicate elements. If try to insert the same item again, it overwrites previous one.
#  unordered collection. When we access all items, they are accessed without any specific order and we cannot access items using indexes as we do in lists.
# ternally use hashing that makes set efficient for search, insert and delete operations. It gives a major advantage over a list for problems with these operations.
# table, meaning we can add or remove elements after their creation, the individual elements within the set cannot be changed directly.

s = {10, 50, 20}
print(s)
print(type(s))


# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding element to the set
s.add("d")
print(s)

# a set cannot have duplicate values
s = {"Geeks", "for", "Geeks"}
print(s)

# values of a set cannot be changed
# s[1] = "Hello"
# print(s)

s = {"Geeks", "for", 10, 52.7, True}
print(s)

# Normal set (mutable)
s = set(["a", "b", "c"])
print("Normal Set:", s)

# Frozen set (immutable)
fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs)


s = {"a", "b", "c"}
s.add("d")
print(s)

a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
print(u)


a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(i)

a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d)

