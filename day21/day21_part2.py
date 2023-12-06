# (c) Copyright 2023 Marcel
import copy


def get_neighbours(point, garden):
    row, col = point
    neighbours = []
    if row != 0:
        neighbours.append((row - 1, col))
    if row != (len(garden) - 1):
        neighbours.append((row + 1, col))

    if col != 0:
        neighbours.append((row , col - 1))
    if col != (len(garden[0]) - 1):
        neighbours.append((row , col + 1))

    return [neighbour for neighbour in neighbours if garden[neighbour[0]][neighbour[1]] != "#"]


def main():
    with open("day21/input.txt") as f:
        garden = f.readlines()
    
    num_steps = 26501365
    start = "S"
    start_point = None
    for i, row in enumerate(garden):
        for j, _ in enumerate(row):
            if garden[i][j] == start:
                start_point = (i, j)
    positions = [start_point]

    for i in range(num_steps):
        print(i)
        new_positions = []
        for point in positions:
            neighbours = get_neighbours(point, garden)
            for neighbour in neighbours:
                if neighbour not in new_positions:
                    new_positions.append(neighbour)
        positions = copy.deepcopy(new_positions)
    
    print(f"Part 1 result: {len(positions)}")
            




if __name__ == "__main__":
    main()
