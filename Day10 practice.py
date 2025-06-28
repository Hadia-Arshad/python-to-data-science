# some mini projects by using oops in python
# project 1: Contact Book
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def display_info(self):
        return f"name: {self.name} phone: {self.phone} Email: {self.email}"
    def update_no(self, new_number):
        self.phone = new_number
    def update_name(self, new_name):
        self.name = new_name
    def update_mail(self, new_mail):
        self.email = new_mail
c1 = Contact("Hadia", "0300921", "hadia123@gmail.com" )
print(c1.display_info())
c2 = Contact("hamna", "09876", "hamna123@gmail.com")
print(c2.display_info())
c3 = Contact("abuzar", "03459", "abuzar@gmail.com")
print(c3.display_info())
c1.update_no("03421")
print(c1.display_info())
c2.update_name("Arshad")
print(c2.display_info())
c3.update_mail("prince123@gmail.com")
print(c3.display_info())
# project 2: Movie Information
class Movie:
    def __init__(self, title, director, year, rating):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating
    def get_info(self):
        return f"Movie: {self.title}, Director: {self.director}, year: {self.year}, rating: {self.rating}"
    def is_classic(self):
        if self.year < 2000:
            return "yes the movie is classic"
        else:
            return "no movie is not classic"
    def update_Rating(self, new_rating):
        self.rating = new_rating
m1 = Movie("Dilwale", "yashraj", 2000, 7)
print(m1.get_info())
m1.update_Rating(8)
print(m1.get_info())
print(m1.is_classic())
print("THe END")
#   project 3: Bank Account (Simplified)
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def check_balance(self):
        return f"name: {self.name}, balance: {self.balance}"
    def add_deposite(self, amount):
        if amount>0:
            self.balance += amount
            print( f"the deposite {amount} is added now total balance is {self.balance}")
        else:
            print("Not Valid")
    def withdrawal(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"your withdrawal amount is {amount} now your total balance is {self.balance}")
        else:
            print("Not Valid")
e1= BankAccount("Hadia", 2000)
print(e1.check_balance())
e1.add_deposite(2000)
e1.withdrawal(1000)
#project 4:  library mangement

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available= True
    def display_info(self):
        status = "available" if self.available else "Not available"
        return f"title: {self.title}, author: {self.author}, and status: {status}"
class Library:
    def __init__(self):
        self.books =[]
    def add_book(self, book):
        self.books.append(book)
    def display_books(self):
        for book in self.books:
            print(book.display_info())
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                return f"you borrowed {book.title}"
        return "Book not available"
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                return f"you return {book.title}"
        return "Book not found"
b1 = Book("Dastan", "Ameera Ahmad")
b2 = Book("ishqia", "Ameera Ahmad")
b3 = Book("Zindgi", "Ameera Ahmad")
b4 = Book("pyara Afzal", "khalil ur rahman")
lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.add_book(b4)
lib.display_books()
print(lib.borrow_book("ishqia"))
print(lib.borrow_book("Zindgi"))
lib.display_books()
print(lib.return_book("Zindgi"))
lib.display_books()
print("THE END")
# Mini Project 5: Student Grade Report System 
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}
    def enroll_course(self, course, grade=None):
            self.courses[course] = grade
    def get_courses(self):
        return self.courses
class Course:
    def __init__(self, course_name, instructor):
        self.course_name = course_name
        self.instructor = instructor
    def __str__(self):
        return f"{self.course_name} by {self.instructor}"
s1 = Student("Hadia", 7)
c1 = Course("Python", "Ali")
c2 = Course("Java", "Hamna")
s1.enroll_course(c1, "A")
s1.enroll_course(c2, "B+")
print(f"Grade Report for {s1.name}:")
for course, grade in s1.get_courses().items():
    print(f"{course}: Grade = {grade}")
