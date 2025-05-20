#Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from the user. filter() should filter out all prime numbers. map() function will multiply each number by 2. reduce() will return the maximum number from the mapped list. You can also use normal functions instead of lambda functions.

from functools import reduce

def ChkPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
 

def Multiply(Num1):
    return Num1 * 2

def MaxNum(Num1,Num2):
    return (max(Num1,Num2))

def main():
    Data = []
    Input = int(input("Enter how much number want to Store :"))
    for i in range(Input):
        Values = int(input("Enter Number :"))
        Data.append(Values)
    print("Data in list :",Data)

    FData = list(filter(ChkPrime,Data))
    print("Filtered Data is :",FData)

    MData = list(map(Multiply,FData))
    print("Maped Data is : ",MData)

    RData = reduce(MaxNum,MData)
    print("Reduce Data is :",RData)



if __name__ == "__main__":
    main()