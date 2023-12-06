# (c) Copyright 2023 Marcel
from tqdm import tqdm


def main():
    with open("day6/input.txt") as f:
        lines = f.readlines()
        times = lines[0].replace("Time:", "").split()
        total_time = ""
        for time in times:
            total_time += time
        total_time = int(total_time)

        records = lines[1].replace("Distance:", "").split()
        total_record = ""
        for record in records:
            total_record += record
        total_record = int(total_record)
        
        possible_distances = []
        for milliseconds_pushing in tqdm(range(total_time)):
            travelled_distance = milliseconds_pushing * (total_time - milliseconds_pushing)
            possible_distances.append(travelled_distance)
        winning_chances = sum([distance > total_record for distance in possible_distances])
        
    print(f"Part 2 result: {winning_chances}")


if __name__ == "__main__":
    main()
