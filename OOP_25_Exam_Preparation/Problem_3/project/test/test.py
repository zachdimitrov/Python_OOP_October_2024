from unittest import TestCase, main

from project.furniture import Furniture


class FurnitureTests(TestCase):
    def setUp(self):
        self.f = Furniture("Test", 100, (3, 4, 5))

    def test_init(self):
        self.assertEqual("Test", self.f.model)
        self.assertEqual(100, self.f.price)
        self.assertEqual((3, 4, 5), self.f.dimensions)
        self.assertEqual(True, self.f.in_stock)
        self.assertEqual(None, self.f.weight)

    def test_model_too_long_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.f.model = "Ttttttttttttttteeeeeeeeeeeeeesssssssssssssssttttttttttttttt"
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))

    def test_model_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.f.model = ""
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))

    def test_model_setter(self):
        self.f.model = "NewModel"
        self.assertEqual("NewModel", self.f.model)

    def test_price_less_than_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.f.price = -1
        self.assertEqual("Price must be a non-negative number.", str(ex.exception))

    def test_price_setter(self):
        self.f.price = 200
        self.assertEqual(200, self.f.price)

    def test_dimensions_wrong_tuple_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.f.dimensions = (2, 3)
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ex.exception))

    def test_dimensions_not_positive_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.f.dimensions = (-2, 3, 4)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))

    def test_dimensions_setter(self):
        self.f.dimensions = (5, 6, 7)
        self.assertEqual((5, 6, 7), self.f.dimensions)

    def test_weight_less_than_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.f.weight = -1
        self.assertEqual("Weight must be greater than zero.", str(ex.exception))

    def test_weight_is_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.f.weight = 0
        self.assertEqual("Weight must be greater than zero.", str(ex.exception))

    def test_weight_setter(self):
        self.f.weight = 100
        self.assertEqual(100, self.f.weight)

    def test_get_available_status_if_available(self):
        result = self.f.get_available_status()
        self.assertEqual("Model: Test is currently in stock.", result)

    def test_get_available_status_if_not_available(self):
        self.f.in_stock = False
        result = self.f.get_available_status()
        self.assertEqual("Model: Test is currently unavailable.", result)

    def test_get_specifications_if_no_weight(self):
        result = self.f.get_specifications()
        self.assertEqual("Model: Test has the following dimensions: 3mm x 4mm x 5mm and weighs: N/A", result)

    def test_get_specifications(self):
        self.f.weight = 100
        result = self.f.get_specifications()
        self.assertEqual("Model: Test has the following dimensions: 3mm x 4mm x 5mm and weighs: 100", result)


if __name__ == "__main__":
    main()
