# Demonstrate private, protected, and public access modifiers using a class Employee with attributes: __salary, _department, and name.

class Employee:
    def __init__(self, name, salary, department):
        self.name = name        # Public attribute
        self.__salary = salary  # Private attribute
        self._department = department  # Protected attribute

    def display(self):
        print(f"Name: {self.name}, Department: {self._department}, Salary: {self.__salary}")

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary!")

    def get_salary(self):
        return self.__salary

# Creating an object and accessing attributes
emp1 = Employee("Rohit", 50000, "IT")
emp1.display()

# Accessing protected attribute
print("Department:", emp1._department)

# Accessing private attribute using getter method
print("Salary:", emp1.get_salary())

# Modifying private attribute using setter method
emp1.set_salary(60000)
print("Updated Salary:", emp1.get_salary())
