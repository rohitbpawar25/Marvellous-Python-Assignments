# Write a program which accepts two file names from user and compare contents of both the files.
# If both the files contain same contents then display "Success" otherwise display "Failure".
# Accept names of both the files from command line.
# Input: Demo.txt Hello.txt
# Compare contents of Demo.txt and Hello.txt

import os
import sys

def Compare_File(FileName1, FileName2):
    fobj = open(FileName1, 'r')
    Data1 = fobj.read()
    fobj.close() 

    fobj2 = open(FileName2, 'r')
    Data2 = fobj2.read()
    fobj2.close()  

    if Data1 == Data2:
        print("Success")
    else:
        print("Failure")

def main():
    Input1 = sys.argv[1]
    Input2 = sys.argv[2]
    Compare_File(Input1, Input2)

if __name__ == "__main__":
    main()
