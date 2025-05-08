# Write a program that accepts a name from the user and displays its length.

def Length(name):
    l = len(name)
    return l
print("Enter a Name :")
Char = input()
Value = Length(Char)
print("length of string is :",Value)
