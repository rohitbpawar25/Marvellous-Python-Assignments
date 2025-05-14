# write a program that accepts a number from the user and displays a repeated sequence of numbers.
'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

'''

def Displaypattern(Num1):
    for i in range(Num1):
        for j in range(1,Num1+1):
            print(j,end=" ")
        print()

def main():

    No1 = int(input("Enter A Number : "))
    Displaypattern(No1)

if __name__ == "__main__":
    main()
    
'''

def Displaypattern(Num1):
    for i in range(Num1):    
            print("1 2 3 4 5")

def main():

    No1 = int(input("Enter A Number : "))
    Displaypattern(No1)

if __name__ == "__main__":
    main()
    
'''