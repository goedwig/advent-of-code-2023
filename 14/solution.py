with open("./input.txt") as f:
    rows = [list(row) for row in f.read().strip().split("\n")]


def tilt_north(rows):
    for i in range(1, len(rows)):
        for j in range(len(rows[0])):
            if rows[i][j] != "O":
                continue
            k = i
            while k > 0:
                if rows[k - 1][j] == ".":
                    k -= 1
                else:
                    break
            rows[i][j] = "."
            rows[k][j] = "O"
    return rows


def tilt_south(rows):
    rows = rows[::-1]
    rows = tilt_north(rows)
    return rows[::-1]


def tilt_west(rows):
    rows = [list(x) for x in zip(*rows)]
    rows = tilt_north(rows)
    return [list(x) for x in zip(*rows)]


def tilt_east(rows):
    rows = [row[::-1] for row in rows]
    rows = tilt_west(rows)
    return [row[::-1] for row in rows]


def part_1(rows):
    rows = rows[::]
    rows = tilt_north(rows)
    print(sum(row.count("O") * i for i, row in enumerate(rows[::-1], start=1)))


def part_2(rows):
    rows = rows[::]
    tilts = [tilt_north, tilt_west, tilt_south, tilt_east]

    patterns = {}
    sums = []
    i = 0
    while True:
        tilt = tilts[i % len(tilts)]
        rows = tilt(rows)
        pattern = hash(tuple(tuple(row) for row in rows))

        if pattern in patterns:
            break
        else:
            patterns[pattern] = i
            sums.append(
                sum(row.count("O") * i for i, row in enumerate(rows[::-1], start=1))
            )
        i += 1

    i_repeat = patterns[pattern]
    repeat_interval = i - i_repeat

    j = i_repeat + ((1000000000 * 4 - 1 - i_repeat) % repeat_interval)
    print(sums[j])


part_1(rows)
part_2(rows)
