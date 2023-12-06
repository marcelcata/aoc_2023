# (c) Copyright 2023 Marcel


def define_first_step(origin, lines):
    row, col = origin
    if lines[row - 1][col] in ["|", "F", "7"]:
        return(row - 1, col)
    if lines[row + 1][col] in ["|", "J", "L"]:
        return(row + 1, col)
    if lines[row][col + 1] in ["-", "J", "7"]:
        return(row, col + 1)
    if lines[row][col - 1] in ["-", "F", "L"]:
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


def main():
    with open("day10/test.txt") as f:
        lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]
    
    # Find starting point
    start_row, start_col = -1, -1
    for row, line in enumerate(lines):
        for col, symbol in enumerate(line):
            if symbol == "S":
                start_row = row
                start_col = col
    
    # Replace S by X
    lines[start_row] = lines[start_row][:start_col] + "X" + lines[start_row][start_col+1:]

    # Find first direction
    current_row, current_col = define_first_step((start_row, start_col), lines)
    distance_to_start = 1

    # Travel the map
    while (current_row, current_col) != (start_row, start_col):
        new_row, new_col = find_next_position(current_row, current_col, lines)
        lines[current_row] = lines[current_row][:current_col] + "X" + lines[current_row][current_col+1:]
        current_col = new_col
        current_row = new_row
        distance_to_start += 1

        # Reprinting the start point (not very nice to be done every time) because keeping an X gives problems (at last step)
        lines[start_row] = lines[start_row][:start_col] + "S" + lines[start_row][start_col+1:]
    
    print(f"Part 1 result: {int(distance_to_start/2)}")


if __name__ == "__main__":
    main()
