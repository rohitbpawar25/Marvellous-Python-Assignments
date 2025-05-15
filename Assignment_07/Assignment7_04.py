# Accept a list of numbers and use the reduce() function (from functools) to find the product of all numbers.

from functools import reduce

ProductNum = lambda Num1,Num2 : Num1 * Num2

def main():
    Data = []
    Input = int(input("Enter Number of Data you want to Add :"))

    for i in range (Input):
        Values = int(input("Enter Data :"))
        Data.append(Values)
    print("Data in List :",Data)

    RData = reduce(ProductNum,Data)
    print("Product of all Numbers is :",RData)

if __name__ == "__main__":
    main()