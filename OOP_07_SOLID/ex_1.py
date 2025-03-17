class NotFoundError(Exception):
    pass


class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page



class Library:
    def __init__(self, books):
        self.books = books

    def find_book(self, title):
        books = [b for b in self.books if b.title == title]
        if books:
            return books[0]
        raise NotFoundError(f"Book with title {title} not found")

    def register_book(self, book: Book):
        self.books.append(book)

    
