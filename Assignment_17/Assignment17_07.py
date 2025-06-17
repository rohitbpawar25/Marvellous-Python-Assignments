# Schedule a function that performs file backup every hour and writes a log entry into backup_log.txt.

import schedule
import time
import os

def File_BackUp():
    MainFile = "Marvellous.txt"
    if not os.path.exists("BackUpLog.txt"):
        fobj1 = open("BackUpLog.txt", 'w')
        fobj1.write("Backup Log File\n")
        fobj1.close()
    
    fobj2 = open("BackUpLog.txt", 'a')
    fobj2.write("Backup of " + MainFile + " completed at " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
    fobj2.close()

def main():

    schedule.every().hour.do(File_BackUp)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
