# (c) Copyright 2023 Marcel


def main():
    with open("day6/input.txt") as f:
        lines = f.readlines()
        times = lines[0].replace("Time:", "").split()
        times = [int(time) for time in times]
        records = lines[1].replace("Distance:", "").split()
        records = [int(record) for record in records]
        
        result = 1
        for time, record in zip(times, records):
            possible_distances = []
            for milliseconds_pushing in range(time):
                travelled_distance = milliseconds_pushing * (time - milliseconds_pushing)
                possible_distances.append(travelled_distance)
            winning_chances = sum([distance > record for distance in possible_distances])
            result *= winning_chances
        
    print(f"Part 1 result: {result}")


if __name__ == "__main__":
    main()
