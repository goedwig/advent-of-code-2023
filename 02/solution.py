from functools import reduce
from operator import mul

records = []

with open("./input.txt") as f:
    for line in f:
        record = []
        i = line.index(":")
        for cube_set in line[i + 1:].split("; "):
            for count_and_color in cube_set.split(", "):
                count, color = count_and_color.split()
                record.append((color, int(count)))
        records.append(record)


def part_1():
    ids_sum = 0
    max_counts = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    for id, record in enumerate(records, start=1):
        possible_game = True
        for color, count in record:
            if count > max_counts[color]:
                possible_game = False
                break
        if possible_game:
            ids_sum += id

    print(ids_sum)


def part_2():
    sum_of_powers = 0
    for record in records:
        max_counts = {}
        for color, count in record:
            max_counts[color] = max(count, max_counts.get(color, count))
        sum_of_powers += reduce(mul, max_counts.values())

    print(sum_of_powers)


part_1()
part_2()
