# 📂 Duplicate File Removal Automation Script
---

## 📌 Objective
This Python script automates the process of removing duplicate files based on checksums. It logs the operation results into a timestamped log file and sends the log via email at specified time intervals. 

---

## 🔧 Features

- Detects and removes duplicate files using MD5 checksums  
- Creates a `Marvellous/` directory to store log files  
- Log files are timestamped for uniqueness and traceability  
- Logs contain all deleted file names and checksums  
- Includes summary with total files scanned and deleted  
- Automatically emails the log file as an attachment  
- Supports time-based scheduling using time intervals (in minutes)  
- Designed with separate, reusable functions in a user-defined module  
- Includes input validations and exception handling  
- Provides help (`--h`) and usage (`--u`) command-line flags  

---

## ⚙️ How to Use

### 🎯 Command-Line Input

- **python Assignment22.py  DirectoryPath  TimeIntervalInMinutes  ReceiverEmail**

## Flow of Program

```bash

main()
  └── TimeInterval(Min, Directory, EmailSend)
         └── task()  [executed every X minutes]
               ├── DirectoryDuplicate(Directory)
               │     └── CalculateChecksum(Fname)
               └── SendMail(LogPath, EmailSend, StartTime, TotalFiles, DeletedFiles)

# ========================
# Script starts executing here
# ========================
if __name__ == "__main__":
    main()  # Entry point of the program

# ========================
# Main function starts
# ========================
def main():
    # Print script info header
    # Accept command-line arguments from user
    # If user provides --h → show help message
    # If user provides --u → show usage format
    # If user provides valid 3 arguments → directory, interval, email:
    #     → Convert interval to integer
    #     → Call TimeInterval() and pass all arguments

# ========================
# Called from main() with 3 arguments
# ========================
def TimeInterval(Min, Directory, EmailSend):
    # Define an internal task() function to be run every N minutes
    def task():
        # Step 1: Call DirectoryDuplicate() with Directory path
        #         → This scans for and deletes duplicates
        #         → Returns log path, start time, total files, and deleted files
        # Step 2: Pass those returned values to SendMail() for email delivery

    # Schedule task() to repeat every 'Min' minutes
    # Run scheduler loop infinitely using schedule.run_pending()

# ========================
# Called from task() inside TimeInterval
# ========================
def DirectoryDuplicate(FileName):
    # Validate and convert path
    # Create 'Marvellous' folder if not already exists
    # Create a timestamped log file
    # Walk through directory with os.walk()

    # For each file:
    #     → Generate checksum using CalculateChecksum()
    #     → If checksum already exists → delete the file and log details
    #     → Else, store the checksum in a dictionary

    # At the end:
    #     → Write all deleted file info into the log
    #     → Append summary stats (files scanned, deleted, execution time)

    # Return: log path, start time, total file count, deleted file count

# ========================
# Helper used inside DirectoryDuplicate()
# ========================
def CalculateChecksum(Filename):
    # Open file in binary mode and read in 1024-byte chunks
    # Generate MD5 hash of file contents
    # Return that hash string for duplicate detection

# ========================
# Called from task() after DirectoryDuplicate completes
# ========================
def SendMail(LogPath, reciver, StartTime, TotalFiles, DeletedFiles):
    # Format a clean email body using f-strings with scan stats
    # Open the log file in binary mode for attachment
    # Set up EmailMessage object with subject, sender, receiver, body
    # Attach the log file to the email
    # Connect to Gmail SMTP with SSL and send the email
    # Close connection

# ========================
# Final result:
# Every 'N' minutes, the system:
#     → Scans directory
#     → Deletes duplicates
#     → Logs all info
#     → Sends email summary + log file
#     → Waits for the next round
# ========================
# your bash commands here
echo "Done"
```
## 🧾 Conclusion

A streamlined automation tool that simplifies duplicate file management by combining checksum validation, timestamped logging, and scheduled email reporting—ideal for efficient and traceable cleanup tasks.



