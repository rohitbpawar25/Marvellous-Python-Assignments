# Create a file marks.txt with student name and marks. Then read the file and display students who scored more than 75 marks

def main():
    
    fobj = open("marks.txt", "w")
    fobj.write("Rohit 82\nSneha 67\nAarav 91\nPriya 76\nKunal 58\n")
    fobj.close()

    fobj = open("marks.txt", "r")
    for line in fobj:
        name, marks = line.split()
        marks = int(marks)
        if marks > 75:
            print(f"{name} scored {marks} marks")
    fobj.close()

if __name__ == "__main__":
    main()
