# Mars Rover Technical Challenge

This project is a Python solution for the Mars Rover technical challenge.

## Problem Summary

NASA has deployed a squad of robotic rovers on a rectangular plateau on Mars.

The plateau is represented as a grid. The lower-left coordinate is assumed to be `0 0`, and the upper-right coordinate is provided as input.

Each rover has:

* An `x` coordinate
* A `y` coordinate
* A direction it is facing: `N`, `E`, `S`, or `W`
* A set of movement instructions

Rovers are processed sequentially, meaning the next rover does not start moving until the previous rover has finished all of its instructions.

## Running the Application

Clone the repository:

```bash
git clone https://github.com/akikohiura/mars-rover.git
cd mars-rover
```

Run the application:

```bash
python src/main.py
```

The application will prompt for:

1. Plateau upper-right coordinates
2. Rover starting position
3. Rover instructions
4. Whether another rover should be processed

Example session:

```text
Enter plateau upper-right coordinates, e.g. 5 5:
5 5

Plateau created.

Enter rover 1 details.
1. Rover starting position, e.g. 1 2 N:
1 2 N

2. Rover instructions, e.g. LMLMLMLMM:
LMLMLMLMM

Rover 1 final position: 1 3 N

Do you wish to continue? Y or N:
Y

Enter rover 2 details.
1. Rover starting position, e.g. 3 3 E:
3 3 E

2. Rover instructions, e.g. MMRMMRMRRM:
MMRMMRMRRM

Rover 2 final position: 5 1 E

Do you wish to continue? Y or N:
N

Exiting...
```

## Input Format

The first line of input contains the upper-right coordinates of the plateau.

The lower-left coordinates are assumed to be:

```text
0 0
```

The remaining input contains information about each rover that has been deployed.

Each rover has two lines of input.

### 1. Rover Starting Position

```text
x y direction
```

Where:

* `x` is the rover's x-coordinate
* `y` is the rover's y-coordinate
* `direction` is one of `N`, `E`, `S`, or `W`

### 2. Rover Instructions

The rover's movement instructions are made up of one or more of the following commands:

| Command | Description                                          |
| ------- | ---------------------------------------------------- |
| `L`     | Spin left 90 degrees without moving                  |
| `R`     | Spin right 90 degrees without moving                 |
| `M`     | Move forward one grid point in the current direction |

## Example Input

```text
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```

## Expected Output

```text
1 3 N
5 1 E
```

## Assumptions

* The plateau lower-left coordinate is always `0 0`.
* The plateau boundaries are inclusive.
* The plateau upper-right coordinates cannot be negative.
* A plateau with upper-right coordinates of `0 0` is considered invalid.
* A rover's starting position must be within the plateau boundaries.
* Rover instructions are required and cannot be empty.
* If invalid input is provided, the application displays an error message and exits cleanly.
* If a rover instruction would move the rover outside the plateau boundaries, the move is rejected and an error is displayed.
* Rovers are processed one at a time.
* After each rover is processed, the user can choose whether to enter another rover.
* Only `Y` continues to the next rover; any other response exits the application.
* Rover collision detection is not implemented, as it is not specified in the requirements.

## Tests

The project includes:

* Unit tests for `Plateau`, `Position`, and `Rover`
* Integration tests covering the supplied Mars Rover example
* An end-to-end test that executes the console application using user input

Run all tests:

```bash
python -m unittest discover
```