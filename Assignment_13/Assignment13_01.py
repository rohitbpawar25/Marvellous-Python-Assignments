# Write a program which contains one class named as BookStore. BookStore class contains two instance variables as Name, Author. That class contains one class variable as NoOfBooks which is initialized to 0. There is one instance method in the class named Display, which displays Name, Author, and the number of books. Initialize instance variables in the init method by accepting values from the user as Name and Author. Inside the init method, increment the value of NoOfBooks by one. After creating the class, create two objects of the BookStore class as:

'''
Obj1 = BookStore(“Linux System Programming”, “Robert Love”)
Obj1.Display()  # Linux System Programming by Robert Love. No of books: 1

Obj2 = BookStore(“C Programming”, “Dennis Ritchie”)
Obj2.Display()  # C Programming by Dennis Ritchie. No of books: 2

'''

class BookStore:
    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")

Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()
