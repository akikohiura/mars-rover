from dataclasses import dataclass
from direction import Direction

@dataclass # the rover position changes, so this should not be frozen
class Position:
    x: int
    y: int
    direction: Direction

    def __str__(self) -> str:
        return f"{self.x} {self.y} {self.direction.value}"