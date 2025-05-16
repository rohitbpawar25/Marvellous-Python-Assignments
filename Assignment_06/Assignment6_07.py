# Accept 5 numbers from the user. Find and print the largest number.

def LarNum(Data):
    max = Data[0]
    for num in Data:
        if num > max:
            max = num
    return max


def main():

     Data = []
     Input = int(input("Enter how many number you want to Enter :"))

     for i in range(Input):
         Num = int(input("Enter the number: "))
         Data.append(Num)

     print("The largest number is: ", Data)

     result = LarNum(Data)
     print(result)
        

if __name__ == "__main__":
    main()
