# Comprehensions in Python provide a short and clear way to create new sequences from existing iterables.

# Improve readability by replacing long loops with a single statement.
# Encourage modular and clean coding practices.
# Commonly used in data processing, web development, and automation tasks.
# Reduce errors by minimizing lines of code.
# Work well with functions like zip(), enumerate(), map(), and lambda.

# 1. List Comprehensions
#  List comprehensions allow for the creation of lists in a single line, improving efficiency and readability. They follow a specific pattern to transform or filter data from an existing iterable.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = [num for num in a if num % 2 == 0]
print(res)

res = [num**2 for num in range(1, 6)]
print(res)

# 2. Dictionary comprehension
# Dictionary Comprehensions are used to construct dictionaries in a compact form, making it easy to generate key-value pairs dynamically based on an iterable.

res = {num: num**3 for num in range(1, 6)}
print(res)

a = ["Texas", "California", "Florida"] # states
b = ["Austin", "Sacramento", "Tallahassee"] # capital

res = {state: capital for state, capital in zip(a, b)}
print(res)

# 3. Set comprehensions
#  Set Comprehensions are similar to list comprehensions but result in sets, "automatically" eliminating duplicate values while maintaining a concise syntax.

a = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

res = {num for num in a if num % 2 == 0}
print(res)

# 3. Generator comprehensions
# Generator Comprehensions create iterators that generate values lazily, making them memory-efficient as elements are computed only when accessed.

res = (num for num in range(10) if num % 2 == 0)
print(list(res))

res = (num**2 for num in range(1, 6))
print(tuple(res))



