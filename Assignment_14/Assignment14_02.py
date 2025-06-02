# Write a class Rectangle with length and width. Add a method to compute area and perimeter.
# Expected Output:
# Area: 50, Perimeter: 30

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

    def compute_perimeter(self):
        return 2 * (self.length + self.width)

# Creating an object and calling methods
rect = Rectangle(10, 5)
print("Area:", rect.compute_area())
print("Perimeter:", rect.compute_perimeter())

