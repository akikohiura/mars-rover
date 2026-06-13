# Mars Rover Technical Challenge

This project is a Python solution for the Mars Rover technical challenge.

## Problem Summary

NASA has deployed a squad of robotic rovers on a rectangular plateau on Mars.

Each rover has:

* An `x` and `y` coordinate
* A direction it is facing: `N`, `E`, `S`, or `W`
* A list of movement instructions

The plateau starts at `0 0`, and the first input line defines the upper-right boundary.

Rovers are moved sequentially. This means the second rover only starts moving after the first rover has completed all of its instructions.

## Instructions

Each rover can receive the following commands:

| Command | Description                 |
| ------- | --------------------------- |
| `L`     | Turn left 90 degrees        |
| `R`     | Turn right 90 degrees       |
| `M`     | Move forward one grid point |

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
