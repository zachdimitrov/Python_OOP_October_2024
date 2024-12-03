from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTests(TestCase):
    def setUp(self):
        self.v = Vehicle(5.5, 50.5)

    def test_init(self):
        self.assertEqual(self.v.fuel, 5.5)
        self.assertEqual(self.v.horse_power, 50.5)
        self.assertEqual(self.v.capacity, 5.5)
        self.assertEqual(self.v.fuel_consumption, 1.25)

    def test_drive_no_fuel_raises(self):
        km = 100
        self.v.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.v.drive(km)
        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_drive(self):
        km = 100
        self.v.fuel = self.v.fuel_consumption * km + 1
        result = self.v.drive(100)
        self.assertEqual(self.v.fuel, 1)
        self.assertEqual(result, None)

    def test_refuel_too_much_raises(self):
        with self.assertRaises(Exception) as ex:
            self.v.refuel(100)
        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_refuel(self):
        self.v.fuel = 1
        self.v.refuel(3)
        self.assertEqual(self.v.fuel, 4)

    def test_str(self):
        result = str(self.v)
        expected = f"The vehicle has 50.5 " \
            f"horse power with 5.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    main()
