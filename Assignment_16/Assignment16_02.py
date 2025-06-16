# Write a program to read and display the contents of a file data.txt.

def main():
    
    fobj = open("Data.txt", 'r')
    Data = fobj.read()
    print("Data in File :")
    print(Data)
    fobj.close()  # <-- Closing the file

if __name__ == "__main__":
    main()
