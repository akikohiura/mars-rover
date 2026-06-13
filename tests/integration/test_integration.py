import unittest

from direction import Direction
from plateau import Plateau
from position import Position
from rover import Rover

class TestIntegration(unittest.TestCase):

    def test_sample_input_returns_expected_output(self):
        plateau = Plateau(5, 5)

        rover_one = Rover(Position(1, 2, Direction.NORTH), plateau)
        rover_one.execute_instructions("LMLMLMLMM")

        rover_two = Rover(Position(3, 3, Direction.EAST), plateau)
        rover_two.execute_instructions("MMRMMRMRRM")

        actual_output = [
            str(rover_one.position),
            str(rover_two.position),
        ]

        expected_output = [
            "1 3 N",
            "5 1 E",
        ]

        self.assertEqual(expected_output, actual_output)

    def test_rover_cannot_start_outside_plateau(self):
        plateau = Plateau(5, 5)
        with self.assertRaises(ValueError) as context:
            Rover(Position(5, 6, Direction.NORTH), plateau)
        self.assertEqual("Rover starting position must be within plateau bounds.", str(context.exception))

    def test_rover_cannot_move_outside_plateau(self):
        plateau = Plateau(5, 5)
        rover = Rover(Position(5, 5, Direction.NORTH), plateau)
        with self.assertRaises(ValueError) as context:
            rover.execute_instructions("M")
        self.assertEqual("Rover cannot move one step to the N because it will cause the rover to be outside the plateau.", str(context.exception))

if __name__ == "__main__":
    unittest.main()