# Write a program which contains filter(), map(), and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return the product of all that numbers.
from functools import reduce

Greater = lambda Num1 : 70 <= Num1 <= 90
Increase = lambda Num1 : Num1 + 10
Product = lambda Num1,Num2 : Num1 * Num2

'''
def Greater(Num1):
    return 70 <= Num1 <= 90

def Increase(Num1):
    return Num1 + 10

def Product(Num1,Num2):
    return Num1 * Num2
    
'''

def main():

    Data = []
    Input = int(input("Enter how much number want to store :"))


    for i in range (Input):
        Values =int(input("Enter Numers :"))
        Data.append(Values)

    print("Values in list:",Data)
    
    FData = list(filter(Greater,Data))
    print("Filtered Data:",FData)
    
    MData = list(map(Increase,FData))
    print("Mapped Data:",MData)

    RData = reduce(Product,MData)
    print("Reduced Data:",RData)


    if __name__ == "__main__":
        main()