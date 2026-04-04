class Dog:
    species = "Canine"  # Class attribute species is shared bya all instances of Dog class

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

    # Creating an object of the Dog class
dog1 = Dog("Buddy", 3)

print(dog1.name)        # (Instance variable)
print(dog1.species)   # (Class variable)
