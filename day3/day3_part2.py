# (c) Copyright 2023 Marcel

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
DIGITS_AND_DOT = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


class Symbol:

    def __init__(self, row: int, col: int):
        """Initializer."""
        self.row = row
        self.col = col

    
class Number:
    
    def __init__(self, row: int, start_col: int, end_col: int, value: int):
        """Initializer."""
        self.row = row
        self.start_col = start_col
        self.end_col = end_col
        self.value = value
    
    def extend_number(self, col, value):
        if col != (self.end_col + 1):
            raise ValueError("Wrong number appended!")
        self.end_col = col
        self.value = self.value*10 + value


def is_neighbour(row, col, number, schematic):
    range_rows = [-1, 0, 1]
    if row == 0:
        range_rows = [0, 1]
    if row == (len(schematic) - 1):
        range_rows = [-1, 0]
    
    range_cols = [-1, 0, 1]
    if col == 0:
        range_cols = [0, 1]
    if col == (len(schematic[0]) - 1):
        range_cols = [-1, 0]
        
    range_rows = [row + _row for _row in range_rows]
    range_cols = [col + _col for _col in range_cols]
    
    if number.row not in range_rows:
        return False
    if (number.start_col not in range_cols) and (number.end_col not in range_cols):
        return False

    return True
    

def main():
    with open("day3/input.txt") as f:
        schematic = [line.replace("\n", "") for line in f.readlines()]

        # Store numbers and symbols positions
        number_in_progress = False
        numbers = []
        symbols = []
        for row, line in enumerate(schematic):
            for col, char in enumerate(line):
                if char in DIGITS:
                    if number_in_progress:
                        numbers[-1].extend_number(col, int(char))
                    else:
                        numbers.append(Number(row, col, col, int(char)))
                        number_in_progress = True
                elif char != ".":
                    symbols.append(Symbol(row, col))
                    number_in_progress = False
                else:
                    number_in_progress = False

        # Find the neighbours per symbol
        result = 0
        for symbol in symbols:
            neighbours = []
            for number in numbers:
                if is_neighbour(symbol.row, symbol.col, number, schematic):
                    neighbours.append(number)
            # If the symbol has exactly 2 neighbours, add product to result
            if len(neighbours) == 2:
                result += neighbours[0].value * neighbours[1].value

    print(f"Part 2 result: {result}")

    

if __name__ == "__main__":
    main()