# Design automation script which accepts directory name and file extension from user.Display all files with that extension.
# Usage: DirectoryFileSearch.py "Demo" ".txt"

import sys
import os
from MHeaderFutter import Header, Footer
from MCheckPath import CheckPath

def DirectoryWatcher(DictName, Extension, OutputFile):

    CheckPath(DictName)  # Used Module to check if directory exists or not

    fobj = open(OutputFile, "w")
    Header("Assignment19_Output", fobj)  # used module to display header

    for FolderName, SubFolderName, FileName in os.walk(DictName):
        for fname in FileName:
            if fname.endswith(Extension):
                fobj.write(fname + "\n")

    Footer("Close", fobj)  # used module to display footer

    fobj.close()

def main():

    if len(sys.argv) == 2:

        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This Application is used to Perform Sorting of files wrt to Extensions")
            print("This is a Directory Automation Script")

        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given Script as:")
            print("ScriptName.py DirectoryName Extension OutputFile")
            print("Please provide valid Absolute path")

    elif len(sys.argv) == 4:
        DirectoryWatcher(sys.argv[1], sys.argv[2], sys.argv[3])

    else:
        print("Invalid Number of Command-line Arguments")
        print("Use the given flags:")
        print("--h : Used to display Help")
        print("--u : Used to Display Usage")

if __name__ == "__main__":
    main()
