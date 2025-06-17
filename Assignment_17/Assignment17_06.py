# Write a script that schedules multiple tasks:
# - One to print "Lunch Time!" at 1 PM 
# - Another to print "Wrap up work" at 6 PM

import schedule
import time

def LunchTime():
    print("Lunch Time!")

def WrapUpWork():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(LunchTime)
    schedule.every().day.at("18:00").do(WrapUpWork)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__ == "__main__":
    main()