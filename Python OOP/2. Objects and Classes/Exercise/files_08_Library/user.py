class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        for name, books_info in library.rented_books.items():
            if book_name in books_info:
                return f'The book "{book_name}" is already rented and will be available in' \
                       f' {library.rented_books[name][book_name]} days!'

        if author not in library.books_available.keys():
            return

        if book_name not in library.books_available[author]:
            return

        self.books.append(book_name)
        library.books_available[author].remove(book_name)

        if self.username not in library.rented_books.keys():
            library.rented_books[self.username] = {}
        library.rented_books[self.username][book_name] = days_to_return

        return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author, book_name, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        self.books.remove(book_name)
        del library.rented_books[self.username][book_name]
        library.books_available[author].append(book_name)

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f'{self.user_id}, {self.username}, {self.books}'