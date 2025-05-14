# Write a Python program that calls all the functions from the Arithmetic module by accepting the parameters from the user.

from ArithmeticM import Addition, Subtraction, Multiplication, Division

def main():
    Val1 = int(input("Enter a First Number :"))
    Val2 = int(input("Enter a Second Number :"))
    
    Result1 = Addition(Val1,Val2)
    Result2 = Subtraction(Val1,Val2)
    Result3 = Multiplication(Val1,Val2)
    Result4 = Division(Val1,Val2)

    print("Addition of two numbers is : ",Result1)
    print("Subtraction of two numbers is : ",Result2)
    print("Multiplication of two numbers is : ",Result3)
    print("Division of two numbers is : ",Result4)

if __name__ == "__main__":
    main()