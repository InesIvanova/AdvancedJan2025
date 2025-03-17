from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass

class InstagramFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:10]


class PaperFormat(BaseFormatter):
    def format(self, book: Book):
        return book.content[10:] + book.content[:10]


class Printer:
    def get_book(self, book: Book, formatter: BaseFormatter):
        formatted_book = formatter.format(book)
        return formatted_book


p = Printer()

f= InstagramFormatter()
pf = PaperFormat()
b= Book("Very long content so that we have 20 chars")

print(p.get_book(b, pf))