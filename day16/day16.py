# (c) Copyright 2023 Marcel
import sys
import tqdm

sys.setrecursionlimit(100000)


DIRECTIONS = {
    "right": (1, 0),
    "left": (-1, 0),
    "up": (0, -1),
    "down": (0, 1),
}


class Cell:

    def __init__(self, x, y, symbol):
        """Initialize cell."""
        self.x = x
        self.y = y
        self.symbol = symbol
        self.beam_received = []
    
    def reset_beam_received(self):
        self.beam_received = []


def find_next_direction(current_cell, input_direction):
    """Return output direction given the input and cell symbol."""
    if current_cell.symbol == ".":
        return [input_direction]
    if current_cell.symbol == "|":
        if input_direction in ["up", "down"]:
            return [input_direction]
        elif input_direction in ["right", "left"]:
            return ["up", "down"]
        else:
            raise ValueError(f"What is this direction? {input_direction}")
    elif current_cell.symbol == "-":
        if input_direction in ["left", "right"]:
            return [input_direction]
        elif input_direction in ["up", "down"]:
            return ["left", "right"]
        else:
            raise ValueError(f"What is this direction? {input_direction}")
    elif current_cell.symbol == "/":
        if input_direction == "right":
            return ["up"]
        elif input_direction == "left":
            return ["down"]
        elif input_direction == "up":
            return ["right"]
        elif input_direction == "down":
            return ["left"]
        else:
            raise ValueError(f"What is this direction? {input_direction}")
    elif current_cell.symbol == "\\":
        if input_direction == "right":
            return ["down"]
        elif input_direction == "left":
            return ["up"]
        elif input_direction == "up":
            return ["left"]
        elif input_direction == "down":
            return ["right"]
        else:
            raise ValueError(f"What is this direction? {input_direction}")
    else:
        raise ValueError(f"What is this symbol? {current_cell.symbol}")


def find_next_cell(current_cell, input_direction, layout, num_rows, num_cols):
    if input_direction in current_cell.beam_received:
        return
    current_cell.beam_received.append(input_direction)
    next_directions = find_next_direction(current_cell, input_direction)
    for next_direction in next_directions:
        next_x = current_cell.x + DIRECTIONS[next_direction][0]
        next_y = current_cell.y + DIRECTIONS[next_direction][1]

        if next_x in [-1, num_cols] or next_y in [-1, num_rows]:
            continue
        else:
            next_cell = layout[(next_x, next_y)]
            find_next_cell(next_cell, next_direction, layout, num_rows, num_cols)


def main():
    with open("day16/input.txt") as f:
        lines = f.readlines()
    layout = [line.replace("\n", "") for line in lines]
    num_rows = len(layout)
    num_cols = len(layout[0])

    cells = {}
    for y, row in enumerate(layout):
        for x, symbol in enumerate(row):
            cells[(x, y)] = Cell(x, y, symbol)

    # Part 1
    num_energized_cells = 0
    initial_cell = cells[(0, 0)]
    find_next_cell(initial_cell, "right", cells, num_rows, num_cols)
    num_energized_cells = sum(1 for _, cell in cells.items() if len(cell.beam_received))

    print(f"Part 1 result: {num_energized_cells}")

    # Part 2
    max_num_energized_cells = 0

    # First and last columns
    for i in tqdm.tqdm(range(num_rows)):
        num_energized_cells = 0
        initial_cell = cells[(0, i)]
        find_next_cell(initial_cell, "right", cells, num_rows, num_cols)
        num_energized_cells = sum(1 for _, cell in cells.items() if len(cell.beam_received))
        if num_energized_cells > max_num_energized_cells:
            max_num_energized_cells = num_energized_cells
        for _, cell in cells.items():
            cell.reset_beam_received()

        num_energized_cells = 0
        initial_cell = cells[(num_cols - 1, i)]
        find_next_cell(initial_cell, "left", cells, num_rows, num_cols)
        num_energized_cells = sum(1 for _, cell in cells.items() if len(cell.beam_received))
        if num_energized_cells > max_num_energized_cells:
            max_num_energized_cells = num_energized_cells
        for _, cell in cells.items():
            cell.reset_beam_received()
    
    # First and last rows
    for i in tqdm.tqdm(range(num_cols)):
        num_energized_cells = 0
        initial_cell = cells[(i, 0)]
        find_next_cell(initial_cell, "down", cells, num_rows, num_cols)
        num_energized_cells = sum(1 for _, cell in cells.items() if len(cell.beam_received))
        if num_energized_cells > max_num_energized_cells:
            max_num_energized_cells = num_energized_cells
        for _, cell in cells.items():
            cell.reset_beam_received()
        
        num_energized_cells = 0
        initial_cell = cells[(i, num_rows - 1)]
        find_next_cell(initial_cell, "up", cells, num_rows, num_cols)
        num_energized_cells = sum(1 for _, cell in cells.items() if len(cell.beam_received))
        if num_energized_cells > max_num_energized_cells:
            max_num_energized_cells = num_energized_cells
        for _, cell in cells.items():
            cell.reset_beam_received()

    print(f"Part 2 result: {max_num_energized_cells}")


if __name__ == "__main__":
    main()
