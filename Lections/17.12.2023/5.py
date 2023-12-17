class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print(self):
     print(f"Ширина: {self.width}, Высота: {self.height}")
     
    def PrintP(rectangle):
        return 2 * (rectangle.width + rectangle.height)
        
    def PrintS(rectangle):
        return rectangle.width * rectangle.height

    def __eq__(self, other):
     if isinstance(other, Rectangle):
        return self.width == other.width and self.height == other.height
     else:
         return False