# Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from the user. filter() should filter out all such numbers which are even. map() function will calculate the square of each filtered number. reduce() will return the sum of all squared numbers.

from functools import reduce

ChkEven = lambda Num1 : Num1 % 2 == 0
CalSquare = lambda Num1 : Num1 ** 2
Sum = lambda Num1,Num2 : Num1 + Num2

'''
def ChkEven(Num1):
    return (Num1%2 == 0)

def CalSquare(Num1):
    return (Num1 ** 2)

def Sum(Num1,Num2):
    return (Num1 + Num2)
'''

def main():
    Data = []
    Input =int(input("Enter how much number want to Store :"))

    for i in range(Input):
        Values =int(input("Enter Number :"))
        Data.append(Values)
    print("Inserted Values Are",Data)

    FData = list(filter(ChkEven,Data))
    print("Filtered data is :",FData)

    MData = list(map(CalSquare,FData))
    print("Mapped data are :",MData)

    RData = reduce(Sum,MData)
    print("Reduced data is :",RData)


if __name__ =="__main__":
    main()