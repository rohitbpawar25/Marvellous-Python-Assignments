# Write a function that accepts a string and checks whether it is a palindrome.

Palindrome = lambda Char : Char[::-1]

def main():
    
    Input = str(input("Enter a String :"))
    Str = Palindrome(Input)
    print(Str,"is Palandrome")

if __name__ == "__main__":
    main()