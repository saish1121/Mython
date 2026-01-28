# 1: Write a Python program to implement a class named BookStore with the following specifications:
# • The class should contain two instance variables:
# ◦ Name (Book Name)
# ◦ Author (Book Author)
# • The class should contain one class variable:
# ◦ NoOfBooks (initialize it to 0)
# • Define a constructor (__init__) that accepts Name and Author and initializes instance variables.
# • Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is created.
# • Implement an instance method:
# ◦ Display() – should display book details in the format:
#  <BookName> by <Author>. No of books: <NoOfBooks>

# Example usage:
# Obj1 = BookStore("Linux System Programming", "Robert Love")
# Obj1.Display() # Linux System Programming by Robert Love. No of
# books: 1
# Obj2 = BookStore("C Programming", "Dennis Ritchie")
# Obj2.Display() # C Programming by Dennis Ritchie. No of books: 2

class BookStore:
    NoofBooks = 0
    def __init__(self,A,B):
        self.Name = A
        self.Author = B

        BookStore.NoofBooks = BookStore.NoofBooks + 1

    def Display(self):
        print(self.Name,"By",self.Author)
        print("No of books: ",BookStore.NoofBooks)


Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()

Obj3 = BookStore("Let us C", "Yashavant Kanetkar")
Obj3.Display()

Obj4 = BookStore("Core Python Programming", "Dr .R. Nageswara Rao")
Obj4.Display()

Obj5 = BookStore("Object Oriented Programming with C++", "BalaGuruSwami")
Obj5.Display()

