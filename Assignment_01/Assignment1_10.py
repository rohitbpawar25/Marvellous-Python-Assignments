# Write a program that accepts a name from the user and displays its length.

def Length(name):
    N = len(name)
    return N

def main():

    print("Enter a Name :")
    Char = input()
    Value = Length(Char)
    print("length of string is :",Value)

if __name__ == "__main__":
    main()


'''
def Length(name):
    l = len(name)
    return l
print("Enter a Name :")
Char = input()
Value = Length(Char)
print("length of string is :",Value)

'''
