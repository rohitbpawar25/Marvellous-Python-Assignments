# Arithmetic Operations on Two Numbers Write a program to accept two integers from the user and display their:Sum,Difference,Product,Division
def Sum(Num1,Num2):
    return Num1 + Num2

def Difference(Num1,Num2):
    return Num1 - Num2

def Product(Num1,Num2):
    return Num1 * Num2

def Division(Num1,Num2):
    return Num1 / Num2


def main():

    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    Result1 = Sum(No1,No2)
    Result2 = Difference(No1,No2)
    Result3 = Product(No1,No2)
    result4 = Division(No1,No2)

    print("Sum is :",Result1)
    print("Difference is :",Result2)
    print("Product is :",Result3)
    print("Division is :",result4)


if __name__ == "__main__":
    main()