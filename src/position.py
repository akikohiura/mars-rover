from direction import Direction

class Position:
    def __init__(self, x: int, y: int, direction: Direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.direction.value}"