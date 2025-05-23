# Sum of Digits Using Recursion : Write a recursive function to calculate the sum of digits of a number

Sum = 0

def SumOfDigits(no):
    global Sum
    if no > 0:
        Sum = Sum + (no % 10)
        no = no // 10
        SumOfDigits(no)
    return Sum

def main():
    ret = SumOfDigits(1234)
    print(ret)

if __name__ == "__main__":
    main()

    