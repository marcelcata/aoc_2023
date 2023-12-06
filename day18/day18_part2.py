# (c) Copyright 2023 Marcel


DIRECTIONS = {
    0: "R",
    1: "D",
    2: "L",
    3: "U",
}


def main():
    with open("day18/input.txt") as f:
        lines = f.readlines()

    directions = []
    steps = []
    for line in lines:
        line = line.replace("\n", "")
        _, hexadecimal = line.split("#")
        hexadecimal = hexadecimal.replace(")", "")
        steps.append(int("0x" + hexadecimal[:-1], 0))
        directions.append(DIRECTIONS[int(hexadecimal[-1])])

    # Accumulate vertices + count border cells
    row, col = 0, 0
    vertices = [(row, col)]
    num_border_cells = 0
    for direction, num_steps in zip(directions, steps):
        if direction == "R":
            col = col + num_steps
        elif direction == "L":
            col = col - num_steps
        elif direction == "U":
            row = row - num_steps
        elif direction == "D":
            row = row + num_steps
        else:
            raise ValueError("Wrong direction!")
        num_border_cells += num_steps
        vertices.append((row, col))

    # Shoelace formula to compute area
    area = 0
    for vertex1, vertex2 in zip(vertices[:-1], vertices[1:]):
        x1, y1 = vertex1
        x2, y2 = vertex2
        area += x1*y2 - x2*y1
    area = int(0.5 * abs(area))

    # Fix the number of inner cells
    inner_cells = area - (num_border_cells // 2) + 1

    print(f"Part 2 result: {inner_cells + num_border_cells}")


if __name__ == "__main__":
    main()
