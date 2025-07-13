from math import sin, cos, radians
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    @staticmethod
    def new_cartesian(x, y):
        return Point(x, y)
    
    @staticmethod
    def new_polar(r, theta):
        return Point(r * cos(theta), r * sin(theta))
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
if __name__ == "__main__":
    p1 = Point(2,3)
    p2 = Point.new_cartesian(4, 5)
    p3 = Point.new_polar(5, 6)
    print(p1)  # Point(2, 3)
    print(p2)  # Point(4, 5)
    print(p3)  # Point(5 * cos(6), 5 * sin
