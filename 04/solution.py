with open("./input.txt") as f:
    lines = [l.strip() for l in f]

pile = []

total_points = 0

for l in lines:
    numbers = l.split(":")[1]
    winning_numbers, given_numbers = numbers.split("|")
    winning_numbers = {int(n) for n in winning_numbers.split()}
    given_numbers = [int(n) for n in given_numbers.split()]

    card = (winning_numbers, given_numbers)

    pile.append([card])

    # part 1
    points = 0
    for n in given_numbers:
        if n in winning_numbers:
            points = points * 2 if points else 1
    total_points += points

print(total_points)

# part 2
for i, cards in enumerate(pile):
    for card in cards:
        winning_numbers, given_numbers = card
        matches_count = len(winning_numbers.intersection(given_numbers))

        pile_to_copy = pile[(i + 1):(i + 1 + matches_count)]

        for cards_to_copy in pile_to_copy:
            cards_to_copy.append(cards_to_copy[0])

print(sum(len(cards) for cards in pile))
