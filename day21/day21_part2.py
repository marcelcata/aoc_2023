# (c) Copyright 2023 Marcel
from collections import deque


def compute_reachable_plots(garden, start_row, start_col, steps):
    size = len(garden)
    reachable_plots = set()
    visited_plots = set((start_row, start_col))
    queue = deque()
    queue.append((start_row, start_col, steps))
    while queue:
        row, col, steps = queue.popleft()
        if steps % 2 == 0:
            reachable_plots.add((row, col))
        if steps == 0:
            continue
        
        # Check the neighbours
        for next_row, next_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
            if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size:
                continue
            if garden[next_row][next_col] == "#":
                continue
            if (next_row, next_col) in visited_plots:
                continue
            visited_plots.add((next_row, next_col))
            queue.append((next_row, next_col, steps - 1))

    return len(reachable_plots)


def main():
    with open("day21/input.txt") as f:
        garden = f.readlines()
    num_steps = 64
    start = "S"
    start_row, start_col = None, None
    for i, row in enumerate(garden):
        for j, _ in enumerate(row):
            if garden[i][j] == start:
                start_row, start_col = i, j
    
    print(f"Part 1 result: {compute_reachable_plots(garden, start_row, start_col, num_steps)}")

    num_steps = 26501365
    size = len(garden)  # Garden is squared
    
    num_gardens = num_steps // size - 1  # Amount of full gardens that can be travelled in same direction

    odd = (num_gardens // 2 * 2 + 1) ** 2
    even = ((num_gardens + 1) // 2 * 2) ** 2

    # Compute value for fully reachable plots
    odd_points = compute_reachable_plots(garden, start_row, start_col, size * 2 + 1)
    even_points = compute_reachable_plots(garden, start_row, start_col, size * 2)

    # Compute value for corner plots
    corner_t = compute_reachable_plots(garden, size - 1, start_col, size - 1)
    corner_r = compute_reachable_plots(garden, start_row, 0, size - 1)
    corner_b = compute_reachable_plots(garden, 0, start_col, size - 1)
    corner_l = compute_reachable_plots(garden, start_row, size - 1, size - 1)

    # Compute value for plots that are reached only on one of their corners, specified by tblr
    small_tr = compute_reachable_plots(garden, size - 1, 0, size // 2 - 1)
    small_tl = compute_reachable_plots(garden, size - 1, size - 1, size // 2 - 1)
    small_br = compute_reachable_plots(garden, 0, 0, size // 2 - 1)
    small_bl = compute_reachable_plots(garden, 0, size - 1, size // 2 - 1)

    # Compute value for plots that are fully reached except on one of their corners, specified by tblr
    large_tr = compute_reachable_plots(garden, size - 1, 0, size * 3 // 2 - 1)
    large_tl = compute_reachable_plots(garden, size - 1, size - 1, size * 3 // 2 - 1)
    large_br = compute_reachable_plots(garden, 0, 0, size * 3 // 2 - 1)
    large_bl = compute_reachable_plots(garden, 0, size - 1, size * 3 // 2 - 1)

    num_reachable_plots = (
        odd * odd_points + even * even_points + corner_t + corner_r + corner_b + corner_l +
        (num_gardens + 1) * (small_tr + small_tl + small_br + small_bl) +
        num_gardens * (large_tr + large_tl + large_br + large_bl)
    )

    print(f"Part 2 result: {num_reachable_plots}")



            




if __name__ == "__main__":
    main()
