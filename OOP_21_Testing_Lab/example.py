from unittest import TestCase, main


def sum_nums(a, b):
    return a + b


class SumTest(TestCase):
    def test_sum_nums_returns_result(self):
        expected_result = 11
        # Act
        actual_result = sum_nums(5, 6)

        # Assert
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
