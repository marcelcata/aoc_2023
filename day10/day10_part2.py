# (c) Copyright 2023 Marcel
import sys

sys.setrecursionlimit(100000)

def define_first_step(origin, lines):
    row, col = origin
    if lines[row - 2][col] in ["|", "F", "7"]:
        return(row - 1, col)
    if lines[row + 2][col] in ["|", "J", "L"]:
        return(row + 1, col)
    if lines[row][col + 2] in ["-", "J", "7"]:
        return(row, col + 1)
    if lines[row][col - 2] in ["-", "F", "L"]:
        return(row, col - 1)
    raise ValueError("Start not connected!")


def find_next_position(row, col, lines):
    origin = lines[row][col]
    if origin == "|":
        if lines[row - 1][col] == "X":
            return (row + 1, col)
        else:
            return (row - 1, col)
    elif origin == "-":
        if lines[row][col - 1] == "X":
            return (row, col + 1)
        else:
            return (row, col - 1)
    elif origin == "L":
        if lines[row - 1][col] == "X":
            return (row, col + 1)
        else:
            return (row - 1, col)
    elif origin == "F":
        if lines[row][col + 1] == "X":
            return (row + 1, col)
        else:
            return (row, col + 1)
    elif origin == "J":
        if lines[row - 1][col] == "X":
            return (row, col - 1)
        else:
            return (row - 1, col)
    elif origin == "7":
        if lines[row][col - 1] == "X":
            return (row + 1, col)
        else:
            return (row, col - 1)
    else:
        raise ValueError(f"Something is wrong! Read this symbol {origin}")
    

def update_neighbours(row, col, lines):
    lines[row] = lines[row][:col] + "o" + lines[row][col+1:]
    
    neighbours = []
    if row != 0:
        neighbours.append((row - 1, col))
    if row != (len(lines) - 1):
        neighbours.append((row + 1, col))
    if col != 0:
        neighbours.append((row , col - 1))
    if col != (len(lines[0]) - 1):
        neighbours.append((row , col + 1))

    for _row, _col in neighbours:
        if lines[_row][_col] in ["X", "o"]:
            continue
        update_neighbours(_row, _col, lines)


def main():
    with open("day10/input.txt") as f:
        lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]
    
    # Trick: add extra columns and files to be able to flood hidden not-enclosed areas
    maze_aux = []
    for line in lines:
        maze_aux.append(line)
        maze_aux.append("".join(["|" for _ in range(len(line))]))
    
    maze = []
    for line in maze_aux:
        maze.append("".join([f"{symbol}-" for symbol in line]))

    # Find starting point
    start_row, start_col = -1, -1
    for row, line in enumerate(maze):
        for col, symbol in enumerate(line):
            if symbol == "S":
                start_row = row
                start_col = col
    
    # Replace S by X
    maze[start_row] = maze[start_row][:start_col] + "X" + maze[start_row][start_col+1:]

    # Find first direction
    current_row, current_col = define_first_step((start_row, start_col), maze)
    distance_to_start = 1

    # Travel the map
    while (current_row, current_col) != (start_row, start_col):
        new_row, new_col = find_next_position(current_row, current_col, maze)
        maze[current_row] = maze[current_row][:current_col] + "X" + maze[current_row][current_col+1:]
        current_col = new_col
        current_row = new_row
        distance_to_start += 1

        # Reprinting the start point (not very nice to be done every time) because keeping an X gives problems (at last step)
        maze[start_row] = maze[start_row][:start_col] + "S" + maze[start_row][start_col+1:]

    # Reprinting an X to have the whole path as X's
    maze[start_row] = maze[start_row][:start_col] + "X" + maze[start_row][start_col+1:]

    # Flooding algorithm: flooding the map from all side cells
    for row in [0, len(maze) - 1]:
        for col in range(len(maze[0])):
            if maze[row][col] not in ["X", "o"]:
                update_neighbours(row, col, maze)

    for row in range(len(maze)):
        for col in [0, len(maze[0]) - 1]:
            if maze[row][col] not in ["X", "o"]:
                update_neighbours(row, col, maze)

    # Trick: Remove all the added rows and columns
    maze = [line[::2] for line in maze[::2]]

    # Count all cells that are not part of the path (X) nor outside (o)
    enclosed_cells = 0
    for line in maze:
        for symbol in line:
            if symbol not in ["X", "o"]:
                enclosed_cells += 1
    
    print(f"Part 2 result: {enclosed_cells}")


if __name__ == "__main__":
    main()
