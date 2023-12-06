# (c) Copyright 2023 Marcel


def main():
    with open("day11/input.txt") as f:
        lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]
    
    # Duplicate rows that are empty (all .)
    space = []
    for row in lines:
        space.append(row)
        if "#" not in row:
            space.append(row)

    # Duplicate cols that are empty (all .)
    empty_cols = list(range(len(space[0])))
    for row in space:
        for j, col in enumerate(row):
            if col == "#":
                if j in empty_cols:
                    empty_cols.pop(empty_cols.index(j))

    space_aux = []
    for row in space:
        new_row = []
        for j, symbol in enumerate(row):
            new_row.append(symbol)
            if j in empty_cols:
                new_row.append(symbol)
        space_aux.append("".join(new_row))

    space = space_aux

    # Look for all the galaxies (#)
    galaxies_coordinates = []
    for i, row in enumerate(space):
        for j, symbol in enumerate(row):
            if symbol == "#":
                galaxies_coordinates.append((i, j))
    
    # Compute all distances
    sum_of_distances = 0
    for src_row, src_col in galaxies_coordinates:
        for dest_row, dest_col in galaxies_coordinates:
            sum_of_distances += abs(src_row-dest_row) + abs(src_col-dest_col)
    
    print(f"Part 1 result: {int(sum_of_distances/2)}")


if __name__ == "__main__":
    main()
