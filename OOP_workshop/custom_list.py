from copy import deepcopy


class CustomList:
    def __init__(self, *args):
        self.__data = list(args)

    def append(self, value):
        self.__data.append(value)
        return self.__data

    def remove(self, index):
        el = self.__data[index]
        del self.__data[index]
        return el

    def get(self, index):
        return self.__data[index]

    def extend(self, data):
        self.__data.extend(data)
        return self.__data

    def insert(self, index, el):
        self.__data.insert(index, el)
        return self.__data

    def pop(self):
        return self.__data.pop()

    def clear(self):
        self.__data.clear()

    def index(self, el):
        return self.__data.index(el)

    def count(self, el):
        return self.__data.count(el)

    def reverse(self):
        return list(reversed(self.__data))

    def copy(self):
        return deepcopy(self.__data)

    def size(self):
        return len(self.__data)

    def add_first(self, element):
        self.insert(0, element)

    def dictionize(self):
        data = {}
        for index in range(0, self.size(), 2):
            key = self.__data[index]
            try:
                value = self.__data[index+1]
            except IndexError:
                value = " "
            data[key] = value
        return data

    def move(self, count):
        first_part = self.__data[:count]
        second_part = self.__data[count:]

        return second_part + first_part

    def sum(self):
        total_sum = 0
        for el in self.__data:
            if isinstance(el, int) or isinstance(el, float):
                total_sum += el
            else:
                total_sum += len(el)
        return total_sum

    def overbound(self):
        max_num = float("-inf")
        biggest_el = None
        for el in self.__data:
            if isinstance(el, int) or isinstance(el, float):
                if el>= max_num:
                    max_num = el
                    biggest_el = el
            else:
                if len(el)>=max_num:
                    max_num = len(el)
                    biggest_el = el
        return self.index(biggest_el)

    def underbound(self):
        min_num = float("inf")
        smallest_el = None
        for el in self.__data:
            if isinstance(el, int) or isinstance(el, float):
                if min_num >=el:
                    min_num = el
                    smallest_el = el
            else:
                if min_num >=len(el):
                    min_num = len(el)
                    smallest_el = el
        return self.index(smallest_el)

