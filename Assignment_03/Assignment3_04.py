# Write a program that accepts N numbers from the user, stores them in a list, then takes another number from the user and returns its frequency within the list.

def FindFrequency(lst, target):
    return lst.count(target)

def main():
    Data = []
    
    print("Enter number of elements: ")
    Size = int(input())

    print("Please enter numeric values: ")
    for i in range(Size):
        no = int(input())
        Data.append(no) 

    print("Input data:", Data)

    print("Enter the number to search for:")
    target = int(input())

    Value = FindFrequency(Data, target)
    print("Frequency of {target} in the list is:", Value)

if __name__ == "__main__":
    main()
