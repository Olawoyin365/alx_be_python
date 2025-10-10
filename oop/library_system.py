class Book:
    def __init__(self, title, author):
        self.title = str(title)
        self.author = str(author)

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = int(file_size)

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = int(page_count)

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)

    """def list_books(self):
        for book in self.books:
            print(f"Book: {book.title} by {book.author}")
            
            if hasattr(book, "file_size"):
                print(f"Ebook: {book.title} by {book.author}, File Size: {book.file_size}KB")

            if hasattr(book, "page_count"):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")"""

    def list_books(self):
        for book in self.books:
            book_type = type(book).__name__

            details = f"{book_type}: {book.title} by {book.author}"

            if isinstance(book, EBook):
                details += f", File Size: {book.file_size}KB"

            elif isinstance(book, PrintBook):
                details += f", Page Count: {book.page_count}"

            print(details)
