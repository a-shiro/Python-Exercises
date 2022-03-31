# Original Code:


# class Book:
#     def __init__(self, content: str):
#         self.content = content
#
#
# class Formatter:
#     def format(self, book: Book) -> str:
#         return book.content
#
#
# class Printer:
#     def get_book(self, book: Book):
#         formatter = Formatter()
#         formatted_book = formatter.format(book)
#         return formatted_book


# Refactored Code


from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    @staticmethod
    @abstractmethod
    def format(book: Book) -> str:
        pass


class MobileFormatter(Formatter):
    @staticmethod
    def format(book: Book) -> str:
        return book.content[:10]


class DesktopFormatter(Formatter):
    @staticmethod
    def format(book: Book) -> str:
        return book.content[11:]


class Printer:
    @staticmethod
    def get_book(book: Book, formatter: Formatter):
        return formatter.format(book)


book1 = Book('Formatter1 Formatter2')
printer = Printer
formatter1 = MobileFormatter()
formatter2 = DesktopFormatter()


print(printer.get_book(book1, formatter1))
print(printer.get_book(book1, formatter2))
