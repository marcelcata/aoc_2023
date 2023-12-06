# (c) Copyright 2023 Marcel

# Part 1
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
result = 0

with open("day1/input.txt") as f:
    for line in f.readlines():
        numbers = []
        for char in line:
            if char in DIGITS:
                numbers.append(int(char))
        
        result += 10 * numbers[0] + numbers[-1]

print(f"Part 1 result: {result}")


# Part 2
NUMBERS_IN_LETTERS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

result = 0
with open("day1/input.txt") as f:
    for line in f.readlines():
        numbers = []
        for i, char in enumerate(line):
            # Case 1: we find a number
            if char in NUMBERS_IN_LETTERS.values():
                numbers.append(char)
            
            # Case 2: we find something else (a letter)
            else:
                for written_num in NUMBERS_IN_LETTERS.keys():
                    # Check if any number starts with the letter
                    if char == written_num[0]:
                        # Ensure the remaining characters are enough to spell the number
                        if (i + len(written_num)) < len(line):
                            match = True
                            # Check for the full number word
                            for j in range(len(written_num)):
                                if line[i + j] != written_num[j]:
                                    match = False
                            if match:
                                numbers.append(NUMBERS_IN_LETTERS[written_num])

        result += int(numbers[0] + numbers[-1])

print(f"Part 2 result: {result}")