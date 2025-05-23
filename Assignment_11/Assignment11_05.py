# Count Zeros in a Number (Recursively): Write a recursive function to count how many zeros are in the given

Count = 0

def countzeros(n):
    global Count
    if n > 0:
        if n % 10 == 0:
            Count += 1
        n = n // 10
        countzeros(n)
    return Count

def main():
    print(countzeros(1020300))

if __name__ == "__main__":
    main()

