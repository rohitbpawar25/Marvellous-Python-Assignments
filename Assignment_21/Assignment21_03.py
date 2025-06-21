# Design an automation script which accepts a directory name from user 
# and creates a log file in that directory containing information of 
# running processes such as: Process Name, PID, and Username.
# Usage: ProcInfoLog.py Demo

import os
import psutil
import sys
import time
from MHeaderFutter import Header, Footer

def ProcInfoLog(DictName):
    StartTime = time.time()

    if not os.path.isabs(DictName):
        DictName = os.path.abspath(DictName)
    
    if not os.path.exists(DictName):
        print("Path is Invalid")
        exit()

    if not os.path.isdir(DictName):
        print("Path is not a Directory")
        exit()

    LogPath = os.path.join(DictName, "LogInfo.log")

    fobj = open(LogPath, 'w')
    Header("Log File Of Running Processes", fobj)

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid', 'name', 'username'])
        fobj.write(str(info) + '\n')

    EndTime = time.time()
    ExecutionTime = EndTime - StartTime
    fobj.write(f"Execution Time: {ExecutionTime:.2f} seconds\n\n")

    Footer("End", fobj)
    fobj.close()

def main():
    Border = "-" * 80
    print(Border + "\n")
    print("Information of Script".center(90) + "\n")
    print(Border + "\n")

    if len(sys.argv) == 2:
        if sys.argv[1] in ("--h", "--H"):
            print("This script creates a log file with information of running processes.\n")
        elif sys.argv[1] in ("--u", "--U"):
            print("Usage: ProcInfoLog.py DirectoryName\n")
        else:
            ProcInfoLog(sys.argv[1])
            print("Code is Executed\n")  
    else:
        print("Invalid number of command-line arguments.")
        print("Use the given flags:")
        print("--h: Used to display the help")
        print("--u: Used to display the usage\n")

    print(Border + "\n")    
    print("End".center(90) + "\n")
    print(Border + "\n")

if __name__ == "__main__":
    main()
