from collections import Counter

hands = []
with open("./input.txt") as f:
    for line in f:
        hand, bid = line.split()
        hands.append((hand, int(bid)))


def hand_strength(hand):
    frequencies = sorted(Counter(hand).values())
    match frequencies:
        case [5]:  # Five of a kind
            return 6
        case [1, 4]:  # Four of a kind
            return 5
        case [2, 3]:  # Full house
            return 4
        case [1, 1, 3]:  # Three of a kind
            return 3
        case [1, 2, 2]:  # Two pair
            return 2
        case [1, 1, 1, 2]:  # One pair
            return 1
        case _:
            return 0


def card_strength(card, part_two):
    if part_two:
        return "J23456789TQKA".index(card)
    else:
        return "23456789TJQKA".index(card)


def sorted_hands(hands, part_two=False):
    def key(hand):
        if part_two:
            f = jokerize_hand
        else:
            f = lambda x: x
        return hand_strength(f(hand[0])), tuple(card_strength(card, part_two) for card in hand[0])

    return sorted(hands, key=key)


def jokerize_hand(hand):
    if "J" not in hand:
        return hand

    labels = {l for l in hand if l != "J"}

    max_hand_strength = hand_strength(hand)
    max_card_strength = card_strength("J", part_two=True)
    new_hand = hand

    for label in labels:
        jokerized = hand.replace("J", label)
        new_hand_strength = hand_strength(jokerized)
        new_card_strength = card_strength(label, part_two=True)

        if (
            new_hand_strength > max_hand_strength
            or new_hand_strength == max_hand_strength and new_card_strength > max_card_strength
        ):
            max_hand_strength = new_hand_strength
            max_card_strength = new_card_strength
            new_hand = jokerized

    return new_hand


# Part 1
hands = sorted_hands(hands)
print(sum(rank * bid for rank, (_, bid) in enumerate(hands, start=1)))

# Part 2
hands = sorted_hands(hands, part_two=True)
print(sum(rank * bid for rank, (_, bid) in enumerate(hands, start=1)))
