# Write a program that accepts a number from the user and prints that many * symbols.

def Display_Star(num):
    num = ("*" * num)
    return num

print("Enter a number :")
num = int(input())
value = Display_Star(num)
print("Number of Star Are : ",value)