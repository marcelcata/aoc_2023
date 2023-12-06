# (c) Copyright 2023 Marcel


def main():
    with open("day15/input.txt") as f:
        lines = f.readlines()
    list_of_steps = lines[0].split(",")

    # Part 1
    result = 0
    for string in list_of_steps:
        current_value = 0
        for char in string:
            current_value += ord(char)
            current_value *= 17
            current_value = current_value % 256
        result += current_value

    print(f"Part 1 result: {result}")

    # Part 2
    # Fill up boxes
    boxes = [{} for _ in range(256)]
    for string in list_of_steps:
        box_id = 0
        for char in string:
            if char.isalpha():
                box_id += ord(char)
                box_id *= 17
                box_id = box_id % 256
            else:
                break
        if "=" in string:
            letters, num = string.split("=")
            boxes[box_id][letters] = int(num)
        elif "-" in string:
            letters = string.replace("-", "")
            boxes[box_id].pop(letters, None)

    # Obtain the result
    result = 0
    for box_id, box in enumerate(boxes):
        for slot_id, (_, focal_length) in enumerate(box.items()):
            result += (box_id + 1) * (slot_id + 1) * focal_length

    print(f"Part 2 result: {result}")


if __name__ == "__main__":
    main()
