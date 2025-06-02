# Design a Python application that contains two threads named thread1 and thread2. thread1 should display numbers from 1 to 50 on the screen, while thread2 should display numbers from 50 to 1 in reverse order. After thread1 completes execution, schedule thread2 to run.

import threading

def display_numbers(start, end, step):
    for num in range(start, end, step):
        print(num)

thread1 = threading.Thread(target=display_numbers, args=(1, 51, 1), name="thread1")
thread2 = threading.Thread(target=display_numbers, args=(50, 0, -1), name="thread2")

thread1.start()
thread1.join()

thread2.start()
thread2.join()

print("Exit from main")
