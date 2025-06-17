# Write a program that schedules a function to print “Do Coding..!” every 30 minutes.
import time
import schedule 

def DoCode():
    print("Do Coding..!")

def main():
    schedule.every(30).minutes.do(DoCode)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
