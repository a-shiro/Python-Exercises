import sys
from numbers import Number


class CustomList:
    def __init__(self):
        self.__list_elements = []

    def append(self, value):
        self.__list_elements.append(value)
        return self.__list_elements

    def remove(self, index):
        return self.__list_elements.pop(index)

    def get(self, index):
        return self.__list_elements[index]

    def extend(self, iterable):
        self.__list_elements.extend(iterable)
        return self.__list_elements

    def insert(self, index, value):
        self.__list_elements.insert(index, value)
        return self.__list_elements

    def pop(self):
        return self.__list_elements.pop()

    def clear(self):
        self.__list_elements.clear()

    def index(self, value):
        return self.__list_elements.index(value)

    def count(self, value):
        return self.__list_elements.count(value)

    def reverse(self):
        return self.__list_elements[::-1]

    def copy(self):
        return self.__list_elements.copy()

    def size(self):
        return len(self.__list_elements)

    def add_first(self, value):
        self.__list_elements = [value] + self.__list_elements

    def dictionize(self):
        result = {}
        previous_key = ''

        for idx, value in enumerate(self.__list_elements):
            if idx % 2 == 0:
                result[value] = ' '
                previous_key = value
            else:
                result[previous_key] = value
        return result

    def move(self, amount):
        self.__list_elements = self.__list_elements[amount:] + self.__list_elements[:amount]
        return self.__list_elements

    def sum(self):
        result = 0

        for el in self.__list_elements:
            if not isinstance(el, Number):
                result += len(el)
            else:
                result += el
        return result

    def overbound(self):
        if len(self.__list_elements) == 0:
            raise IndexError('Custom list is empty.')

        biggest_value = -sys.maxsize
        biggest_value_idx = None

        for index, value in enumerate(self.__list_elements):
            if not isinstance(value, Number):
                if biggest_value < len(value):
                    biggest_value = len(value)
                    biggest_value_idx = index
            else:
                if biggest_value < value:
                    biggest_value = value
                    biggest_value_idx = index
        return biggest_value_idx

    def underbound(self):
        if len(self.__list_elements) == 0:
            raise IndexError('Custom list is empty.')

        smallest_value = sys.maxsize
        smallest_value_idx = None

        for index, value in enumerate(self.__list_elements):
            if not isinstance(value, Number):
                if smallest_value > len(value):
                    smallest_value = len(value)
                    smallest_value_idx = index
            else:
                if smallest_value > value:
                    smallest_value = value
                    smallest_value_idx = index
        return smallest_value_idx
