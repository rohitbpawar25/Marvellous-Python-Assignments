# Create a class Employee with attributes name, emp_id, and salary. Create objects of this class and print their details using a method.
# Expected Output:
# Name: Rohit, ID: 101, Salary: 50000

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def Display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")

emp1 = Employee("Rohit", 101, 50000)
emp1.Display()

 