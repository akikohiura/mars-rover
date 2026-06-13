import unittest

from plateau import Plateau

class TestPlateau(unittest.TestCase):

    def test_plateau_initialises_with_valid_coordinates(self):
        test_cases = [
            (5, 5),
            (0, 5),
            (5, 0),
        ]

        for max_x, max_y in test_cases:
            with self.subTest(max_x=max_x, max_y=max_y):
                plateau = Plateau(max_x, max_y)
                self.assertEqual(max_x, plateau.max_x)
                self.assertEqual(max_y, plateau.max_y)

    def test_plateau_raises_error_for_invalid_coordinates(self):
        test_cases = [
            (-1, 5, "Plateau upper-right x-coordinate cannot be negative."),
            (5, -1, "Plateau upper-right y-coordinate cannot be negative."),
            (0, 0, "Plateau must have a non-zero size."),
        ]

        for max_x, max_y, expected_error in test_cases:
            with self.subTest(max_x=max_x, max_y=max_y):
                with self.assertRaises(ValueError) as context:
                    Plateau(max_x, max_y)
                self.assertEqual(expected_error, str(context.exception))

    def test_is_in_plateau_returns_expected_result(self):
        plateau = Plateau(5, 5)

        test_cases = [
            (1, 2, True),
            (0, 0, True),
            (5, 5, True),
            (-1, 0, False),
            (0, -1, False),
            (6, 5, False),
            (5, 6, False),
        ]

        for x, y, expected_result in test_cases:
            with self.subTest(x=x, y=y):
                self.assertEqual(expected_result, plateau.is_in_plateau(x, y))

if __name__ == "__main__":
    unittest.main()