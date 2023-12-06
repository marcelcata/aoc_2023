# (c) Copyright 2023 Marcel


def all_zeros(sequence):
    for element in sequence:
        if element != 0:
            return False
    return True


def find_next_value(sequence):
    new_sequence = []
    for i in range(len(sequence) - 1):
        new_sequence.append(sequence[i+1] - sequence[i])
    
    if all_zeros(new_sequence):
        return sequence[-1]
    else:
        return find_next_value(new_sequence) + sequence[-1]


def find_previous_value(sequence):
    new_sequence = []
    for i in range(len(sequence) - 1):
        new_sequence.append(sequence[i+1] - sequence[i])
    
    if all_zeros(new_sequence):
        return sequence[0]
    else:
        return sequence[0] - find_previous_value(new_sequence)


def main():
    with open("day9/input.txt") as f:
        lines = f.readlines()

    result_1 = 0
    for line in lines:
        sequence = line.replace("\n", "").split()
        sequence = [int(element) for element in sequence]
        result_1 += find_next_value(sequence)

    print(f"Part 1 result: {result_1}")

    result_2 = 0
    for line in lines:
        sequence = line.replace("\n", "").split()
        sequence = [int(element) for element in sequence]
        result_2 += find_previous_value(sequence)

    print(f"Part 2 result: {result_2}")


if __name__ == "__main__":
    main()
