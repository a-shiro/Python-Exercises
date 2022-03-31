from unittest import TestCase, main
from project import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Peter', 'Lion', 'Roar')

    def test_initializer(self):
        self.assertEqual('Peter', self.mammal.name)
        self.assertEqual('Lion', self.mammal.type)
        self.assertEqual('Roar', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_string_returned_when_you_call_make_sound(self):
        result = self.mammal.make_sound()
        expected = f"{self.mammal.name} makes {self.mammal.sound}"
        self.assertEqual(expected, result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual(self.mammal._Mammal__kingdom, result)

    def test_string_that_info_returns(self):
        result = self.mammal.info()
        expected = f"{self.mammal.name} is of type {self.mammal.type}"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()