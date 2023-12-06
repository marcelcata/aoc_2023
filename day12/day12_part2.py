# (c) Copyright 2023 Marcel
import functools
import tqdm

def next_is_damaged(sequence, group_lengths):
    """# case."""
    group_length = group_lengths[0]
    group = sequence[:group_length]
    group = group.replace("?", "#")

    if group != "#" * group_length:
        # Can't fit all the damaged springs in the rest of the sequence
        return 0
    
    if len(sequence) == len(group):
        if len(group_lengths) == 1:
            # We fit the last group of damaged springs :)
            return 1
        # It fits but there's more groups to fit still
        return 0
    
    if sequence[group_length] in ".?":
        # Make sure that the next one can be an operational spring (.)
        # Continue the search after the whole group
        return find_num_arrangements(sequence[group_length + 1:], group_lengths[1:])
    
    return 0


def next_is_operational(sequence, group_lengths):
    """. case"""
    return find_num_arrangements(sequence[1:], group_lengths)


@functools.lru_cache(maxsize=None)
def find_num_arrangements(sequence, group_lengths):
    """Find the possibilities for the given sequence."""
    # If there's no more groups of damaged springs
    if len(group_lengths) == 0:
        if "#" in sequence:
            # It is not a possible arrangement if we still have damaged springs left
            return 0
        return 1

    # If there are groups left but no more sequence, it is not a possible arrangement
    if len(sequence) == 0:
        return 0
    
    num = 0
    next_char = sequence[0]
    if next_char == "#":
        num += next_is_damaged(sequence, group_lengths)
    elif next_char == '.':
        num += next_is_operational(sequence, group_lengths)
    elif next_char == "?":
        num += next_is_damaged(sequence, group_lengths) + next_is_operational(sequence, group_lengths)
    
    return num


def main():
    with open("day12/input.txt") as f:
        lines = f.readlines()
    springs = [line.replace("\n", "") for line in lines]

    num_arrangements = 0
    for spring in tqdm.tqdm(springs):
        sequence, group_lengths = spring.split()

        group_lengths = [int(num) for num in group_lengths.split(",")] * 5
        sequence = (sequence + "?") * 5
        sequence = sequence[:-1]  # Remove the trailing "?"

        num_arrangements += find_num_arrangements(sequence, tuple(group_lengths))

    print(f"Part 2 result: {num_arrangements}")


if __name__ == "__main__":
    main()
