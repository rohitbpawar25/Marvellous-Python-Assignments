# Write a program which accepts a number from the user and checks whether that number is positive, negative, or zero.

def CheckNumber(num):
    if num > 0:
        return "Number is Positive"
    elif num < 0:
        return "Number is Negative"
    else:
        return "Zero"

def main():
    print("Enter a Number:")
    number = int(input())
    
    result = CheckNumber(number)
    print(result)

if __name__ == "__main__":
    main()
