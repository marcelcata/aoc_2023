# (c) Copyright 2023 Marcel


def compute_distance(a, b, empties):
    """Compute distance taking into account the 1M separation of empty rows."""
    distance = 0
    for i in range(min(a, b), max(a, b)):
        if i in empties:
            distance += 1000000
        else:
            distance += 1
    return distance

    
def main():
    with open("day11/input.txt") as f:
        lines = f.readlines()
    space = [line.replace("\n", "") for line in lines]
    
    #Find empty rows
    empty_rows = []
    for i, row in enumerate(space):
        if "#" not in row:
            empty_rows.append(i)
        
    # Find empty cols
    empty_cols = list(range(len(space[0])))
    for row in space:
        for j, col in enumerate(row):
            if col == "#":
                if j in empty_cols:
                    empty_cols.pop(empty_cols.index(j))

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
            
            sum_of_distances += compute_distance(src_row, dest_row, empty_rows)
            sum_of_distances += compute_distance(src_col, dest_col, empty_cols)

    
    print(f"Part 2 result: {int(sum_of_distances/2)}")


if __name__ == "__main__":
    main()
