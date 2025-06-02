# Write a program which contains one class named as Numbers. Numbers class contains one instance variable as Value. Inside the init method, initialize that instance variable to the value which is accepted from the user. There are four instance methods inside the class: ChkPrime(), ChkPerfect(), SumFactors(), Factors(). ChkPrime() method will return true if the number is prime, otherwise return false. ChkPerfect() method will return true if the number is perfect, otherwise return false. Factors() method will display all factors of the instance variable. SumFactors() method will return the sum of all factors. Use this method in any other method as a helper method if required. After designing the above class, call all instance methods by creating multiple

class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

    def SumFactors(self):
        return sum([i for i in range(1, self.Value) if self.Value % i == 0])

    def Factors(self):
        print("Factors:", [i for i in range(1, self.Value + 1) if self.Value % i == 0])

# Creating multiple objects and calling methods
num1 = Numbers(28)
print("Is Prime:", num1.ChkPrime())
print("Is Perfect:", num1.ChkPerfect())
num1.Factors()
print("Sum of Factors:", num1.SumFactors())

num2 = Numbers(7)
print("Is Prime:", num2.ChkPrime())
print("Is Perfect:", num2.ChkPerfect())
num2.Factors()
print("Sum of Factors:", num2.SumFactors())
