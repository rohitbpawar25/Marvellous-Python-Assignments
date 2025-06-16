# Accept a file name and one string from the user and return the frequency of that string from the file.

import os
import sys

def String_Frequency(FileName, String):
    fobj = open(FileName,'r')
    Data = fobj.read()
    frequency = Data.count(String)
    print(f"The word '{String}' occurred {frequency} times in '{FileName}'.")
    
def main():
    Filename = input("Enter the Filename: ")
    String = input("Enter the String: ")
    String_Frequency(Filename,String)

if __name__ == "__main__":
    main()