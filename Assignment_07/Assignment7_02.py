# Accept a list of integers from the user and use the map() function to double each value

DoubleValue = lambda Num1 : Num1 * 2

def main():
    Data = []
    Input = int(input("Enter Number of Data you want to Add :"))

    for i in range (Input):
        Values = int(input("Enter Data :"))
        Data.append(Values)
    print("Data in List :",Data)

    MData = list(map(DoubleValue,Data))
    print("Double list :",MData)

if __name__ == "__main__":
    main()
