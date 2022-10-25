class Library:
    def __init__(self, name): # test constructor 1
        self.name = name
        self.books_by_authors = {}
        self.readers = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value): # test setter 2
        if value == '': # 1
            raise ValueError("Name cannot be empty string!")
        self.__name = value # 2

    def add_book(self, author, title): # test add book 2
        if author not in self.books_by_authors: # 1
            self.books_by_authors[author] = []
        if title not in self.books_by_authors[author]: # 2
            self.books_by_authors[author].append(title)

    def add_reader(self, name): # test add reader 2
        if name not in self.readers: # 1
            self.readers[name] = []
        else: # 2
            return f"{name} is already registered in the {self.name} library."

    def rent_book(self, reader_name, book_author, book_title): # test rent book 4
        if reader_name not in self.readers: # 1
            return f"{reader_name} is not registered in the {self.name} Library."
        if book_author not in self.books_by_authors: # 2
            return f"{self.name} Library does not have any {book_author}'s books."
        if book_title not in self.books_by_authors[book_author]: # 3
            return f"""{self.name} Library does not have {book_author}'s "{book_title}"."""
        self.readers[reader_name].append({book_author: book_title}) # 4
        book_title_index = self.books_by_authors[book_author].index(book_title)
        del self.books_by_authors[book_author][book_title_index]
