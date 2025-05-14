# write a Python program that accepts one number from the user and returns its factorial.

def Factorial(Num1):
    if Num1 == 0 or Num1 == 1:
        return 1
    else:
        return Num1 * Factorial(Num1 - 1)

def main():
    num = int(input("Enter a number: "))
    result1 = Factorial(num)
    print("Factorial of the number is: ", result1)

if __name__ == "__main__":
    main()