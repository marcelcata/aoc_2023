# (c) Copyright 2023 Marcel
import sys


sys.setrecursionlimit(100000)


def flood_neighbours(row, col, lines):
    """From a cell, paint all the neighbours as o until borders."""
    neighbours = []

    for _row, _col in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
        if lines[row + _row][col + _col] == ".":
            lines[row + _row][col + _col] = "o"
            neighbours.append((row + _row, col + _col))

    for _row, _col in neighbours:
        flood_neighbours(_row, _col, lines)


def main():
    with open("day18/input.txt") as f:
        lines = f.readlines()

    # Compute size of map
    rows = [0]
    cols = [0]
    for line in lines:
        line = line.replace("\n", "")
        direction, steps, _ = line.split()
        steps = int(steps)
        if direction == "R":
            cols.append(cols[-1] + steps)
        elif direction == "L":
            cols.append(cols[-1] - steps)
        elif direction == "U":
            rows.append(rows[-1] - steps)
        elif direction == "D":
            rows.append(rows[-1] + steps)
        else:
            raise ValueError("Wrong direction!")

    # Create map
    map = []
    for _ in range(max(rows) + 1 - min(rows)):
        map.append(["." for _ in range(max(cols) + 1 - min(cols))])

    # Draw the outline
    row, col = - min(rows), - min(cols)
    map[row][col] = "#"
    for line in lines:
        line = line.replace("\n", "")
        direction, steps, _ = line.split()
        for _ in range(int(steps)):
            if direction == "R":
                col = col + 1
            elif direction == "L":
                col = col - 1
            elif direction == "U":
                row = row - 1
            elif direction == "D":
                row = row + 1
            else:
                raise ValueError("Wrong direction!")
            map[row][col] = "#"

    count = 0
    for line in map:
        count += sum([1 for symbol in line if symbol != "."])
    print(count)

    # Flooding algorithm: flooding the inside
    map[- min(rows) + 1][- min(cols) + 1] = "o"
    flood_neighbours(
        row=- min(rows) + 1,
        col=- min(cols) + 1,
        lines=map,
    )

    # Count the # and inner cells
    count = 0
    for line in map:
        count += sum([1 for symbol in line if symbol != "."])
    
    print(f"Part 1 result: {count}")


if __name__ == "__main__":
    main()
