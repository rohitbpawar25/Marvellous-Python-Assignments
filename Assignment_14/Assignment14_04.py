# Create a class Student with name, roll_no, and a class variable school_name. Print student details and school name. Change the school name using class name.

class Student:
    school_name = "ABC High School"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def Display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, School: {Student.school_name}")

# Creating objects and displaying details
student1 = Student("Rohit", 101)
student1.Display()

student2 = Student("Amit", 102)
student2.Display()

# Changing school name using class name
Student.school_name = "XYZ International School"

# Displaying updated details
student1.Display()
student2.Display()
