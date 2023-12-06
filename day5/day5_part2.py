# (c) Copyright 2023 Marcel


def _number_in_line(line: str):
    """True if there is a number in the line."""
    for char in line:
        if char.isdigit():
            return True
    
    return False


def is_a_valid_seed(value, seeds):
    """True if the value is in the initial seeds."""
    for seed_range in seeds:
        if seed_range[0] <= value < seed_range[0] + seed_range[1]:
            return True
    return False


def main():
    with open("day5/input.txt") as f:
        lines = f.readlines()
        seeds = lines[0].replace("\n", "")
        seeds = seeds.replace("seeds: ", "").split(" ")
        seeds = [int(seed) for seed in seeds]
        seeds = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]

        list_of_mappings = []
        for line in lines[2:]:
            if not _number_in_line(line):
                list_of_mappings.append([])
            else:
                id_out, id_in, map_range = line.replace("\n", "").split(" ")
                id_in = int(id_in)
                id_out = int(id_out)
                map_range = int(map_range)
                list_of_mappings[-1].append([id_out, id_in, map_range])

        seed_found = False
        location = 0
        while(not seed_found):
            value = location
            for mapping in list_of_mappings[::-1]:
                mapping_applied = False
                for conversion_rule in mapping:
                    if not mapping_applied:
                        id_out, id_in, map_range = conversion_rule
                        if id_out <= value < id_out + map_range:
                            value = id_in + value - id_out
                            mapping_applied = True
                    
            if is_a_valid_seed(value, seeds):
                seed_found = True
            else:
                location += 1

    print(f"Part 2 result: {location}")


if __name__ == "__main__":
    main()
