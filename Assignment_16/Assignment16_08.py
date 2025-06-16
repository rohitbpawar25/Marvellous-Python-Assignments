# Write a script to remove all blank lines from a file. Save the cleaned output to a new file.

def Remove_Blank(File1,File2):
    fobj1 = open(File1, "r")
    fobj2 = open(File2, "w")

    for line in fobj1:
        if line.strip():
            fobj2.write(line)

    fobj1.close()
    fobj2.close()

    print(f"Blank lines removed. Cleaned file saved as '{File2}'")

def main():
    Remove_Blank("Data.txt", "Cleaned_data.txt")

if __name__ == "__main__":
    main()

    