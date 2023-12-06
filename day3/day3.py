# (c) Copyright 2023 Marcel


DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
DIGITS_AND_DOT = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def replace_non_dot_neighbours(schematic, row, col):
    """Replace all the symbols by dots and recursively replace neighbouring numbers as well."""
    schematic[row] = schematic[row][:col] + "." + schematic[row][col+1:]
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
    
    for i in range_rows:
        for j in range_cols:
            if schematic[row + i][col + j] != ".":
                replace_non_dot_neighbours(schematic, row + i, col + j)

def main():
    with open("day3/input.txt") as f:
        schematic = [line.replace("\n", "") for line in f.readlines()]

        # Get sum of all numbers
        all_numbers_sum = 0
        number = "0"
        for row, line in enumerate(schematic):
            for col, char in enumerate(line):
                if char in DIGITS:
                    number += char
                else:
                    all_numbers_sum += int(number)
                    number = "0"

        # Remove numbers adjacent to symbols
        for row, line in enumerate(schematic):
            for col, char in enumerate(line):
                if char not in DIGITS_AND_DOT:
                    replace_non_dot_neighbours(schematic, row, col)

        # Get sum of remaining numbers
        lonely_numbers_sum = 0
        number = "0"
        for row, line in enumerate(schematic):
            for col, char in enumerate(line):
                if char in DIGITS:
                    number += char
                else:
                    lonely_numbers_sum += int(number)
                    number = "0"
        
        # Result = all numbers - lonely numbers
        result = all_numbers_sum - lonely_numbers_sum

    print(f"Part 1 result: {result}")

    

if __name__ == "__main__":
    main()
