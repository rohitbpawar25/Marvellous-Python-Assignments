# Write a program which contains one class named as Arithmetic. Arithmetic class contains two instance variables: Value1, Value2. Inside the init method, initialize all instance variables to 0. There are five instance methods inside the class: Accept(), Addition(), Subtraction(), Multiplication(), Division(). Accept method will accept values of Value1 and Value2 from the user. Addition() method will perform addition of Value1 and Value2 and return the result. Subtraction() method will perform subtraction of Value1 and Value2 and return the result. Multiplication() method will perform multiplication of Value1 and Value2 and return the result. Division() method will perform.

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter first number: "))
        self.Value2 = float(input("Enter second number: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Division by zero is not allowed"

# Creating multiple objects and calling methods
arith1 = Arithmetic()
arith1.Accept()
print("Addition:", arith1.Addition())
print("Subtraction:", arith1.Subtraction())
print("Multiplication:", arith1.Multiplication())
print("Division:", arith1.Division())

arith2 = Arithmetic()
arith2.Accept()
print("Addition:", arith2.Addition())
print("Subtraction:", arith2.Subtraction())
print("Multiplication:", arith2.Multiplication())
print("Division:", arith2.Division())
