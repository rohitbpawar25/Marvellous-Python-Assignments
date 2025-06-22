# Design an automation script that:
# 1. Accepts a directory name from the user and deletes all duplicate files based on checksum.
# 2. Creates a directory named "Marvellous" and inside it, generates a log file recording deleted duplicate file names.
#    - The log file should be timestamped with creation date and time.
# 3. Accepts a time interval in minutes and performs duplicate file removal after that interval.
# 4. Accepts an email ID and sends the log file as an attachment.
#    - Email body must include:
#      • Scanning start time
#      • Total number of files scanned
#      • Total number of duplicates found
# Follow these coding rules:
# - Use command-line arguments or accept input through file.
# - Log messages should be written to the log file, not printed to console.
# - Write separate functions for separate tasks and organize them in user-defined modules.
# - Implement proper validations and handle expected exceptions robustly.
# - Include help and usage options.
# - Prepare a README file detailing script usage and command-line options.

import os
import sys
import time
import smtplib
import hashlib
import schedule
from datetime import datetime
from email.message import EmailMessage

def CalculateChecksum(Filename):
    fobj = open(Filename, 'rb')
    hobj = hashlib.md5()
    buffer = fobj.read(1024)

    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fobj.read(1024)
    fobj.close()
    return hobj.hexdigest()

def DirectoryDuplicate(FileName):
    StartTime = datetime.now()
    StartEpoch = time.time()

    if not os.path.isabs(FileName):
        FileName = os.path.abspath(FileName)

    if not os.path.exists(FileName):
        return

    if not os.path.isdir(FileName):
        return

    TargetDir = "Marvellous"
    if not os.path.exists(TargetDir):
        os.makedirs(TargetDir)
    
    Timestamp = StartTime.strftime("%Y-%m-%d_%H-%M-%S")
    LogPath = os.path.join(TargetDir, f"DuplicateDeleteLog_{Timestamp}.log")

    fobj = open(LogPath, 'w')

    Border = "-" * 90
    fobj.write(Border + "\n")
    fobj.write("Deleted Duplicates Files Log Details".center(90) + "\n")
    fobj.write(("Date: " + StartTime.strftime("%Y-%m-%d") + "    Time: " + StartTime.strftime("%H:%M:%S")).center(90) + "\n")
    fobj.write(Border + "\n")

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
                DeletedDetails.append(f"Deleted File: {os.path.basename(Fname)}\nChecksum    : {CheckSum}\n\n")
            else:
                Duplicate[CheckSum] = Fname

    fobj.write(f"Scanning started at: {StartTime}\n")
    fobj.write(f"Total Files Scanned: {TotalFiles}\n")
    fobj.write(f"Total Duplicates Found: {DeletedFiles}\n\n")

    fobj.write("Deleted Duplicate Files:\n\n")
    for entry in DeletedDetails:
        fobj.write(entry)

    ExecutionTime = time.time() - StartEpoch
    fobj.write(f"Execution Time: {ExecutionTime:.2f} seconds\n\n")
    fobj.write(Border + "\n")
    fobj.write("End".center(90) + "\n")
    fobj.write(Border + "\n")
    fobj.close()

    return LogPath, StartTime, TotalFiles, DeletedFiles

def TimeInterval(Min, Directory, EmailSend):
    def task():
        logfile, start, total, deleted = DirectoryDuplicate(Directory)
        SendMail(logfile, EmailSend, start, total, deleted)
    schedule.every(Min).minutes.do(task)
    while True:
        schedule.run_pending()
        time.sleep(1)

def SendMail(LogPath, reciver, StartTime, TotalFiles, DeletedFiles):
    Subject = "Duplicate File Removal Report"
    Body = (f"Report for Duplicate File Removal\nScanning Started At: {StartTime}\nTotal Files Scanned: {TotalFiles}\nTotal Duplicate Files Found: {DeletedFiles}")

    sender = "aditi.raut.1305@gmail.com"
    password = "slghpxblmazrvhsw"

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
        filename=os.path.basename(LogPath)
    )

    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(sender, password)
    smtp.send_message(msg)
    smtp.quit()

def main():
    Border = "-" * 80
    print(Border + "\n")
    print("Information of Script".center(90) + "\n")
    print(Border + "\n")

    if len(sys.argv) == 2:
        if sys.argv[1] in ("--h", "--H"):
            print("This script deletes duplicate files and sends the log via email after a time interval.")
        elif sys.argv[1] in ("--u", "--U"):
            print("Usage: Assignment22_01.py <DirectoryPath> <TimeInterval(min)> <ReceiverEmail>")

    elif len(sys.argv) == 4:
        Directory = sys.argv[1]
        TimeInt = int(sys.argv[2])
        EmailSend = sys.argv[3]
        print("Code Run successfully")
        print(f"Directory name is : {Directory}\nTime Interval is : {TimeInt}\nEmail will be sent to : {EmailSend}\nProgram is in Running State (Press [con + c] to Stop)\n")

        print(Border + "\n")
        print("End".center(90) + "\n")
        print(Border + "\n")

        TimeInterval(TimeInt, Directory, EmailSend)

    else:
        print("Invalid number of Command Line Arguments")
        print("Use the given flags:")
        print("--h: Used to Display the Help")
        print("--u: Used to Display the Usage\n")

    print(Border + "\n")
    print("End".center(90) + "\n")
    print(Border + "\n")

if __name__ == "__main__":
    main()
