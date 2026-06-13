import unittest

from direction import Direction
from position import Position

class TestPosition(unittest.TestCase):

    def test_position_initialises_with_x_y_and_direction(self):
        position = Position(1, 2, Direction.NORTH)
        self.assertEqual(1, position.x)
        self.assertEqual(2, position.y)
        self.assertEqual(Direction.NORTH, position.direction)

    def test_position_str_returns_x_y_and_direction_value(self):
        position = Position(1, 2, Direction.NORTH)
        self.assertEqual("1 2 N", str(position))

if __name__ == "__main__":
    unittest.main()