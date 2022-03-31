class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class TestIntegerList(TestCase):
    def setUp(self) -> None:
        self.int_list = IntegerList(1, 2, 3)

    def test_constructor(self):
        self.assertEqual([1, 2, 3], self.int_list._IntegerList__data)

    def test_constructor_with_string(self):
        int_list = IntegerList('a', 'b', 3)
        self.assertEqual([3], int_list._IntegerList__data)

    def test_add_operation_adds_integer(self): # res test?
        self.int_list.add(4)
        self.assertEqual([1, 2, 3, 4], self.int_list._IntegerList__data)

    def test_add_operation_adds_data_type_different_than_integer_raises_error(self):
        # Example 1
        with self.assertRaises(ValueError) as ex:
            self.int_list.add('4')
        self.assertEqual('Element is not Integer', str(ex.exception))

        # Example 2
        with self.assertRaises(ValueError) as ex:
            self.int_list.add(5.4)
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_remove_index_removes_the_integer_ont_the_index(self):
        self.int_list.remove_index(0)
        self.assertEqual([2, 3], self.int_list._IntegerList__data)

    def test_remove_index_with_out_of_range_index(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(100)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_get_returns_specified_index(self):
        res = self.int_list.get(1)
        self.assertEqual(2, res)

    def test_get_if_given_out_of_range_index(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.get(10)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert_specified_el_on_specified_position(self):
        self.int_list.insert(1, 4)
        self.assertEqual([1, 4, 2, 3], self.int_list._IntegerList__data)

    def test_insert_with_index_out_of_range(self):

        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(10, 4)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert_with_element_that_is_not_int(self):
        # Example 1
        with self.assertRaises(ValueError) as ex:
            self.int_list.insert(1, '4')
        self.assertEqual('Element is not Integer', str(ex.exception))

        # Example 2
        with self.assertRaises(ValueError) as ex:
            self.int_list.insert(1, 5.4)
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_get_biggest_integer(self):
        res = self.int_list.get_biggest()
        self.assertEqual(3, res)

    def test_get_index_of_element(self):
        index = self.int_list.get_index(3)
        self.assertEqual(2, index)


if __name__ == '__main__':
    main()

