class Circle:

    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
if __name__ == "__main__":  
    circle = Circle(5)
    print(f"Circle radius: {circle.radius}")
    
    # Update radius
    circle.radius = 10
    print(f"Updated Circle radius: {circle.radius}")
    
    # Attempt to set a negative radius
    try:
        circle.radius = -3
    except ValueError as e:
        print(e)  # Output: Radius cannot be negative