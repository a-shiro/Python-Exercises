from unittest import TestCase, main
from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train('Thomas', 3)

    def test_constructor(self):
        self.assertEqual('Thomas', self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_when_there_is_no_more_space_left_raises_error(self):
        self.train.passengers = ['Gosho', 'Tosho', 'Pesho']

        with self.assertRaises(ValueError) as cm:
            self.train.add('Kiro')
        self.assertEqual('Train is full', str(cm.exception))

    def test_add_when_the_given_name_is_already_on_board_raises_error(self):
        self.train.passengers = ['Kiro']

        with self.assertRaises(ValueError) as cm:
            self.train.add('Kiro')
        self.assertEqual('Passenger Kiro Exists', str(cm.exception))

    def test_add_passenger_successfully(self):
        result = self.train.add('Toncho')

        self.assertEqual(['Toncho'], self.train.passengers)
        self.assertEqual('Added passenger Toncho', result)

    def test_remove_if_passenger_is_not_on_board(self):
        with self.assertRaises(ValueError) as cm:
            self.train.remove('Ivan')
        self.assertEqual('Passenger Not Found', str(cm.exception))

    def test_remove_passenger_successfully(self):
        self.train.add('Kiro')
        result = self.train.remove('Kiro')

        self.assertEqual([], self.train.passengers)
        self.assertEqual('Removed Kiro', result)


if __name__ == '__main__':
    main()

