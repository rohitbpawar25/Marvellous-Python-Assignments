# Write a program that accepts a number from the user and returns True if the number is divisible by 5, otherwise False.

def Div(num):
    if num % 5 == 0:
        return True
    else:
        return False
    
print("Enter a number :")
no = int(input())

value = Div(no)
print("The number is",value)