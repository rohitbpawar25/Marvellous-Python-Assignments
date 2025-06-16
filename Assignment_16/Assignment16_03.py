# Write a Python script to count the number of lines, words, and characters in a given file.

def main():
    fobj = open("Data.txt", 'r')
    lines = fobj.readlines()

    Count_line = len(lines)
    Count_Words = sum(len(line.split()) for line in lines)
    Count_Characters = sum(len(line) for line in lines)

    print(f"Total Lines: {Count_line}")
    print(f"Total Words: {Count_Words}")
    print(f"Total Characters: {Count_Characters}")

    fobj.close()

if __name__ == "__main__":
    main()
