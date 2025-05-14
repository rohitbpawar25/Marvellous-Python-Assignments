# write a program that accepts a number from the user and returns the sum of its factors.

def SumFactors(Num1):
    total = 0
    for i in range(1,Num1):
        if Num1 % i == 0:
            total += i
    return total

def main():
    No1 = int(input("Enter A Number : "))
    result = SumFactors(No1)
    print("Sum of Factors of", No1, "is", result)

if __name__ == "__main__":
    main()
