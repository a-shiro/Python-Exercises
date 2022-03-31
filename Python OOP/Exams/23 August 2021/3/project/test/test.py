from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library("Dave's")

    def test_constructor(self):
        self.assertEqual("Dave's", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_setter_sets_name_correctly(self):
        self.library.name = "Henry's"
        self.assertEqual("Henry's", self.library.name)

    def test_name_setter_raises_error_when_given_an_empty_string(self):
        with self.assertRaises(ValueError) as cm:
            self.library.name = ''
        self.assertEqual('Name cannot be empty string!', str(cm.exception))

    def test_add_book_adds_author_if_he_is_not_in(self):
        self.library.add_book('John Green', 'The Cloud')
        self.assertEqual({'John Green': ['The Cloud']}, self.library.books_by_authors)

    def test_add_book_adds_book_title_if_it_is_not_in(self):
        self.library.books_by_authors = {'John Green': ['The Cloud']}
        self.library.add_book('John Green', 'The Trap')
        self.assertEqual({'John Green': ['The Cloud', 'The Trap']}, self.library.books_by_authors)

    def test_add_reader_adds_reader_if_reader_in_not_in(self):
        self.library.add_reader('Tony')
        self.assertEqual({'Tony': []}, self.library.readers)

    def test_add_reader_returns_str_that_reader_is_already_in(self):
        self.library.readers = {'Tony': []}
        result = self.library.add_reader('Tony')
        self.assertEqual("Tony is already registered in the Dave's library.", result)

    def test_rent_book_if_reader_is_not_in_returns_str_that_he_is_not_registered(self):
        result = self.library.rent_book('Tony', 'John Green', 'The Cloud')
        self.assertEqual("Tony is not registered in the Dave's Library.", result)

    def test_rent_book_if_author_is_not_in_returns_str_that_library_doesnt_contain_that_authors(self):
        self.library.readers = {'Tony': []}
        result = self.library.rent_book('Tony', 'John Green', 'The Cloud')
        self.assertEqual("Dave's Library does not have any John Green's books.", result)

    def test_rent_book_if_book_title_is_not_in_returns_str_that_library_doesnt_contain_that_book(self):
        self.library.readers = {'Tony': []}
        self.library.books_by_authors = {'John Green': []}
        result = self.library.rent_book('Tony', 'John Green', 'The Cloud')
        self.assertEqual("""Dave's Library does not have John Green's "The Cloud".""", result)

    def test_rent_book_adds_it_to_the_readers_books_and_removes_it_from_the_library(self):
        self.library.books_by_authors = {'John Green': ['The Cloud']}
        self.library.readers = {'Bob': []}

        self.library.rent_book('Bob', 'John Green', 'The Cloud')
        self.assertEqual({'Bob': [{'John Green': 'The Cloud'}]}, self.library.readers)
        self.assertEqual({'John Green': []}, self.library.books_by_authors)


if __name__ == '__main__':
    main()