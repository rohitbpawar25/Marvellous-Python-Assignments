# Accept a list of numbers and use filter() to keep only even numbers.

ChkEven = lambda Num1 : Num1 % 2 == 0

def main():
    Data = []
    Input = int(input("Enter Number of Data you want to Add :"))

    for i in range (Input):
        Values = int(input("Enter Data :"))
        Data.append(Values)
    print("Data in List :",Data)

    FData = list(filter(ChkEven,Data))
    print("Even Number :",FData)

if __name__ == "__main__":
    main()