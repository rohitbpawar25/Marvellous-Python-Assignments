# write a program that accepts a number from the user and checks whether it is a prime number or not.

def CheckPrime(Num1):
    if Num1 < 2:
        return ("Not Prime")
    for i in range(2,int(Num1 ** 0.5) + 1):
        if Num1 % i == 0:
            return ("Not Prime")
    return ("Prime")


def main():
    Num = int(input("Enter a number: "))
    Val = CheckPrime(Num)
    print("Entered number is :",Val)

if __name__ == "__main__":
    main()
