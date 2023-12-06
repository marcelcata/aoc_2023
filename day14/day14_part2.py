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


def rotate_platform(platform):
    """Rotate platform 45º clockwise."""
    rotated_platform = [["" for _ in range(len(platform))] for _ in range(len(platform[0]))]
    for i, row in enumerate(platform):
        for j, value in enumerate(row):
            rotated_platform[j][len(platform) - i - 1] = value
    return rotated_platform


def main():
    with open("day14/input.txt") as f:
        lines = f.readlines()
    platform = []
    for line in lines:
        line = line.replace("\n", "")
        platform.append([char for char in line])

    # Somehow for a reason I don't fully understand, 1000 was highly probably a cycle, therefore
    # the result after 1_000_000_000 will be the same.
    num_iterations = 1000  # 1_000_000_000
    platforms = []
    i = 1
    while i <= num_iterations:
        platforms.append(platform)
        
        # Tilt towards north
        platform = tilt_platform(platform)

        # Rotate + tilt (towards west)
        platform = rotate_platform(platform)
        platform = tilt_platform(platform)

        # Rotate + tilt (towards south)
        platform = rotate_platform(platform)
        platform = tilt_platform(platform)

        # Rotate + tilt (towards east)
        platform = rotate_platform(platform)
        platform = tilt_platform(platform)

        # Rotate again back to initial orientation
        platform = rotate_platform(platform)

        for j, _platform in enumerate(platforms):
            if _platform == platform:
                iter_left = num_iterations - i
                i = num_iterations - iter_left % (i - j)
        i = i + 1

    result = 0
    for i, row in enumerate(platform):
        result += sum([elem == "O" for elem in row]) * (len(platform) - i)

    print(f"Part 2 result: {result}")


if __name__ == "__main__":
    main()
