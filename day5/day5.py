# (c) Copyright 2023 Marcel


def _number_in_line(line: str):
    """True if there is a number in the line."""
    for char in line:
        if char.isdigit():
            return True
    
    return False

def main():
    with open("day5/input.txt") as f:
        lines = f.readlines()
        seeds = lines[0].replace("\n", "")
        seeds = seeds.replace("seeds: ", "").split(" ")
        seeds = [int(seed) for seed in seeds]

        new_mapping = True
        value = 0
        locations = []
        mapping_applied = False
        for seed in seeds:
            value = seed
            for line in lines[2:]:
                if new_mapping:
                    mapping_applied = False
                    new_mapping = False
                else:
                    if _number_in_line(line):
                        if not mapping_applied:
                            id_out, id_in, map_range = line.replace("\n", "").split(" ")
                            id_in = int(id_in)
                            id_out = int(id_out)
                            map_range = int(map_range)
                            if id_in <= value < id_in + map_range:
                                value = id_out + (value - id_in)
                                mapping_applied = True
                    else:
                        new_mapping = True
            locations.append(value)
        
    print(f"Part 1 result: {min(locations)}")


if __name__ == "__main__":
    main()
