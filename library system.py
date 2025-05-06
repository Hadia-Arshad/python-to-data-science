class Library:
    def __init__(self):
        self.books = []
    def add_books(self, book_name):
        self.books.append(book_name)
    def get_no_of_books(self):
        return len(self.books)
    def print_books(self):
        for book in self.books:
            print(book)
my_library = Library()
my_library.add_books("pakistan studies")
my_library.add_books("islamic studies")
my_library.add_books("History")
my_library.add_books("English")
my_library.print_books()
print("Total numbers of books:", my_library.get_no_of_books())