# Design a Python application that creates two threads named evenlist and oddlist. Both threads accept a list of integers as a parameter. The evenlist thread should add all even elements from the input list and display the sum, while the oddlist thread should add all odd elements from the input list and display the sum

import threading

def even_list_sum(numbers):
    even_sum = sum(num for num in numbers if num % 2 == 0)
    print(f"Sum of even numbers: {even_sum}")

def odd_list_sum(numbers):
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    print(f"Sum of odd numbers: {odd_sum}")

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even_thread = threading.Thread(target=even_list_sum, args=(numbers,), name="evenlist")
odd_thread = threading.Thread(target=odd_list_sum, args=(numbers,), name="oddlist")

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()

print("Exit from main")
