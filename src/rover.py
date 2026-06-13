from direction import Direction
from instruction import Instruction
from plateau import Plateau
from position import Position

class Rover:
    def __init__(self, position: Position, plateau: Plateau):
        if not plateau.is_in_plateau(position.x, position.y):
            raise ValueError("Rover starting position must be within plateau bounds.")

        self.position = position
        self.plateau = plateau

    def execute_instructions(self, instructions: str):
        for instruction in instructions.upper():
            match instruction:
                case Instruction.LEFT.value:
                    self.turn_left()
                case Instruction.RIGHT.value:
                    self.turn_right()
                case Instruction.MOVE.value:
                    self.move_forward()
                case _:
                    raise ValueError("Invalid instruction provided.")


    def turn_left(self):
        # print("Turning left...")
        # rover spin 90 degrees left without moving
        match self.position.direction:
            case Direction.NORTH:
                self.position.direction = Direction.WEST
            case Direction.EAST:
                self.position.direction = Direction.NORTH
            case Direction.SOUTH:
                self.position.direction = Direction.EAST
            case Direction.WEST:
                self.position.direction = Direction.SOUTH
            case _:
                raise ValueError("Invalid direction provided.")

    def turn_right(self):
        # print("Turning right...")
        # rover spin 90 degrees right without moving
        match self.position.direction:
            case Direction.NORTH:
                self.position.direction = Direction.EAST
            case Direction.EAST:
                self.position.direction = Direction.SOUTH
            case Direction.SOUTH:
                self.position.direction = Direction.WEST
            case Direction.WEST:
                self.position.direction = Direction.NORTH
            case _:
                raise ValueError("Invalid direction provided.")

    def move_forward(self):
        # print("Moving forward...")
        # move forward one grid point and maintain the same heading (i.e. direction)
        new_x = self.position.x
        new_y = self.position.y
        match self.position.direction:
            case Direction.NORTH:
                new_y += 1
            case Direction.EAST:
                new_x += 1
            case Direction.SOUTH:
                new_y -= 1
            case Direction.WEST:
                new_x -= 1

        if not self.plateau.is_in_plateau(new_x, new_y):
            raise ValueError(f"Rover cannot move one step to the {self.position.direction.value} because it will cause the rover to be outside the plateau.")

        self.position.x = new_x
        self.position.y = new_y