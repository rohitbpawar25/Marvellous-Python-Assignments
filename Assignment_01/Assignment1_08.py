# Write a program that accepts a number from the user and prints that many * symbols.

def Display_Star(num):
    num = (" * " * num)
    return num

def main():
    print("Enter a number :")
    num = int(input())
    value = Display_Star(num)
    print("Stars are printed : ",value)

if __name__ == "__main__":
    main()

'''
def Display_Star(num):
    num = ("*" * num)
    return num

print("Enter a number :")
num = int(input())
value = Display_Star(num)
print("Number of Star Are : ",value)

'''