# Create a class BankAccount with account_number, name, and balance. Use __init__ and create methods for deposit, withdraw, and displaying balance.

class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def display(self):
        print(f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}")

# Creating an object and calling methods
account1 = BankAccount(101, "Rohit", 50000)
account1.display()
account1.deposit(5000)
account1.withdraw(2000)
account1.display()
