class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        return 0
    
    def info(self):
        print(f"{self.name} - 넓이: {self.area()}")

class rectangle(Shape):
    def __init__(self, base, height):
        self.base=base
        self.name="사각형"
        self.height=height
    def area(self):
        return self.base*self.height
    def info(self):
        print(f"{self.name}의 넓이: {self.area()}")

class triangle(Shape):
    def __init__(self, base, height):
        self.base=base
        self.height=height
        self.name="삼각형"
    def area(self):
        return (self.base*self.height)/2
    def info(self):
        print(f"{self.name}의 넓이: {self.area()}")

class circle(Shape):
    def __init__(self, radius):
        self.radius=radius
        self.name="원"
    def area(self):
        return self.radius*self.radius*3.14
    def info(self):
        print(f"{self.name}의 넓이: {self.area()}")

g=triangle(3, 7)
g.info()

h=rectangle(100, 98)
h.info()

j=circle(1.34)
j.info()
