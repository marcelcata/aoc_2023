# (c) Copyright 2023 Marcel
import numpy


class Node:

    def __init__(self, name: str, left: str, right: str):
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

    current_nodes = [node.name for node in list_of_nodes if node.name.endswith("A")]
    movements = []
    for current_node in current_nodes:
        index = 0
        movements_current_node = 0
        while not current_node.endswith("Z"):
            for node in list_of_nodes:
                if node.name == current_node:
                    current_node = node.left if turn_sequence[index] == "L" else node.right
                    break
            index = (index + 1) % len(turn_sequence)
            movements_current_node += 1
        movements.append(movements_current_node)

    print(f"Part 2 result: {numpy.lcm.reduce(movements)}")


if __name__ == "__main__":
    main()
