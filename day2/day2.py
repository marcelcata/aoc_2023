# (c) Copyright 2023 Marcel

# Part 1: 12 red cubes, 13 green cubes, and 14 blue cubes
MAX_CUBES = {"red": 12, "green": 13, "blue": 14}

result = 0
with open("day2/input.txt") as f:
    for line in f.readlines():
        game_id, game = line.split(":")
        valid_game = True
        
        # Each play will have the format "X green, X blue, X red"
        plays = game.split(";")
        for play in plays:
            cubes_by_color = play.split(",")
            for amount_and_color in cubes_by_color:
                amount, color = amount_and_color.strip().split(" ")
                if int(amount) > MAX_CUBES[color]:
                    valid_game = False

        if valid_game:
            game_number = int(game_id.replace("Game ", ""))
            result += game_number
    
print(f"Part 1 result: {result}")


# Part 2: Minimum amount of cubes
result = 0
with open("day2/input.txt") as f:
    for line in f.readlines():
        _, game = line.split(":")
        min_amount_to_play = {"red": 0, "green": 0, "blue": 0}

        # Each play will have the format "X green, X blue, X red"
        plays = game.split(";")
        for play in plays:
            cubes_by_color = play.split(",")
            for amount_and_color in cubes_by_color:
                amount, color = amount_and_color.strip().split(" ")
                if int(amount) > min_amount_to_play[color]:
                    min_amount_to_play[color] = int(amount)

        result += min_amount_to_play["red"] * min_amount_to_play["green"] * min_amount_to_play["blue"]
    
print(f"Part 2 result: {result}")