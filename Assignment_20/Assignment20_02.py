# Design an automation script which accepts a directory name and writes the names of duplicate files
# from that directory into a log file named Log.txt (created inside the target directory).
# Usage: DirectoryDuplicate.py "Demo"

import sys
import os
import hashlib
from MHeaderFutter import Header, Footer

def CalculateChecksum(Fname):
    fobj = open(Fname, 'rb')
    hobj = hashlib.md5()
    Buffer = fobj.read(1024)

    while len(Buffer) > 0:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()
    return hobj.hexdigest()

def DirectoryDuplicate(FileName):
    if not os.path.isabs(FileName):
        FileName = os.path.abspath(FileName)

    if not os.path.exists(FileName):
        print("Path is Invalid")
        exit()

    if not os.path.isdir(FileName):
        print("Path is valid but Directory not found..")
        exit()

    LogPath = os.path.join(FileName, "Log.txt")
    fobj = open(LogPath, 'w')
    Header("Writes Duplicates", fobj)

    Duplicate = {}
    TotalFiles = 0
    DuplicateFiles = 0
    DuplicateDetails = []

    for Folder, SubFolder, Files in os.walk(FileName):
        for File in Files:
            Fname = os.path.join(Folder, File)

            if os.path.abspath(Fname) == os.path.abspath(LogPath):
                continue

            TotalFiles += 1
            CheckSum = CalculateChecksum(Fname)

            if CheckSum in Duplicate:
                DuplicateFiles += 1
                DuplicateDetails.append(f"Duplicate File Found: {os.path.basename(Fname)}\nChecksum  : {CheckSum}\n\n")
            else:
                Duplicate[CheckSum] = [Fname]

    fobj.write("Summary:\n")
    fobj.write(f"Total Files Scanned   : {TotalFiles}\n")
    fobj.write(f"Duplicate Files Found : {DuplicateFiles}\n")
    fobj.write(f"Unique Files          : {TotalFiles - DuplicateFiles}\n\n")
    fobj.write("Duplicate Files in the Directory are:\n\n")

    for entry in DuplicateDetails:
        fobj.write(entry)

    Footer("Close", fobj)
    fobj.close()

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "--H" or sys.argv[1] == "--h":
            print("This script is used to find duplicate files in a directory")
            print("It accepts a directory name and writes duplicates to Log.txt (inside the target directory).")
        elif sys.argv[1] == "--U" or sys.argv[1] == "--u":
            print("Use this script as:")
            print("DirectoryDuplicate.py Demo")
        else:
            DirectoryDuplicate(sys.argv[1])
    else:
        print("Invalid number of Command Line Arguments")
        print("Use the given flags:")
        print("--h: Used to Display the Help")
        print("--u: Used to Display the Usage")

if __name__ == "__main__":
    main()
