# Write a program which accepts file name from user and create new file named as Demo.txt and copy all contents from existing file into new file. Accept file name through command line arguments.

import sys
import os

def Copy_Content(FileName1,FileName2):
    fobj1 = open(FileName1, 'r')           
    Data = fobj1.read() 
    fobj1.close()     
                            
    fobj2 = open(FileName2, 'w')         
    fobj2.write(Data)                   
    fobj1.close()                       

def main():
    Input1 = sys.argv[1]
    Input2 = sys.argv[2]
    Copy_Content(Input1,Input2)

if __name__ == "__main__":
    main()

