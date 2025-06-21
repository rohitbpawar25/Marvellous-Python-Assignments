# Design an automation script which accepts a directory name and deletes all duplicate files from that directory.Write the names of deleted duplicate files into a log file named Log.txt.Log.txt file should be created inside the target directory.
# Usage: DirectoryDuplicateRemoval.py "Demo"

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
    Header("Delete Duplicates", fobj)

    Duplicate = {}
    TotalFiles = 0
    DeletedFiles = 0
    DeletedDetails = []

    for Folder, SubFolder, Files in os.walk(FileName):
        for File in Files:
            Fname = os.path.join(Folder, File)

            if os.path.abspath(Fname) == os.path.abspath(LogPath):
                continue

            TotalFiles += 1
            CheckSum = CalculateChecksum(Fname)

            if CheckSum in Duplicate:
                os.remove(Fname)
                DeletedFiles += 1
                DeletedDetails.append(f"Deleted File: {os.path.basename(Fname)}\nChecksum : {CheckSum}\n\n")
            else:
                Duplicate[CheckSum] = Fname

   
    fobj.write("Summary:\n")
    fobj.write(f"Total Files Scanned   : {TotalFiles}\n")
    fobj.write(f"Total Files Deleted   : {DeletedFiles}\n")
    fobj.write(f"Unique Files Remaining: {TotalFiles - DeletedFiles}\n\n")
    fobj.write("Deleted Duplicate Files:\n\n")


    for entry in DeletedDetails:
        fobj.write(entry)

    Footer("Close", fobj)
    fobj.close()

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] in ("--h", "--H"):
            print("This script deletes duplicate files from a directory and logs them.")

        elif sys.argv[1] in ("--u", "--U"):
            print("Usage: DirectoryDuplicateRemoval.py DirectoryName")

        else:
            DirectoryDuplicate(sys.argv[1])
    else:
        print("Invalid number of Command Line Arguments")
        print("Use the given flags:")
        print("--h: Used to Display the Help")
        print("--u: Used to Display the Usage")

if __name__ == "__main__":
    main()
