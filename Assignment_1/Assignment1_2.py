# write a program that contains a function named ChkNum(), which accepts one number as a parameter. If the number is even, the function should display "Even number", otherwise "Odd number"

def ChkNum(number):
    if number % 2 == 0:
        return "Even number"
    else:
        return "Odd number"

value = int(input("Enter a number: "))
result = ChkNum(value)

print(" Answer : ", result)

