# (c) Copyright 2023 Marcel
from collections import Counter


HANDS = [
    "five", "four", "full_house", "three", "double_pair", "pair", "high_card"
]
CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


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

        if counts[5] == 1:
            self.value = "five"
        elif counts[4] == 1:
            self.value = "four"
        elif counts[3] == 1 and counts[2] == 1:
            self.value = "full_house"
        elif counts[3] == 1:
            self.value = "three"
        elif counts[2] == 2:
            self.value = "double_pair"
        elif counts[2] == 1:
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
            print(hand, bet)
            list_of_hands.append(Hand(hand, bet=int(bet)))

        # Compute final result over sorted list
        result = 0
        for i, hand in enumerate(sorted(list_of_hands)):
            result += (i+1) * hand.bet
        
    print(f"Part 1 result: {result}")


if __name__ == "__main__":
    main()
