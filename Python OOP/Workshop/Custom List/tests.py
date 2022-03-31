from unittest import TestCase, main
from custom_list import CustomList


class TestCustomList(TestCase):

    def setUp(self) -> None:
        self.cl = CustomList()

    def test_append_adds_element_to_the_list_when_list_is_empty(self):
        result = self.cl.append(1)

        self.assertEqual(1, result[0])
        self.assertEqual(1, self.cl.get(0))
        self.assertEqual(1, self.cl.size())

    def test_append_adds_element_to_the_list_when_list_is_not_empty(self):
        self.cl.append(1)
        result = self.cl.append(2)

        self.assertEqual([1, 2], result)
        self.assertEqual(2, self.cl.get(1))
        self.assertEqual(2, self.cl.size())

    def test_remove_removes_index_of_the_list(self):
        self.cl.append(1)
        self.cl.remove(0)

        self.assertEqual([], self.cl._CustomList__list_elements)
        self.assertEqual(0, len(self.cl._CustomList__list_elements))



if __name__ == '__main__':
    main()

