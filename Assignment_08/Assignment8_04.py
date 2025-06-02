# "Design a Python application that creates three threads named small, capital, and digits. Each thread accepts a string as a parameter. The small thread should display the number of lowercase characters, the capital thread should display the number of uppercase characters, and the digits thread should display the number of digits. Additionally, display the ID and name of each thread

import threading

def count_small_chars(text):
    small_count = sum(1 for char in text if char.islower())
    print(f"Small characters: {small_count}, Thread ID: {threading.get_ident()}, Name: {threading.current_thread().name}")

def count_capital_chars(text):
    capital_count = sum(1 for char in text if char.isupper())
    print(f"Capital characters: {capital_count}, Thread ID: {threading.get_ident()}, Name: {threading.current_thread().name}")

def count_digits(text):
    digit_count = sum(1 for char in text if char.isdigit())
    print(f"Digits: {digit_count}, Thread ID: {threading.get_ident()}, Name: {threading.current_thread().name}")

text = input("Enter a string: ")

small_thread = threading.Thread(target=count_small_chars, args=(text,), name="small")
capital_thread = threading.Thread(target=count_capital_chars, args=(text,), name="capital")
digits_thread = threading.Thread(target=count_digits, args=(text,), name="digits")

small_thread.start()
capital_thread.start()
digits_thread.start()

small_thread.join()
capital_thread.join()
digits_thread.join()

print("Exit from main")
