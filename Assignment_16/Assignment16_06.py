# Q6: Write a Python program to copy the contents of one file (source.txt) into another file (destination.txt).

def Copy_Contest(Input1, Input2):
    fobj = open(Input1, 'r')
    fobj1 = open(Input2, 'w')
    fobj1.write(fobj.read())
    fobj.close()
    fobj1.close()
    print("File copied successfully")

def main():
    Copy_Contest("Source.txt", "Destination.txt")

if __name__ == "__main__":
    main()
