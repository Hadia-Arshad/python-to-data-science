 #problem 1 Create a class Student with attributes: name and roll_no. Write a method display() that prints the student's name and roll number.
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def display(self):
        return f"name: {self.name} and roll number: {self.roll_no}"
s1 = Student("hadia", 7)
print(s1.display())
print("THE END")
# problem 2 Create a class Circle with a constructor that accepts the radius as input. Add a method area() that returns the area of the circle (use 3.14 * radius^2).
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        area_of_circle = 3.14*(self.radius**2)
        return area_of_circle
c1 = Circle(5)
print(c1.area())
print("THE END")
#problem 3 Create a class Car with attributes: brand, model, and year. Add a method display_info() to print details. Set default values for brand and model if not provided.
class Car:
    def __init__(self, brand="unknown", model="standard", year=2020):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        return f"brand {self.brand}, model {self.model}, year {self.year}"
c1 = Car("toyota", "Aone", 2021)
print(c1.display_info())
c2 = Car(year=2024)
print(c2.display_info())
print("THE END")
#problem 4 Create a class Animal with a method speak() that prints "Animal sound". Inherit a class Dog from Animal and override the speak() method to print "Bark".
# inheritance basic  creating new class from the existing class
class Animal:
    def speak(self):
        return "Animal sound"
class Dog(Animal):
    def speak(self):
        return "bark"
dog = Dog()
print(dog.speak())
print("THE END")
# problem 5 Create a class BankAccount with attributes: account_holder and balance. Write methods to:
#deposit(amount)
#withdraw(amount)
#display_balance()
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            return f" Deposit: {amount} new balance {self.balance}"
        else:
            print("Invalid deposit amount")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f" withdrawal: {amount} new balance {self.balance}"
        else:
            return "insufficient balance"
    def display_balance(self):
        return f" current balance {self.balance}"
e1 = BankAccount("Hadia", 2000)
print(e1.deposit(1000))
print(e1.withdraw(500))
print(e1.display_balance())
print("THE END")
#problem 6 Create a class Book with attributes title and author. Write a method get_info() that returns the string: "Book: {title}, Author: {author}".
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        return f"Book: {self.title}, author: {self.author}"
b1 = Book("Dastan", "Ameera Ahmad")
print(b1.get_info())
print("THE END")
#problem 7 Create a class Rectangle with attributes length and width. Add a method area() that returns the area of the rectangle.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        area_of_rectangle = self.length * self.width
        return area_of_rectangle
r1 = Rectangle(5, 4)
print(r1.area())
print("THE END")
#problem 8 Create a class Laptop with attributes: brand (default = "Dell"), model (default = "Inspiron"), and price. Add a method show() that returns all the information.
class Laptop:
    def __init__(self, price, brand="Dell", model="inspiron"):
        self.brand = brand
        self.model = model
        self.price = price
    def show(self):
        return f"brand: {self.brand}, model:{self.model}, price: {self.price}"
l1 = Laptop(20000)
print(l1.show())
print("THE END")
#problem 9 Create a class Person with a method greet() that returns "Hello!". Then, create a class Student that inherits from Person and overrides greet() to return "Hi, I am a student!".
class Person():
    def greet(self):
        return "Hello!"
class Student(Person):
    def greet(self):
        return "Hi, I am a student"
s1 = Student()
print(s1.greet())
print("THE END")
#problem 10 Create a class BankAccount as before. Add a method add_interest() that increases the balance by 5%.
class BankAccount:
    def __init__(self, account_holder, balance, interest):
        self.account_holder = account_holder
        self.balance = balance
        self.interest = interest
    def add_interest(self):
        total_interest = self.balance *(self.interest/100)
        return f" account holder: {self.account_holder}, balance: {self.balance}, interest: {total_interest}"
b1 = BankAccount("Hadia",20000, 5 )
print(b1.add_interest())
print("THE END")