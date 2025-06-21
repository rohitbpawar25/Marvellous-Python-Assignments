# Design an automation script which accepts a directory name and email ID from the user.It should: Create a log file in that directory containing info of running processes (Name, PID, Username) and send that log file to the specified email address.
# Usage: ProcInfoLog.py Demo marvellousinfosystem@gmail.com

import os
import psutil
import sys
import time
import smtplib
from email.message import EmailMessage
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

    return LogPath

def SendMail(directory, reciver):
    Subject = ("Text File sent using Python")
    Body = ("Attached is the log file of running processes.")
    sender = ("testmail252002@gmail.com")
    password = ("MAIL@1025") 

    LogPath = os.path.join(directory, "LogInfo.log")

    fobj = open(LogPath, 'rb')
    log_data = fobj.read()
    fobj.close()

    msg = EmailMessage()
    msg['Subject'] = Subject
    msg['From'] = sender
    msg['To'] = reciver
    msg.set_content(Body)

    msg.add_attachment(
        log_data,
        maintype='application',
        subtype='octet-stream',
        filename="LogInfo.log"
    )

    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(sender, password)
    smtp.send_message(msg)
    smtp.quit()

    print("Mail sent successfully.\n")

def main():
    Border = "-" * 80
    print(Border + "\n")
    print("Information of Script".center(90) + "\n")
    print(Border + "\n")

    if len(sys.argv) == 3:
        if sys.argv[1] in ("--h", "--H"):
            print("This script creates a log file with information of running processes and sends it via Gmail.\n")
        elif sys.argv[1] in ("--u", "--U"):
            print("Usage: ProcInfoLog.py DirectoryName EmailID\n")
        else:
            LogPath = ProcInfoLog(sys.argv[1])
            SendMail(sys.argv[1], sys.argv[2])
            print("Code executed successfully.\n", LogPath) 
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
