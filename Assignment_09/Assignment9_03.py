# Create a Python program that uses multiprocessing.Pool to compute factorial of numbers in a list.

import multiprocessing

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    numbers = [3, 4, 5, 6]  # Example list of numbers

    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)

    print("Factorials:", results)
