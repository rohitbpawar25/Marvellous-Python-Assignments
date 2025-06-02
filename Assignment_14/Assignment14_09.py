# Create a class Product with attributes name and price. Implement __eq__ method to compare two products if they are equal in price.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False

    def display(self):
        print(f"Product: {self.name}, Price: {self.price}")

# Creating objects and comparing them
product1 = Product("Laptop", 50000)
product2 = Product("Smartphone", 50000)
product3 = Product("Tablet", 30000)

product1.display()
product2.display()
product3.display()

print("Product1 and Product2 have the same price:", product1 == product2)
print("Product1 and Product3 have the same price:", product1 == product3)
