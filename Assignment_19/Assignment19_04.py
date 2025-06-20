# Design automation script which accepts two directory names and a file extension.Copy all files with the given extension from first to second directory (create second at runtime).
# Usage: DirectoryCopyExt.py "Demo" "Temp" ".exe"

import os
import shutil
import sys

def DirectoryCopyExt(OldName, NewDict, Extension):

    flag = os.path.isabs(OldName)
    if flag == False:
        OldName = os.path.abspath(OldName)

    flag = os.path.exists(OldName)
    if flag == False:
        print("The Path is Invalid")
        exit()

    flag = os.path.isdir(OldName)
    if flag == False:
        print("Path is valid but the target is not a directory")
        exit()
    
    if not os.path.exists(NewDict):
        os.mkdir(NewDict)
        print(f"Created Directory: {NewDict}")

    for Folder, SubFolders, FileName in os.walk(OldName):
        for Fname in FileName:
            if Fname.endswith(Extension):
                Files1 = os.path.join(Folder, Fname)
                CopyFile = shutil.copy(Files1, NewDict)
                print(f"File {Fname} copied to {CopyFile}")
    
    print("File copy completed")

def main():
    
    Border = "-" * 90
    print(Border + "\n")
    print(f"{'Assignment19_04'.center(90)}\n")
    print(Border + "\n")

    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This script copies files with a given extension from one directory to another.")
            print("This script accepts three parameters: first directory name, second directory name and file extension.")

        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use this Script as:")
            print("DirectoryCopyExt.py Demo Temp .exe")
            print("Give proper directory names and file extension as arguments.")

    elif len(sys.argv) == 4:
        DirectoryCopyExt(sys.argv[1], sys.argv[2], sys.argv[3])

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
