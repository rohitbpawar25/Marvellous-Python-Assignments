# Sum of First N Natural Numbers Using Recursion : Write a recursive function to calculate sum from 1 to n.

Total = 0

def sumNum(n):
    global Total
    if n > 0:
        Total += n
        n -= 1
        sumNum(n)
    return Total

def main():
    print(sumNum(5))

if __name__ == "__main__":
    main()

