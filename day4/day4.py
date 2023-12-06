# (c) Copyright 2023 Marcel


def main():
    with open("day4/input.txt") as f:
        result = 0
        for line in f.readlines():
            _, numbers = line.replace("\n", "").split(":")
            winner_numbers, numbers_you_have = numbers.split("|")

            winner_numbers = winner_numbers.strip().replace("  ", " ").split(" ")
            numbers_you_have = numbers_you_have.strip().replace("  ", " ").split(" ")

            card_score = 0
            for num in numbers_you_have:
                if num in winner_numbers:
                    if card_score == 0:
                        card_score = 1
                    else:
                        card_score *= 2

            result += card_score

    print(f"Part 1 result: {result}")


if __name__ == "__main__":
    main()
