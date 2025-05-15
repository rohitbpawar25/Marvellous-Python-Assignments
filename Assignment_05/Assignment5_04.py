# Q4. Find Largest Among Three Numbers Write a program to accept three numbers from the user and print the largest using nested if-else statements.

def LargNum(Num1,Num2,Num3):
    if Num1 >= Num2 and Num1 >= Num3:
        return num1
    elif Num2 >= Num1 and Num2 >= Num3:
        return Num2
    else:
        return Num3

    

def main():

    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))
    No3 = int(input("Enter Third Number :"))
    
    result =LargNum(No1,No2,No3)
    print("Large number is ",result)

if __name__ == "__main__":
    main()