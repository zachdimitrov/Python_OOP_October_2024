from unittest import TestCase, main


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(TestCase):
    def test_init(self):
        w = Worker("Test", 1000, 10)

        self.assertEqual(w.name, "Test")
        self.assertEqual(w.salary, 1000)
        self.assertEqual(w.energy, 10)
        self.assertEqual(w.money, 0)

    def test_worker_work_no_energy_raises(self):
        # Create worker with no energy
        # Arrange
        w = Worker("Test", 1000, 0)
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 0)

        # Act
        with self.assertRaises(Exception) as ex:
            result = w.work()
        self.assertEqual(str(ex.exception), "Not enough energy.")
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 0)

    def test_worker_works(self):
        w = Worker("Test", 1000, 100)
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 100)

        result = w.work()

        self.assertEqual(w.money, 1000)
        self.assertEqual(w.energy, 99)

        self.assertIsNone(result)

    def test_rest(self):
        w = Worker("Test", 1000, 100)
        self.assertEqual(w.energy, 100)
        result = w.rest()
        self.assertEqual(w.energy, 101)
        self.assertIsNone(result)

    def test_get_info(self):
        w = Worker("Test", 1000, 100)
        w.work()
        result = w.get_info()
        self.assertEqual(result, f'Test has saved 1000 money.')

    def test_worker_works_money_increases(self):
        w = Worker("Test", 1000, 100)
        self.assertEqual(w.money, 0)
        self.assertEqual(w.energy, 100)
        w.work()
        w.work()
        w.work()
        self.assertEqual(w.money, 3000)
        self.assertEqual(w.energy, 97)


if __name__ == "__main__":
    main()
