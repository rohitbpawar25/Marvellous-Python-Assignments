# Write a program which accepts two file names from user and compares the contents of both the files. > If contents match, display "Success" — otherwise, display "Failure". > Accept both file names as command line arguments.

import os
import sys

def Compare_File(FileName1,FileName2):
    fobj = open(FileName1,'r')
    Data1 = fobj.read()

    fobj2 = open(FileName2,'r')
    Data2 = fobj2.read()

    if Data1 == Data2:
        print("Success")
    else:
        print("Failure")

def main():
    Input1 = sys.argv[1]
    Input2 = sys.argv[2]
    Compare_File(Input1,Input2)

if __name__ == "__main__":
    main()