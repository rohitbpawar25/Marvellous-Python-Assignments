# Create a class Book with a private attribute __price. Add methods to get and set the price. Show encapsulation.

class Book:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price!")

    def get_price(self):
        return self.__price

    def display(self):
        print(f"Book: {self.name}, Price: {self.__price}")

book1 = Book("Python Programming", 500)
book1.display()

book1.set_price(600)
print("Updated Price:", book1.get_price())
