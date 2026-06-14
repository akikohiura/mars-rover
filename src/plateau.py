from dataclasses import dataclass

@dataclass(frozen=True) # prevents fields from being reassigned
class Plateau:
    max_x: int
    max_y: int

    def __post_init__(self):
        if self.max_x < 0:
            raise ValueError("Plateau upper-right x-coordinate cannot be negative.")

        if self.max_y < 0:
            raise ValueError("Plateau upper-right y-coordinate cannot be negative.")

        if self.max_x == 0 and self.max_y == 0:
            raise ValueError("Plateau must have a non-zero size.")

    def is_in_plateau(self, x: int, y: int) -> bool:
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y