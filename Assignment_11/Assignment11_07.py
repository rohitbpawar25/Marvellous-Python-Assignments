# Print Pattern Using Recursion (Right Triangle): Write a recursive function to print the following pattern:

i = 1
j = 1

def printLine():
    global j
    if j > 0:
        print("* ", end='')
        j -= 1
        printLine()

def printPattern(n):
    global i, j
    if i <= n:
        j = i
        printLine()
        print()
        i += 1
        printPattern(n)

def main():
    printPattern(5)

if __name__ == "__main__":
    main()
