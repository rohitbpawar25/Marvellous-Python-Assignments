# Create a base class Person with attributes name and age. Derive a class Teacher with subject and salary. Use super() to call base class constructor and print both.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display(self):
        super().display()
        print(f"Subject: {self.subject}, Salary: {self.salary}")

# Creating an object and calling methods
teacher1 = Teacher("Rohit", 35, "Mathematics", 60000)
teacher1.display()
