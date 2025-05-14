# write a program that accepts a number from the user and displays a growing sequence of numbers.
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''

def Displaypattern(Num1):
    for i in range(1, Num1+1, +1):
            for j in range(1, i+1):
                 print(j, end=' ')
            print()

def main():

    No1 = int(input("Enter A Number : "))
    Displaypattern(No1)

if __name__ == "__main__":
    main()