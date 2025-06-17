# Schedule a job that runs every 5 minutes to write the current time to a file "Marvellous.txt".

import schedule
import time
import os

def EveryFive():
    if not os.path.exists("Marvellous.txt"):
        fobj = open("Marvellous.txt", "w")
        fobj.close()
    
    now = time.strftime("%H:%M:%S")
    fobj = open("Marvellous.txt", "a")
    fobj.write(now + "\n")
    fobj.close()

def main():
    schedule.every(5).minutes.do(EveryFive)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
