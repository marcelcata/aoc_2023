# (c) Copyright 2023 Marcel
from collections import Counter


HANDS = [
    "five", "four", "full_house", "three", "double_pair", "pair", "high_card"
]
CARDS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


# Helper functions to check hand value
def _is_a_five(counts, joker_amount):
    if counts[5]:
        return True
    if counts[4] and joker_amount == 1:
        return True
    if counts[3] and joker_amount == 2:
        return True
    if counts[2] == 1 and joker_amount == 3:
        return True
    if counts[1] == 1 and joker_amount == 4:
        return True
    if joker_amount == 5:
        return True
    return False


def _is_a_four(counts, joker_amount):
    if counts[4]:
        return True
    if counts[3] and joker_amount == 1:
        return True
    if counts[2] == 2 and joker_amount == 2:
        return True
    if counts[1] == 2 and joker_amount == 3:
        return True
    return False


def _is_a_full_house(counts, joker_amount):
    if counts[3] == 1 and counts[2] == 1:
        return True
    if counts[2] == 2 and joker_amount == 1:
        return True
    return False


def _is_a_three(counts, joker_amount):
    if counts[3] == 1:
        return True
    if counts[2] == 1 and joker_amount == 1:
        return True
    if counts[2] == 1 and joker_amount == 2:
        return True
    if counts[1] == 1 and joker_amount == 2:
        return True
    return False


def _is_a_double_pair(counts):
    if counts[2] == 2:
        return True
    return False


def _is_a_pair(counts, joker_amount):
    if counts[2] == 1:
        return True
    if counts[1] == 5 and joker_amount == 1:
        return True
    return False


class Hand:
    def __init__(self, hand, bet):
        """Initialize."""
        self.hand = hand
        self.bet = bet
        self.value = "not_set"
        self._compute_hand_value()

    def _compute_hand_value(self):
        """Get the hand value."""
        card_counter = Counter(self.hand)
        counts = Counter(card_counter.values())
        joker_amount = card_counter["J"]
        if _is_a_five(counts, joker_amount):
            self.value = "five"
        elif _is_a_four(counts, joker_amount):
            self.value = "four"
        elif _is_a_full_house(counts, joker_amount):
            self.value = "full_house"
        elif _is_a_three(counts, joker_amount):
            self.value = "three"
        elif _is_a_double_pair(counts):
            self.value = "double_pair"
        elif _is_a_pair(counts, joker_amount):
            self.value = "pair"
        else:
            self.value = "high_card"

    def __gt__(self, other):
        """Greater than definition."""
        if HANDS.index(self.value) < HANDS.index(other.value):
            return True
        if HANDS.index(self.value) == HANDS.index(other.value):
            for own_card, other_card in zip(self.hand, other.hand):
                if CARDS.index(own_card) < CARDS.index(other_card):
                    return True
                elif CARDS.index(own_card) > CARDS.index(other_card):
                    return False
        return False


def main():
    with open("day7/input.txt") as f:
        
        # Accumulate hands
        list_of_hands = []
        for line in f.readlines():
            hand, bet = line.replace("\n", "").split(" ")
            list_of_hands.append(Hand(hand, bet=int(bet)))

        # Compute final result over sorted list of hands
        result = 0
        for i, hand in enumerate(sorted(list_of_hands)):
            result += (i+1) * hand.bet
        
    print(f"Part 2 result: {result}")


if __name__ == "__main__":
    main()
