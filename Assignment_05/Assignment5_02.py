# Write a program to accept a single character from the user and check if it is a vowel (a, e, i, o, u). If not, print that it's a consonant.

def ChkVowel(Char):
    if Char in ["A","a","E","e","I","i","O","o","U","u"]:
        return ("Vowel")
    else:
        return("consonant")

def main():

    Str  = str(input("Enter Character :"))
    result = ChkVowel(Str)
    print("Character is :",result)

if __name__ == "__main__":
    main()