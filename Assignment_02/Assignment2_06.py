# write a program that accepts a number from the user and displays below patteren
'''
* * * * *
* * * *
* * *
* *
*
'''

def Displaypattern(Num1):
    for i in range(Num1, 0, -1):    
            print("*" * i)

def main():

    No1 = int(input("Enter A Number : "))
    Displaypattern(No1)

if __name__ == "__main__":
    main()