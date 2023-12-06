# (c) Copyright 2023 Marcel
from queue import PriorityQueue


def opposite_direction(direction):
    if direction == "horizontal":
        return "vertical"
    return "horizontal"


def main():
    with open("day17/input.txt") as f:
        lines = f.readlines()
    city_map = [line.replace("\n", "") for line in lines]
    num_rows = len(city_map)
    num_cols = len(city_map[0])

    nodes_to_search = PriorityQueue()

    # Start options, node 0,0 in both directions
    nodes_to_search.put((0, (0, 0, "horizontal")))
    nodes_to_search.put((0, (0, 0, "vertical")))

    visited_nodes = []
    goal_col, goal_row = (num_cols - 1, num_rows - 1)

    while not nodes_to_search.empty():
        original_distance, (col, row, direction) = nodes_to_search.get()

        # If we get to visit the goal block, we're done
        if col == goal_col and row == goal_row:
            print(f"Part 1 result: {original_distance}")
            break

        # We don't revisit any state
        if (col, row, direction) in visited_nodes:
            continue

        # Add the visited state
        visited_nodes.append((col, row, direction))

        for step_direction in [-1, 1]:
            distance = original_distance
            for step_size in [1, 2, 3]:
                if direction == "horizontal":
                    new_col = col + step_direction * step_size
                    new_row = row
                else:
                    new_col = col
                    new_row = row + step_direction * step_size

                if new_col < 0 or new_row < 0 or new_col >= num_cols or new_row >= num_rows:
                    break

                distance += int(city_map[new_row][new_col])

                if (new_col, new_row, opposite_direction(direction)) in visited_nodes:
                    continue

                nodes_to_search.put((distance, (new_col, new_row, opposite_direction(direction))))


if __name__ == "__main__":
    main()
