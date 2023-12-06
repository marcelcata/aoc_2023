# (c) Copyright 2023 Marcel


def main():
    with open("day4/input.txt") as f:
        cards = f.readlines()
        list_num_copies = [1 for _ in cards]

        for i, (num_copies, card) in enumerate(zip(list_num_copies, cards)):
            _, numbers = card.replace("\n", "").split(":")
            winner_numbers, numbers_you_have = numbers.split("|")

            winner_numbers = winner_numbers.strip().replace("  ", " ").split(" ")
            numbers_you_have = numbers_you_have.strip().replace("  ", " ").split(" ")

            winning_numbers = sum(num in winner_numbers for num in numbers_you_have)

            for j in range(winning_numbers):
                list_num_copies[i + j + 1] += num_copies
            
        result = sum(list_num_copies)

    print(f"Part 2 result: {result}")


if __name__ == "__main__":
    main()
