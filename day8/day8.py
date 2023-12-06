# (c) Copyright 2023 Marcel

class Node:

    def __init__(self, name, left, right):
        """Initialize."""
        self.name = name
        self.left = left
        self.right = right


def main():
    with open("day8/input.txt") as f:
        lines = f.readlines()

    turn_sequence = lines[0].replace("\n", "")

    list_of_nodes = []
    for line in lines[2:]:
        name, destinations = line.replace("\n", "").split(" = ")
        left, right = destinations.split(", ")
        list_of_nodes.append(
            Node(
                name,
                left.replace("(", ""),
                right.replace(")", ""),
            )
        )

    current_node = "AAA"
    index = 0
    movements = 0
    while current_node != "ZZZ":
        for node in list_of_nodes:
            if node.name == current_node:
                current_node = node.left if turn_sequence[index] == "L" else node.right
                break
        index = (index + 1) % len(turn_sequence)
        movements += 1

    print(f"Part 1 result: {movements}")


if __name__ == "__main__":
    main()
