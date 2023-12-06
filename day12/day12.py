# (c) Copyright 2023 Marcel
import copy
import tqdm


def sequence_is_possible(sequence, expected_pattern):
    """Returns true if there is a combination that is correct."""
    if sum(elem in ["#", "?"] for elem in sequence) < sum(expected_pattern):
        return False
    
    if sum(elem in ["#", "?"] for elem in sequence) == sum(expected_pattern):
        sequence = copy.copy(sequence)
        for i, elem in enumerate(sequence):
            if elem == "?":
                sequence[i] == "#"
    
    seq_pattern = []
    damaged_in_a_row = 0
    
    for element in sequence:
        if element == "#":
            damaged_in_a_row += 1
        elif element == "?":
            break
        else:
            if damaged_in_a_row > 0:
                seq_pattern.append(damaged_in_a_row)
                damaged_in_a_row = 0
    if damaged_in_a_row > 0:
        seq_pattern.append(damaged_in_a_row)
    
    if len(seq_pattern) == 0:
        return True
    
    if len(seq_pattern) > len(expected_pattern):
       return False

    for found, expected in zip(seq_pattern[:-1], expected_pattern[:len(seq_pattern) - 1]):
        if found != expected:
            return False
    
    if seq_pattern[-1] <= expected_pattern[len(seq_pattern) - 1]:
        return True
    return False

def find_num_arrangements(sequence, pattern):
    """Find the possibilities for the given sequence."""
    if "?" not in sequence:
        return 1

    num = 0
    new_sequence = copy.deepcopy(sequence)
    next_unknown_index = next(i for i, elem in enumerate(sequence) if elem == "?")
    new_sequence[next_unknown_index] = "#"
    if sequence_is_possible(new_sequence, pattern):
        num += find_num_arrangements(new_sequence, pattern)
    new_sequence[next_unknown_index] = "."
    if sequence_is_possible(new_sequence, pattern):
        num += find_num_arrangements(new_sequence, pattern)
    return num


def main():
    with open("day12/input.txt") as f:
        lines = f.readlines()
    springs = [line.replace("\n", "") for line in lines]

    result = 0
    for spring in tqdm.tqdm(springs):
        sequence, pattern = spring.split()
        pattern = [int(num) for num in pattern.split(",")]
        sequence = [element for element in sequence]

        value = find_num_arrangements(sequence, pattern)
        result = result + value            

    print(f"Part 1 result: {result}")


if __name__ == "__main__":
    main()
