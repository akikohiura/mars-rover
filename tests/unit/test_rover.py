import unittest
from unittest.mock import patch

from direction import Direction
from plateau import Plateau
from position import Position
from rover import Rover

class TestRover(unittest.TestCase):

    def test_rover_initialises_with_valid_position(self):
        plateau = Plateau(5, 5)
        position = Position(1, 2, Direction.NORTH)
        rover = Rover(position, plateau)
        self.assertEqual(position, rover.position)
        self.assertEqual(plateau, rover.plateau)

    def test_rover_raises_error_when_starting_position_is_outside_plateau(self):
        plateau = Plateau(5, 5)
        position = Position(5, 6, Direction.NORTH)
        with self.assertRaises(ValueError) as context:
            Rover(position, plateau)
        self.assertEqual("Rover starting position must be within plateau bounds.", str(context.exception))

    def test_rover_execute_instructions_calls_correct_methods(self):
        rover = Rover(Position(1, 2, Direction.NORTH), Plateau(5, 5))

        with patch.object(rover, "turn_left") as mock_turn_left, patch.object(rover, "turn_right") as mock_turn_right, patch.object(rover, "move_forward") as mock_move_forward:
            rover.execute_instructions("LMRRLL")

            self.assertEqual(3, mock_turn_left.call_count)
            self.assertEqual(2, mock_turn_right.call_count)
            self.assertEqual(1, mock_move_forward.call_count)

    def test_rover_execute_instructions_raises_error_for_invalid_instruction(self):
        rover = Rover(Position(1, 2, Direction.NORTH), Plateau(5, 5))

        with patch.object(rover, "turn_left") as mock_turn_left, patch.object(rover, "turn_right") as mock_turn_right, patch.object(rover, "move_forward") as mock_move_forward:
            with self.assertRaises(ValueError) as context:
                rover.execute_instructions("LMXR")

            self.assertEqual("Invalid instruction provided.", str(context.exception))
            self.assertEqual(1, mock_turn_left.call_count)
            self.assertEqual(0, mock_turn_right.call_count)
            self.assertEqual(1, mock_move_forward.call_count)

    def test_rover_turn_left_updates_direction_correctly(self):
        test_cases = [
            (Direction.NORTH, Direction.WEST),
            (Direction.WEST, Direction.SOUTH),
            (Direction.SOUTH, Direction.EAST),
            (Direction.EAST, Direction.NORTH),
        ]

        for starting_direction, expected_direction in test_cases:
            with self.subTest(starting_direction=starting_direction):
                rover = Rover(Position(1, 2, starting_direction), Plateau(5, 5))
                rover.turn_left()
                self.assertEqual(expected_direction, rover.position.direction)

    def test_rover_turn_left_raises_error_for_invalid_direction(self):
        rover = Rover(Position(1, 2, "X"), Plateau(5, 5))
        with self.assertRaises(ValueError) as context:
            rover.turn_left()
        self.assertEqual("Invalid direction provided.", str(context.exception))

    def test_rover_turn_right_updates_direction_correctly(self):
        test_cases = [
            (Direction.NORTH, Direction.EAST),
            (Direction.EAST, Direction.SOUTH),
            (Direction.SOUTH, Direction.WEST),
            (Direction.WEST, Direction.NORTH),
        ]

        for starting_direction, expected_direction in test_cases:
            with self.subTest(starting_direction=starting_direction):
                rover = Rover(Position(1, 2, starting_direction), Plateau(5, 5))
                rover.turn_right()
                self.assertEqual(expected_direction, rover.position.direction)

    def test_rover_turn_right_raises_error_for_invalid_direction(self):
        rover = Rover(Position(1, 2, "X"), Plateau(5, 5))
        with self.assertRaises(ValueError) as context:
            rover.turn_right()
        self.assertEqual("Invalid direction provided.", str(context.exception))

    def test_rover_move_forward_updates_position_correctly(self):
        test_cases = [
            (Direction.NORTH, "1 3 N"),
            (Direction.EAST, "2 2 E"),
            (Direction.SOUTH, "1 1 S"),
            (Direction.WEST, "0 2 W"),
        ]

        for direction, expected_position in test_cases:
            with self.subTest(direction=direction):
                rover = Rover(Position(1, 2, direction), Plateau(5, 5))
                rover.move_forward()
                self.assertEqual(expected_position, str(rover.position))

    def test_rover_move_forward_raises_error_for_invalid_direction(self):
        rover = Rover(Position(1, 2, "X"), Plateau(5, 5))
        with self.assertRaises(ValueError) as context:
            rover.move_forward()
        self.assertEqual("Invalid direction provided.", str(context.exception))

    def test_rover_move_forward_raises_error_when_moving_outside_plateau(self):
        test_cases = [
            (Position(5, 5, Direction.NORTH), "N"),
            (Position(5, 5, Direction.EAST), "E"),
            (Position(0, 0, Direction.SOUTH), "S"),
            (Position(0, 0, Direction.WEST), "W"),
        ]

        for position, direction_value in test_cases:
            with self.subTest(position=str(position)):
                rover = Rover(position, Plateau(5, 5))
                with self.assertRaises(ValueError) as context:
                    rover.move_forward()
                self.assertEqual(f"Rover cannot move one step to the {direction_value} because it will cause the rover to be outside the plateau.", str(context.exception))

if __name__ == "__main__":
    unittest.main()