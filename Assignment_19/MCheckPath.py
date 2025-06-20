# Use this module for Check Path

import os
import sys

def CheckPath(DirectoryName):

    flag = os.path.isabs(DirectoryName)
    if flag == False:
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)
    if flag == False:
        print("The path is invalid.")
        sys.exit()

    flag = os.path.isdir(DirectoryName)
    if flag == False:
        print("Path is valid but the target is not a directory.")
        sys.exit()

    return DirectoryName
