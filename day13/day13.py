# (c) Copyright 2023 Marcel

def _is_a_proper_reflection(pattern, i):
    """Check that the reflection follows along the whole pattern."""
    for j in range(1, i):
        if (i-j) >= 0 and (i + j + 1) < len(pattern):
            if pattern[i-j] != pattern[i + j + 1]:
                return False
    return True


def _find_horizontal_reflection(pattern):
    """Find horizontal reflection."""
    for i, _ in enumerate(pattern[:-1]):
            if pattern[i] == pattern[i + 1]:
                if _is_a_proper_reflection(pattern, i):
                    return i + 1
    return 0


def main():
    with open("day13/input.txt") as f:
        list_of_patterns = f.read().split("\n\n")

    list_of_patterns = [pattern.split("\n") for pattern in list_of_patterns]

    result = 0
    for pattern in list_of_patterns:


        # Look for horizontal mirrors
        result += 100*_find_horizontal_reflection(pattern)

        # Transpose pattern and look for horizontal mirrors again
        pattern = [''.join(line) for line in zip(*pattern)]
        result += _find_horizontal_reflection(pattern)

    print(f"Part 1 result: {result}")


if __name__ == "__main__":
    main()
