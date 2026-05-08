#Inheritance

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0
    
class circle(Shape):      #child inherits from Shape
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class square(Shape):          #override parent method
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side * self.side
