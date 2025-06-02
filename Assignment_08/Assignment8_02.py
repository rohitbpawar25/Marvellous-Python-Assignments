# Design a Python application that creates two threads named evenfactor and oddfactor. Both threads accept one integer parameter. The evenfactor thread will display the sum of all even factors of the given number, while the oddfactor thread will display the sum of all odd factors of the given number. After both threads complete execution, the main thread should display the message 'exit from main

import threading

def even_factors_sum(num):
    even_sum = sum(factor for factor in range(1, num + 1) if num % factor == 0 and factor % 2 == 0)
    print(f"Sum of even factors of {num}: {even_sum}")

def odd_factors_sum(num):
    odd_sum = sum(factor for factor in range(1, num + 1) if num % factor == 0 and factor % 2 != 0)
    print(f"Sum of odd factors of {num}: {odd_sum}")

num = int(input("Enter a number: "))

even_thread = threading.Thread(target=even_factors_sum, args=(num,), name="evenfactor")
odd_thread = threading.Thread(target=odd_factors_sum, args=(num,), name="oddfactor")

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()

print("Exit from main")
