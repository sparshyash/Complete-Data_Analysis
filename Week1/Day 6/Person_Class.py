class Person:
    def __init__(self):
        # Private attributes with double underscores
        self.__name = "Geeks"
        self.__age = 10

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, age):
        self.__age = age