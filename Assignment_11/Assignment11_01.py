# Printing numbers using recursion write a recursive function to print numbers from 1 to N.

current = 1

def NNum(n):
    global current
    if current <= n:
        print(current, end=' ')
        current += 1
        NNum(n)

def main():
    NNum(5)

if __name__ == "__main__":
    main()