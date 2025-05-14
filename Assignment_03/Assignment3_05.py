# Write a program that accepts N numbers from the user, stores them in a list, and returns the sum of all prime numbers from the list. The main Python file should call the function ChkPrime() from a user-defined module named MarvellousNum. The function name in the main file should be ListPrime()

from MarvellousNum import ChkPrime

def ListPrime(Num1):
    prime_sum = 0  
    for num in Num1:
        if ChkPrime(num):
            prime_sum += num
    return prime_sum 


def main():
    Data = []
    
    print("Enter number of elements: ")
    Size = int(input())

    print("Please enter numeric values: ")
    for i in range(Size):
        no = int(input())
        Data.append(no) 

    print("Input data:", Data)

    Value = ListPrime(Data)
    print("Sum of all prime numbers in the list is:", Value)

if __name__ == "__main__":
    main()


