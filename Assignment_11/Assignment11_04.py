# Power Function Using Recursion : Write a recursive function to calculate x^n.

Result = 1

def power(x, n):
    global Result
    if n > 0:
        Result *= x
        n -= 1
        power(x, n)
    return Result

def main():
    print(power(2, 3))

if __name__ == "__main__":
    main()
