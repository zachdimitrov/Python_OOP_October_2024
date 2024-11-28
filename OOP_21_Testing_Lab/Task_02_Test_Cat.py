from unittest import TestCase, main


class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False


class CatTests(TestCase):
    def test_cat_init(self):
        c = Cat("Test")
        self.assertEqual(c.name, "Test")
        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        self.assertEqual(c.size, 0)

    def test_cat_eats(self):
        c = Cat("Test")
        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        self.assertEqual(c.size, 0)

        result = c.eat()
        self.assertIsNone(result)

        self.assertTrue(c.fed)
        self.assertTrue(c.sleepy)
        self.assertEqual(c.size, 1)

    def test_cat_fed_raises(self):
        c = Cat("Test")
        c.eat()
        self.assertEqual(c.size, 1)
        self.assertTrue(c.fed)
        self.assertTrue(c.sleepy)

        with self.assertRaises(Exception) as ex:
            c.eat()
        self.assertEqual(str(ex.exception), "Already fed.")
        self.assertEqual(c.size, 1)
        self.assertTrue(c.fed)
        self.assertTrue(c.sleepy)

    def test_sleep_cat_not_fed_raises(self):
        c = Cat("Test")
        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        with self.assertRaises(Exception) as ex:
            c.sleep()
        self.assertEqual(str(ex.exception), "Cannot sleep while hungry")
        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)

    def test_sleep(self):
        c = Cat("Test")
        c.eat()
        self.assertTrue(c.sleepy)
        result = c.sleep()
        self.assertFalse(c.sleepy)
        self.assertIsNone(result)

if __name__ == "__main__":
    main()