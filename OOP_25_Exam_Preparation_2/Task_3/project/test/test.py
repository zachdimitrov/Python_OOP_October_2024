from unittest import TestCase, main
from project.restaurant import Restaurant


class RestaurantTests(TestCase):
    def setUp(self):
        self.r = Restaurant("Test", 10)
        self.waiters = [{"name": "Gosho", "total_earnings": 10},
                        {"name": "Pesho", "total_earnings": 20},
                        {"name": "Alex", "total_earnings": 30},
                        {"name": "Ivan", "total_earnings": 40},
                        {"name": "Drago", "total_earnings": 50}]

    def test_init(self):
        self.assertEqual("Test", self.r.name)
        self.assertEqual(10, self.r.capacity)
        self.assertEqual([], self.r.waiters)

    def test_name_empty_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.r.name = ""
        self.assertEqual("Invalid name!", str(ex.exception))

    def test_name_with_intervals_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.r.name = "     "
        self.assertEqual("Invalid name!", str(ex.exception))

    def test_name_setter(self):
        self.assertEqual("Test", self.r.name)
        self.r.name = "NewName"
        self.assertEqual("NewName", self.r.name)

    def test_capacity_invalid_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.r.capacity = -1
        self.assertEqual("Invalid capacity!", str(ex.exception))

    def test_capacity_setter(self):
        self.assertEqual(10, self.r.capacity)
        self.r.capacity = 20
        self.assertEqual(20, self.r.capacity)

    def test_get_waiters_all(self):
        self.r.waiters = self.waiters
        result = self.r.get_waiters()
        self.assertEqual([{"name": "Gosho", "total_earnings": 10},
                          {"name": "Pesho", "total_earnings": 20},
                          {"name": "Alex", "total_earnings": 30},
                          {"name": "Ivan", "total_earnings": 40},
                          {"name": "Drago", "total_earnings": 50}], result)

    def test_get_waiters_filtered(self):
        self.r.waiters = self.waiters
        result = self.r.get_waiters(20, 40)
        self.assertEqual([{"name": "Pesho", "total_earnings": 20},
                          {"name": "Alex", "total_earnings": 30},
                          {"name": "Ivan", "total_earnings": 40}], result)

    def test_add_waiter_no_capacity(self):
        self.r.capacity = 1
        self.r.add_waiter("Ivan")
        self.assertEqual([{"name": "Ivan"}], self.r.waiters)
        result = self.r.add_waiter("Gosho")
        self.assertEqual("No more places!", result)

    def test_add_waiter_if_exists(self):
        self.r.add_waiter("Ivan")
        self.assertEqual([{"name": "Ivan"}], self.r.waiters)
        result = self.r.add_waiter("Ivan")
        self.assertEqual("The waiter Ivan already exists!", result)

    def test_add_waiter(self):
        result = self.r.add_waiter("Ivan")
        self.assertEqual("The waiter Ivan has been added.", result)
        self.assertEqual([{"name": "Ivan"}], self.r.waiters)

    def test_remove_waiter_not_existing(self):
        self.assertEqual([], self.r.waiters)
        result = self.r.remove_waiter("Ivan")
        self.assertEqual("No waiter found with the name Ivan.", result)

    def test_remove_waiter(self):
        self.r.add_waiter("Ivan")
        self.assertEqual([{"name": "Ivan"}], self.r.waiters)
        result = self.r.remove_waiter("Ivan")
        self.assertEqual("The waiter Ivan has been removed.", result)
        self.assertEqual([], self.r.waiters)

    def test_get_total_earnings(self):
        self.r.waiters = self.waiters
        result = self.r.get_total_earnings()
        self.assertEqual(150, result)


if __name__ == "__main__":
    main()
