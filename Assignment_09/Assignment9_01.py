# Create a Python program that starts 3 threads, each printing numbers from 1 to 5 with a delay of 1 second. Use threading.Thread.

import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Thread {threading.current_thread().name}: {i}")
        time.sleep(1)

# Creating three threads
threads = []
for i in range(3):
    thread = threading.Thread(target=print_numbers, name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()

# Waiting for all threads to complete
for thread in threads:
    thread.join()

print("All threads have finished execution.")
