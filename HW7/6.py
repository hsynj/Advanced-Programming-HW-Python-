class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __repr__(self):
        return f"Book({self.title}, {self.author})"
    

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def borrowed_book(self, book_name):
        for book in self.books:
            if book.title == book_name:
                if book.is_borrowed:
                    print(f"{book.title} by {book.author} is already borrowed.")
                    return
                else:
                    book.is_borrowed = True
                    print(f"{book.title} by {book.author} has been borrowed.")
                    return
        print(f"{book_name} is not available in the library.")
            
    def get_back(self, book_name):
        for book in self.books:
            if book.title == book_name:
                if not book.is_borrowed:
                    print(f"{book.title} by {book.author} is not borrowed for you.")
                    return
                else:
                    book.is_borrowed = False
                    print(f"{book.title} by {book.author} has been returned.")
                    return
        print(f"{book_name} is not available in the library.")

    def __str__(self):
        if not self.books:
            return "No books available in the library."
        else:
            book_list = [f"{book.title} by {book.author} - {'Borrowed' if book.is_borrowed else 'Available'}" for book in self.books]
            return "\n".join(book_list)

    def __repr__(self):
        return f"Library({self.books})"
    

# Example usage
if __name__ == "__main__":
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    print(library)
    library.borrowed_book("The Great Gatsby")
    library.get_back("1984")