from direction import Direction
from plateau import Plateau
from position import Position
from rover import Rover


def main():
    try:
        plateau_input = input("Enter plateau upper-right coordinates, e.g. 5 5:\n")
        plateau_x, plateau_y = map(int, plateau_input.split())
        plateau = Plateau(plateau_x, plateau_y)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print("Plateau created.")
    rover_number = 1

    while True:
        print(f"Enter rover {rover_number} details.")
        try:
            position_input = input("1. Rover starting position, e.g. 1 2 N:\n")
            position_input_parts = position_input.split()

            if len(position_input_parts) != 3:
                print("Rover starting position must include x, y, and direction.")
                return

            x, y, direction = position_input_parts

            position = Position(int(x), int(y), Direction(direction))
            rover = Rover(position, plateau)
        except ValueError as error:
            print(f"Error: {error}")
            return

        try:
            instructions = input("2. Rover instructions, e.g. LMLMLMLMM:\n")
            if not instructions:
                print("Rover instructions are required.")
                return

            rover.execute_instructions(instructions)

            print(f"Rover {rover_number} final position: {rover.position}")
        except ValueError as error:
            print(f"Error: {error}")
            return

        continue_input = input("Do you wish to continue? Y or N:\n").upper()

        if continue_input == "Y":
            rover_number += 1
            continue

        print("Exiting...")
        return

if __name__ == "__main__":
    main()