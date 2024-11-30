from car_manager import Car
from unittest import TestCase, main


class CarTests(TestCase):
    def test_init(self):
        car = Car("Test", "TestModel", 2, 30)
        self.assertEqual(car.make, "Test")
        self.assertEqual(car.model, "TestModel")
        self.assertEqual(car.fuel_consumption, 2)
        self.assertEqual(car.fuel_capacity, 30)
        self.assertEqual(car.fuel_amount, 0)

    def test_make_empty_string_raises(self):
        with self.assertRaises(Exception) as ex:
            c = Car("", "TestModel", 2, 30)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_make_none_raises(self):
        with self.assertRaises(Exception) as ex:
            c = Car(None, "TestModel", 2, 30)
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_model_empty_string_raises(self):
        with self.assertRaises(Exception) as ex:
            c = Car("Test", "", 2, 30)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_model_none_raises(self):
        with self.assertRaises(Exception) as ex:
            c = Car("Test", None, 2, 30)
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            c = Car("Test", "TestModel", 0, 30)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_less_than_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            c = Car("Test", "TestModel", -1, 30)
        self.assertEqual(str(ex.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            c = Car("Test", "TestModel", 2, 0)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_capacity_less_than_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            c = Car("Test", "TestModel", 2, -1)
        self.assertEqual(str(ex.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_ammount_negative_raises(self):
        c = Car("Test", "TestModel", 2, 30)
        self.assertEqual(c.fuel_amount, 0)
        with self.assertRaises(Exception) as ex:
            c.fuel_amount = -1
        self.assertEqual(str(ex.exception), "Fuel amount cannot be negative!")

    def test_refuel_zero_raises(self):
        c = Car("Test", "TestModel", 2, 30)
        self.assertEqual(c.fuel_amount, 0)
        with self.assertRaises(Exception) as ex:
            c.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_zero_raises(self):
        c = Car("Test", "TestModel", 2, 30)
        self.assertEqual(c.fuel_amount, 0)
        with self.assertRaises(Exception) as ex:
            c.refuel(-1)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel(self):
        c = Car("Test", "TestModel", 2, 30)
        self.assertEqual(c.fuel_amount, 0)
        c.refuel(10)
        self.assertEqual(c.fuel_amount, 10)

    def test_refuel_more(self):
        c = Car("Test", "TestModel", 2, 30)
        self.assertEqual(c.fuel_amount, 0)
        c.refuel(30)
        self.assertEqual(c.fuel_amount, 30)
        c.refuel(10)
        self.assertEqual(c.fuel_amount, 30)

    def test_drive_no_fuel_raises(self):
        c = Car("Test", "TestModel", 2, 30)
        c.refuel(30)
        self.assertEqual(c.fuel_amount, 30)
        with self.assertRaises(Exception) as ex:
            c.drive(3000)
        self.assertEqual(c.fuel_amount, 30)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive(self):
        c = Car("Test", "TestModel", 2, 30)
        c.refuel(30)
        self.assertEqual(c.fuel_amount, 30)
        c.drive(1000)
        self.assertEqual(c.fuel_amount, 10)


if __name__ == "__main__":
    main()
