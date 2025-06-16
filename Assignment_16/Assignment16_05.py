# Write a program to read a file line by line and display only those lines that contain more than 5 words.

def Display_line(filename):
    
    fobj = open(filename, "r")
    for line in fobj:
        words = line.split()
        if len(words) > 5:
            print(line.strip())
    fobj.close()

def main():
    Display_line("Data.txt")

if __name__ == "__main__":
    main()
