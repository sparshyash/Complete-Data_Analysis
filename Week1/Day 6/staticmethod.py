class Addition:
    
    @staticmethod
    def add(a, b):
        # Simply return the sum of the two parameters
        return a + b
    
#  You typically use @staticmethod when the logic inside the function is related to the class but doesn't actually need to access or modify any data stored in the class or its objects.