from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, c):
        self.color = c
        
    def get_color(self):
        return self.color
        
    @abstractmethod
    def get_area(self):
        # This method is a placeholder and must be overridden in subclasses
        pass

class Square(Shape):
    def __init__(self, c, side):
        # Initialize the parent class (Shape) using super()
        super().__init__(c)
        self.side = float(side)
        
    def get_area(self):
        # Implementing the abstract method from Shape
        return float(self.side * self.side)