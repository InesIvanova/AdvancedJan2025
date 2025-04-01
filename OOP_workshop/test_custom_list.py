from unittest import TestCase, main

from OOP_workshop.custom_list import CustomList


class TestCustomList(TestCase):
    def setUp(self):
        self.cl = CustomList(1, -1, 5, 3)

    def test_init(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

    def test_append(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

        result = self.cl.append(10)

        self.assertEqual([1, -1, 5, 3, 10], self.cl._CustomList__data)
        self.assertEqual([1, -1, 5, 3, 10], result)

    def test_remove(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

        element = self.cl.remove(1)

        self.assertEqual([1, 5, 3], self.cl._CustomList__data)
        self.assertEqual(-1, element)

    def test_get(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

        element = self.cl.get(1)

        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)
        self.assertEqual(-1, element)

    def test_extend(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

        nums = [100, 200]

        result = self.cl.extend(nums)

        self.assertEqual([1, -1, 5, 3, 100, 200], self.cl._CustomList__data)
        self.assertEqual([1, -1, 5, 3, 100, 200], result)

    def test_insert(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

        result = self.cl.insert(1, 100)

        self.assertEqual([1, 100, -1, 5, 3], self.cl._CustomList__data)
        self.assertEqual([1, 100, -1, 5, 3], result)

    def test_pop(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

        result = self.cl.pop()
        self.assertEqual([1, -1, 5], self.cl._CustomList__data)
        self.assertEqual(3, result)

    def test_clear(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

        result = self.cl.clear()

        self.assertEqual([], self.cl._CustomList__data)
        self.assertIsNone(result)

    def test_index(self):
        self.cl.append(1)
        self.assertEqual([1, -1, 5, 3, 1], self.cl._CustomList__data)

        result = self.cl.index(1)

        self.assertEqual(0, result)
        self.assertEqual([1, -1, 5, 3, 1], self.cl._CustomList__data)

    def test_count(self):
        self.cl.append(1)
        self.assertEqual([1, -1, 5, 3, 1], self.cl._CustomList__data)

        result = self.cl.count(1)

        self.assertEqual(2, result)
        self.assertEqual([1, -1, 5, 3, 1], self.cl._CustomList__data)

    def test_reverse(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

        result = self.cl.reverse()

        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)
        self.assertEqual([3, 5, -1, 1], result)

    def test_copy(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

        result = self.cl.copy()

        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)
        self.assertEqual([1, -1, 5, 3], result)

        self.assertNotEqual(id(result), id(self.cl._CustomList__data))

    def test_size(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

        result = self.cl.size()

        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)
        self.assertEqual(4, result)

    def test_add_first(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

        result = self.cl.add_first(100)

        self.assertEqual([100, 1, -1, 5, 3], self.cl._CustomList__data)
        self.assertIsNone(result)

    def test_dictionize(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

        result = self.cl.dictionize()
        self.assertEqual({1: -1, 5: 3}, result)

        self.cl.remove(3)
        self.assertEqual([1, -1, 5], self.cl._CustomList__data)

        result = self.cl.dictionize()
        self.assertEqual({1: -1, 5: " "}, result)

    def test_move_n_elements(self):
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)

        result = self.cl.move(3)
        self.assertEqual([1, -1, 5, 3], self.cl._CustomList__data)
        self.assertEqual([3, 1, -1, 5], result)

    def test_sum(self):
        custom_list = CustomList(1, "asd", [1,2,3,4,5,6], 4)

        result = custom_list.sum()

        self.assertEqual(14, result)

    def test_overbound(self):
        custom_list = CustomList(1, "asd", [1,2,3,4,5,6], 4)

        result = custom_list.overbound()

        self.assertEqual(2, result)

    def test_underbound(self):
        custom_list = CustomList(1, "asd", [1,2,3,4,5,6], 4)

        result = custom_list.underbound()

        self.assertEqual(0, result)

    def test_underbound_with_str(self):
        custom_list = CustomList(5, "asd", [1, 2, 3, 4, 5, 6], 4)

        result = custom_list.underbound()

        self.assertEqual(1, result)


if __name__ == "__main__":
    main()