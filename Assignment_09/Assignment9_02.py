# write a Python program using multiprocessing.Process to square a list of numbers using multiple processes.

import multiprocessing

def square_number(n):
    print(f"Process {multiprocessing.current_process().name}: {n}² = {n * n}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    
    processes = []
    for num in numbers:
        process = multiprocessing.Process(target=square_number, args=(num,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All processes have finished execution.")
