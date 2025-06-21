# Design an automation script which accepts a process name and displays its information if it is currently running (Process Name, PID, Username).
# Usage: ProcInfo.py notepad

import psutil
import sys

def ProcInfoByName(PName):
    found = False
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info['name'] == PName:
            print("Process is running!")
            print("PID      :", proc.info['pid'])
            print("Name     :", proc.info['name'])
            print("Username :", proc.info['username'] + "\n")
            found = True
            break

    if not found:
        print("Process not found.")

def main():
    Border = "-" * 80
    print(Border + "\n")
    print("Information of Process".center(90) + "\n")
    print(Border + "\n")

    ProcInfoByName(sys.argv[1])


    print(Border + "\n")
    print("End".center(90) + "\n")
    print(Border + "\n")

if __name__ == "__main__":
    main()
