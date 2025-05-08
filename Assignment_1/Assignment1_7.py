# Write a program that accepts a number from the user and returns True if the number is divisible by 5, otherwise False.


def Div(num):
    if num % 5 == 0:
        return True
    else:
        return False
    
def main():
    print("Enter a number :")
    no = int(input())
    value = Div(no)
    print("The number is",value)
    
if __name__ == "__main__":
    main()


'''
def Div(num):
    if num % 5 == 0:
        return True
    else:
        return False
    
print("Enter a number :")
no = int(input())

value = Div(no)
print("The number is",value)

'''