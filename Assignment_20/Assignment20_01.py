# Design automation script which accepts directory name and displays checksum of all files.
# Usage: DirectoryChecksum.py "Demo"

import os
import hashlib
import sys
from MHeaderFutter import Header, Footer

def CalculateChecksum(Filename):

    fobj = open(Filename, 'rb')
    hobj = hashlib.md5()
    buffer = fobj.read(1024)

    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fobj.read(1024)
    fobj.close()
    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName, LogFileName):    
    flag = os.path.isabs(DirectoryName)
    if flag == False:
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if flag == False:
        print("Path is Invalid")
        exit()

    flag = os.path.isdir(DirectoryName)
    if flag == False:
        print("Path is valid but Directory not found..")
        exit()

    fobj = open(LogFileName, "w")
    Header("Displays CheckSum", fobj) # Header
 
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        for FName in FileName:
            Filepath = os.path.join(FolderName, FName)
            Checksum = CalculateChecksum(Filepath)
            fobj.write(f"File Name : {FName}\n")
            fobj.write(f"Checksum  : {Checksum}\n\n")

    Footer("Close", fobj) # Footer
    fobj.close()

def main():

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script accepts directory name and displays checksum of all files.")
            print("This script accepts two arguments: directory name and Log File name.")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use this Script as:")
            print("DirectoryChecksum.py Directory name LogFileName")
            print("Give proper directory names and file extension as arguments.")


    elif len(sys.argv) == 3:
        DirectoryWatcher(sys.argv[1], sys.argv[2])

    else:
        print("Invalid Number of Command-line Arguments")
        print("Use the given flags:")
        print("--h : Used to display Help")
        print("--u : Used to Display Usage")

if __name__ == "__main__":
    main()
