class Plateau:
    def __init__(self, max_x: int, max_y: int):
        if max_x < 0:
            raise ValueError("Plateau upper-right x-coordinate cannot be negative.")

        if max_y < 0:
            raise ValueError("Plateau upper-right y-coordinate cannot be negative.")

        if max_x == 0 and max_y == 0:
            raise ValueError("Plateau must have a non-zero size.")

        self.max_x = max_x
        self.max_y = max_y

    def is_in_plateau(self, x: int, y: int) -> bool:
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y
