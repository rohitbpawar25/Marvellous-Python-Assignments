# Design automation script which accepts two directory names.Copy all files from the first directory into the second directory (create second at runtime).
# Usage: DirectoryCopy.py "Demo" "Temp"

import os
import sys
import shutil

def DirectoryCopyFile(Dict1, Dict2):

    flag = os.path.isabs(Dict1)
    if flag == False:
        Dict1 = os.path.abspath(Dict1)

    flag = os.path.exists(Dict1)
    if flag == False:
        print("The Path is Invalid")
        exit()

    flag = os.path.isdir(Dict1)
    if flag == False:
        print("Path is valid but the target is not a directory")
        exit()
    
    if not os.path.exists(Dict2):
        os.mkdir(Dict2)
        print(f"Created Directory: {Dict2}")

    for Folder, SubFolders, FileName in os.walk(Dict1):
        for Fname in FileName:
            Files1 = os.path.join(Folder, Fname)
            CopyFile = shutil.copy(Files1, Dict2)
            print(f"File Copied: {CopyFile}")

    print("Files Copied Successfully")

def main():

    Border = "-" * 90
    print(Border + "\n")
    print(f"{'Assignment19_02'.center(90)}\n")
    print(Border + "\n")

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script is for copying files from one directory to another.")
            print("Script accepts two directory names as arguments.")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the given Script as:")
            print("Usage: python DirectoryCopy.py Directory1 Directory2")
            print("Please provide a valid absolute or relative directory path")

    elif len(sys.argv) == 3:
        DirectoryCopyFile(sys.argv[1], sys.argv[2])

    else:
        print("Invalid Number of Command-line Arguments")
        print("Use the given flags:")
        print("--h : Used to display Help")
        print("--u : Used to Display Usage")
    
    print("\n" + Border)
    print(f"{'End of Execution'.center(90)}")
    print(Border)

if __name__ == "__main__":
    main()
