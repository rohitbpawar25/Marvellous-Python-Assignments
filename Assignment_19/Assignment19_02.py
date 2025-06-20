# Design an automation script which accepts: a directory name and two file extensions.The script should rename all files with the first file extension to the second file extension.
# Usage: python DirectoryRename.py "Demo" ".txt" ".doc"

import sys
import os

def DirectoryRename(DictName, Extension1, Extension2):
    flag = os.path.isabs(DictName)
    if flag == False:
        DictName = os.path.abspath(DictName)

    flag = os.path.exists(DictName)
    if flag == False:
        print("The Path is Invalid")
        exit()

    flag = os.path.isdir(DictName)
    if flag == False:
        print("Path is valid but the target is not a directory")
        exit()

    for FolderName, SubFolderName, FileName in os.walk(DictName):
        for Fname in FileName:
            if Fname.endswith(Extension1):
                OldPath = os.path.join(FolderName, Fname)
                NewFName = Fname.replace(Extension1, Extension2)
                NewPath = os.path.join(FolderName, NewFName)
                os.rename(OldPath, NewPath)
                print(f"Renamed '{Fname}' -> '{NewFName}'")

def main():
    Border = "-" * 90
    print(Border + "\n")
    print(f"{'Assignment19_02'.center(90)}\n")
    print(Border + "\n")

    if len(sys.argv) == 2:
        if sys.argv[1] == '--h' or sys.argv[1] == '--H':
            print("This script accepts a Directory name and two file extensions.")
            print("It renames all files with the first extension to the second one.")

        elif sys.argv[1] == '--u' or sys.argv[1] == '--U':
            print("Use the given Script as:")
            print("Usage: python DirectoryRename.py DirectoryName .Extension1 .Extension2")
            print("Please provide a valid absolute or relative directory path")

    elif len(sys.argv) == 4:
        DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

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
