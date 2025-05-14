# Write a program that accepts N numbers from the user, stores them in a list, and returns the sum of all elements in the list.

def Addition(Num1):
    sum = 0
    for no in Num1:
        sum = sum + no
    return sum


def main():
    Data = []
    
    print("Enter number of elements : ")
    Size = int(input())

    print("Please enter numeric values : ")
    for i in range(Size):
        no = int(input())
        Data.append(no) 

    print("Input data : ",Data)

    Value = Addition(Data)
    print("Sum of all elements in the list is :",Value)



if __name__ == "__main__":
    main()

    