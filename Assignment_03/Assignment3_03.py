# Write a program that accepts N numbers from the user, stores them in a list, and returns the minimum number from that list.

def Minimum(Num1):
    return (min(Num1))
    

def main():
    Data = []

    print("Enter number of elements :")
    Value = int(input())

    print("Entered number of elementsn are")

    for i in range(Value):
        num = int(input())
        Data.append(num)
    print("The entered list is: ", Data)

    num = Minimum(Data)
    print("The maximum number is: ", num)
    

if __name__ == "__main__":
    main()