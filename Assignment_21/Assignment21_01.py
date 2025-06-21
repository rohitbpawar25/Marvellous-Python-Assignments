# Design an automation script which displays information of running processes such as: Process Name, Process ID (PID), and Username.
# Usage: ProcInfo.py

import psutil
from MHeaderFutter import Header, Footer

def ProcInfo():
    fobj = open("Logfile", 'w')
    Header("ProcInfo", fobj)

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid', 'name', 'username'])
        fobj.write(f"{info}\n")

    Footer("End", fobj)
    fobj.close()

def main():
    ProcInfo()

if __name__ == "__main__":
    main()
