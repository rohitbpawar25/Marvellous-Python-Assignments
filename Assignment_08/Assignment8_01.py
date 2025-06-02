# Design a Python application that creates two threads named even and odd. The even thread will display the first 10 even numbers, and the odd thread will display the first 10 odd numbers

import threading

def print_even():
    for num in range(2, 21, 2):  
        print(f"Even: {num}")


def print_odd():
    for num in range(1, 20, 2):  
        print(f"Odd: {num}")


even_thread = threading.Thread(target=print_even, name="even")
odd_thread = threading.Thread(target=print_odd, name="odd")


even_thread.start()
odd_thread.start()


even_thread.join()
odd_thread.join()

print("Threads execution completed.")
