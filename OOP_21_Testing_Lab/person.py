from unittest import TestCase, main


class Person:
    def __init__(self, first_name, last_name, age):
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_info(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old."


class TestPerson(TestCase):
    def setUp(self):
        self.person = Person("Test", "Testov", 12)

    def test_init(self):
        # Assert
        self.assertEqual("Test", self.person.first_name)
        self.assertEqual("Testov", self.person.last_name)
        self.assertEqual(self.person.age, 12)

    def test_get_full_name(self):
        # Act
        result = self.person.get_full_name()
        expected_result = "Test Testov"

        # Assert
        self.assertEqual(expected_result, result)

    def test_get_info(self):
        # Act
        result = self.person.get_info()
        expected_result = "Test Testov is 12 years old."

        # Assert
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
