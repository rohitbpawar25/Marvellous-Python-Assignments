# write a program that accepts a number from the user and returns the number of digits in that number

def CountDigits(Num1):
    count = 0
    while Num1 > 0:
        Num1 //= 10  
        count += 1 
    return count

def main():

    Num = int(input("Enter A Number: "))
    Val = CountDigits(Num)
    print("Number of digits in the number is: ", Val)

if __name__ == "__main__":
    main()


    