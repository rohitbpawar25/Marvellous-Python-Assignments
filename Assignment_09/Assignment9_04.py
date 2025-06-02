# Create a Python program that compares execution time of summing numbers from 1 to 10 million using normal function, threading, and multiprocessing.

import threading
import multiprocessing
import time

# Normal function
def sum_numbers(n):
    return sum(range(1, n + 1))

# Threading function
def sum_threading(n, result):
    result.append(sum_numbers(n))

# Multiprocessing function
def sum_multiprocessing(n, queue):
    queue.put(sum_numbers(n))

if __name__ == "__main__":
    N = 10_000_000

    # Normal execution
    start_time = time.time()
    normal_result = sum_numbers(N)
    normal_time = time.time() - start_time
    print(f"Normal Execution Time: {normal_time:.4f} seconds")

    # Threading execution
    start_time = time.time()
    result = []
    thread = threading.Thread(target=sum_threading, args=(N, result))
    thread.start()
    thread.join()
    threading_time = time.time() - start_time
    print(f"Threading Execution Time: {threading_time:.4f} seconds")

    # Multiprocessing execution
    start_time = time.time()
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=sum_multiprocessing, args=(N, queue))
    process.start()
    process.join()
    multiprocessing_time = time.time() - start_time
    print(f"Multiprocessing Execution Time: {multiprocessing_time:.4f} seconds")
