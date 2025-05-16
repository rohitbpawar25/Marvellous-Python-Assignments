# Accept a number and print its factorial using a for loop.

def factorial():
    
    num = int(input("Enter a number: "))
    result = 1
    for i in range(1, num + 1):
        result *= i
    print(f"Factorial of {num} is: {result}")

factorial()