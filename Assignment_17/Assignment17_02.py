# Schedule a task that displays the current date and time every minute using the datetime module

import datetime
import schedule
import time

def CurrentTime():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    schedule.every(1).minutes.do(CurrentTime)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
