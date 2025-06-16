# Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not. > Input: Demo.txt > Output: Check whether Demo.txt exists or not.

import os

def File_Exist(FileName):
    
    ret = os.path.exists(FileName)
    if(ret == True):
         print("File is present in the current directory")
    else:
         print("There is no such file")

def main():

     Input = input("Enter the filename: ")
     File_Exist(Input)
    

if __name__ == "__main__":
    main()