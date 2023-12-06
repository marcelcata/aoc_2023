# (c) Copyright 2023 Marcel


def _is_a_proper_reflection(pattern, i, smudge_index):
    """Check that the reflection follows along the whole pattern."""
    checked_rows = [i, i+1]
    for j in range(1, i + 1):
        if (i-j) >= 0 and (i + j + 1) < len(pattern):
            checked_rows.append(i-j)
            checked_rows.append(i+j+1)
            if pattern[i-j] != pattern[i + j + 1]:
                return False

    # Reflection is only good if the smudge is part of it
    if smudge_index in checked_rows:
        return True
    else:
        return False


def _find_horizontal_reflection(pattern, smudge_index):
    """Find horizontal reflection."""
    for i, _ in enumerate(pattern[:-1]):
            if pattern[i] == pattern[i + 1]:
                # When two contiguous rows are equal, check the full mirrorin effect
                if _is_a_proper_reflection(pattern, i, smudge_index):
                    return i + 1
    return 0


def switch_value(pattern, row, col):
    """Switches # and . in pattern in position (row, col)."""
    new_value = "#" if pattern[row][col] == "." else "."
    new_pattern = []
    for i, line in enumerate(pattern):
        if i == row:
            if col == 0:
                new_pattern.append(new_value + line[1:])
            elif col == len(line) - 1:
                new_pattern.append(line[:-1] + new_value)
            else:
                new_pattern.append(line[:col] + new_value + line[col + 1:])
        else:
            new_pattern.append(line)

    return new_pattern


def find_symmetry_with_smudge(pattern):
    """Find the symmetry with all the smudge combinations."""
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            
            # Switch value in the pattern (smudge it)
            pattern = switch_value(pattern, i, j)

            # Look for horizontal reflections
            result = _find_horizontal_reflection(pattern, i)

            if result > 0:
                return 100 * result

            # Transpose pattern and look for horizontal mirrors again
            pattern_transposed = [''.join(line) for line in zip(*pattern)]
            result = _find_horizontal_reflection(pattern_transposed, j)
            if result > 0:
                return result
            
            # Switch value back
            pattern = switch_value(pattern, i, j)

    # We should never get here
    raise ValueError("Input map has no smudged symmetries!")


def main():
    with open("day13/input.txt") as f:
        list_of_patterns = f.read().split("\n\n")

    list_of_patterns = [pattern.split("\n") for pattern in list_of_patterns]

    result = 0
    for pattern in list_of_patterns:
        result += find_symmetry_with_smudge(pattern) #, no_smudge_index)

    print(f"Part 2 result: {result}")


if __name__ == "__main__":
    main()
