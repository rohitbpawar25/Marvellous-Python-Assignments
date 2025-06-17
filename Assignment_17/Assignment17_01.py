# Write a Python script that prints "Jay Ganesh..." every 2 seconds. Use the schedule.every(2).seconds.do(...) function.
import os
import schedule
import time

def Great():
    print("Jay Ganesh...")

def main():
    schedule.every(1).seconds.do(Great)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()