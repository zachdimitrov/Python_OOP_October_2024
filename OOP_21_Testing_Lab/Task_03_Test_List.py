from extended_list import IntegerList
from unittest import TestCase, main


class IntegerListTests(TestCase):
    def setUp(self):
        self.int_list = IntegerList(4, -2, 15, 200)

    def test_init_stores_only_int(self):
        # No args
        i = IntegerList()
        self.assertEqual(i._IntegerList__data, [])

        # With args
        i = IntegerList(1, "str", 1.5, [1, 2, 3])
        self.assertEqual(i._IntegerList__data, [1])

    def test_get_data(self):
        result = self.int_list.get_data()
        expected = [4, -2, 15, 200]
        self.assertEqual(expected, result)

    def test_add_not_int_raises(self):
        result = self.int_list.get_data()
        expected = [4, -2, 15, 200]
        self.assertEqual(expected, result)

        # Act
        with self.assertRaises(ValueError) as ex:
            self.int_list.add("str")
        self.assertEqual(str(ex.exception), "Element is not Integer")

        result = self.int_list.get_data()
        expected = [4, -2, 15, 200]
        self.assertEqual(expected, result)

    def test_add(self):
        result = self.int_list.get_data()
        expected = [4, -2, 15, 200]
        self.assertEqual(expected, result)

        self.int_list.add(1)
        result = self.int_list.get_data()
        expected = [4, -2, 15, 200, 1]
        self.assertEqual(expected, result)
        self.assertEqual(self.int_list._IntegerList__data, expected)

    def test_remove_index_invalid_idx_raises(self):
        # index = len
        self.assertEqual(len(self.int_list.get_data()), 4)
        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(4)
        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.int_list.get_data()), 4)
        # index is greater than len
        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(5)
        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.int_list.get_data()), 4)

    def test_remove_index(self):
        self.assertEqual(self.int_list.get_data()[2], 15)
        self.assertEqual(len(self.int_list.get_data()), 4)
        result = self.int_list.remove_index(2)
        self.assertEqual(result, 15)
        self.assertEqual(self.int_list.get_data()[2], 200)
        self.assertEqual(len(self.int_list.get_data()), 3)

    def test_get_invalid_index_raises(self):
        # index = len
        self.assertEqual(len(self.int_list.get_data()), 4)
        with self.assertRaises(IndexError) as ex:
            self.int_list.get(4)
        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.int_list.get_data()), 4)
        # index is greater than len
        with self.assertRaises(IndexError) as ex:
            self.int_list.get(5)
        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.int_list.get_data()), 4)

    def test_get(self):
        self.assertEqual(len(self.int_list.get_data()), 4)
        self.assertEqual(self.int_list.get_data()[2], 15)

        result = self.int_list.get(2)

        self.assertEqual(result, 15)
        self.assertEqual(len(self.int_list.get_data()), 4)

    def test_insert_invalid_index_raises(self):
        # index = len
        self.assertEqual(len(self.int_list.get_data()), 4)
        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(4, 101)
        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.int_list.get_data()), 4)
        # index is greater than len
        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(5, 101)
        self.assertEqual(str(ex.exception), "Index is out of range")
        self.assertEqual(len(self.int_list.get_data()), 4)

    def test_insert_invalid_value_raises(self):
        self.assertEqual(len(self.int_list.get_data()), 4)
        with self.assertRaises(ValueError) as ex:
            self.int_list.insert(2, "str")
        self.assertEqual(str(ex.exception), "Element is not Integer")
        self.assertEqual(len(self.int_list.get_data()), 4)

    def test_insert(self):
        self.assertEqual(len(self.int_list.get_data()), 4)
        self.assertEqual(self.int_list.get_data()[2], 15)
        self.int_list.insert(2, 101)
        self.assertEqual(self.int_list.get_data()[2], 101)

    def test_get_biggest(self):
        result = self.int_list.get_biggest()
        self.assertEqual(result, 200)
        self.int_list.insert(2, 1000)
        result = self.int_list.get_biggest()
        self.assertEqual(result, 1000)

    def test_get_index(self):
        self.assertEqual(self.int_list.get_data()[2], 15)
        result = self.int_list.get_index(15)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    main()
