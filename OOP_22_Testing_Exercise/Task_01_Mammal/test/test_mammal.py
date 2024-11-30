from project.mammal import Mammal
from unittest import TestCase, main


class MammalTests(TestCase):
    def setUp(self):
        self.m = Mammal("Test", "Dog", "Bau")

    def test_init(self):
        self.assertEqual(self.m.name, "Test")
        self.assertEqual(self.m.type, "Dog")
        self.assertEqual(self.m.sound, "Bau")
        self.assertEqual(self.m._Mammal__kingdom, "animals")

    def test_make_sound(self):
        result = self.m.make_sound()
        self.assertEqual(result, "Test makes Bau")

    def test_get_kingdom(self):
        result = self.m.get_kingdom()
        self.assertEqual(result, "animals")

    def test_info(self):
        result = self.m.info()
        self.assertEqual(result, "Test is of type Dog")


if __name__ == "__main__":
    main()
