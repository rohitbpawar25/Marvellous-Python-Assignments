# Write a program which contains one class named as BankAccount. BankAccount class contains two instance variables as Name & Amount. That class contains one class variable as ROI which is initialized to 10.5. Inside the init method, initialize all name and amount variables by accepting the values from the user. There are four instance methods inside the class: Display(), Deposit(), Withdraw(), CalculateInterest(). Deposit() method will accept the amount from the user and add that value to the instance variable Amount. Withdraw() method will accept the amount to be withdrawn from the user and subtract that amount from the instance variable Amount. CalculateInterest() method calculates the interest based on Amount by considering the rate of interest which is a class variable (ROI). Display() method will display values of all the instance variables: Name and Amount. After designing the above class, call all instance methods by creating multiple objects.

class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Deposit(self, amount):
        self.Amount += amount

    def Withdraw(self, amount):
        if amount <= self.Amount:
            self.Amount -= amount
        else:
            print("Insufficient balance!")

    def CalculateInterest(self):
        return (self.Amount * BankAccount.ROI) / 100

    def Display(self):
        print(f"Account Holder: {self.Name}")
        print(f"Balance: {self.Amount}")

# Creating multiple objects and calling methods
account1 = BankAccount("Alice", 5000)
account1.Deposit(2000)
account1.Withdraw(1000)
print("Interest:", account1.CalculateInterest())
account1.Display()

account2 = BankAccount("Bob", 10000)
account2.Deposit(5000)
account2.Withdraw(3000)
print("Interest:", account2.CalculateInterest())
account2.Display()
