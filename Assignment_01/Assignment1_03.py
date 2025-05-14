# Write a program which contains one function named as Add() which accepts two numbers from the user and returns the addition of those two numbers.

def Add(number1,number2):
    Addition = number1 + number2
    return Addition

def main():

    print("Enter first Number :")
    no1 = int(input())
    print("Enter second Number :")

    no2 = int(input())
    result = Add(no1,no2)
    
    print("Addition of two number is :",result)

if __name__=="__main__":
    main()



'''
def Add(number1,number2):
    Addition = number1 + number2
    return Addition

print("Enter first Number :")
no1 = int(input())
print("Enter second Number :")
no2 = int(input())

result = Add(no1,no2)
print("Addition of two number is :",result)

'''