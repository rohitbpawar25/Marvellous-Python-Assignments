# Write a Python program to create a text file named student.txt and write the names of 5 students into it.
    
def main():
    
    fobj = open('student.txt', 'w')
    students = ["Rohit", "Sneha", "Aditi", "Yashraj", "Arbaj"]
    for name in students:
        fobj.write(name + '\n')
    fobj.close()

if __name__ == "__main__":
    main()
