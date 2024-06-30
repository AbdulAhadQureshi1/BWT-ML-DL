class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Getter methods
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_pages(self):
        return self.pages

    # Setter methods
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_pages(self, pages):
        self.pages = pages

    @classmethod
    def calculate_reading_time(cls, pages, reading_speed=250):
        return cls.pages / reading_speed

# Creating an instance of Book
my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)

# Using getter methods
print(f"Title: {my_book.get_title()}")
print(f"Author: {my_book.get_author()}")
print(f"Pages: {my_book.get_pages()}")

# Using setter methods
my_book.set_title("New Title")
my_book.set_author("New Author")
my_book.set_pages(200)

# Updated information
print(f"\nUpdated Information:")
print(f"Title: {my_book.get_title()}")
print(f"Author: {my_book.get_author()}")
print(f"Pages: {my_book.get_pages()}")

class Ebook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages, Format: {self.format}"

# Creating an instance of Ebook
my_ebook = Ebook("1984", "George Orwell", 328, "PDF")

# Displaying the Ebook details using the overridden __str__() method
print(my_ebook)
