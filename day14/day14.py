# (c) Copyright 2023 Marcel


def tilt_platform(platform):
    """Tilt platform towards north."""
    for i, row in enumerate(platform[1:]):
        row_index = i + 1
        for col_index, elem in enumerate(row):
            if elem == "O":
                rolled = False
                platform[row_index][col_index] = "."
                for row_above_index in range(row_index - 1, -1, -1):
                    if platform[row_above_index][col_index] in ["#", "O"]:
                        platform[row_above_index + 1][col_index] = "O"
                        rolled = True
                        break
                if rolled == False:
                    platform[0][col_index] = "O"
    return platform


def main():
    with open("day14/test.txt") as f:
        lines = f.readlines()
    platform = []
    for line in lines:
        line = line.replace("\n", "")
        platform.append([char for char in line])

    platform = tilt_platform(platform)

    result = 0
    for i, row in enumerate(platform):
        result += sum([elem == "O" for elem in row]) * (len(platform) - i)

    print(f"Part 1 result: {result}")


if __name__ == "__main__":
    main()
