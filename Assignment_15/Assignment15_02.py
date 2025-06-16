# Write a Python program that accepts a file name from the user, opens that file, and displays its contents on the screen

import os

def Display_Contents(FileName):
        fobj = open(FileName, 'r')
        print(fobj.read())
        fobj.close()

def main():
    Input = input("Enter File Name: ")
    Display_Contents(Input)
       
if __name__ == "__main__":
    main()

