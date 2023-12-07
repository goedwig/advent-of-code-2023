with open("./input.txt") as f:
    lines = [l.strip() for l in f]


def part_1():
    numbers_sum = 0
    for y, l in enumerate(lines):
        num = ""
        is_adjacent = False
        for x, ch in enumerate(l):
            if ch.isdigit():
                num += ch
                for yd, xd in [(y - 1, x), (y - 1, x + 1), (y, x + 1), (y + 1, x + 1), (y + 1, x), (y + 1, x - 1),
                               (y, x - 1), (y - 1, x - 1)]:
                    try:
                        chd = lines[yd][xd]
                    except IndexError:
                        continue
                    if not chd.isdigit() and not chd == ".":
                        is_adjacent = True
                        break

            else:
                if is_adjacent:
                    numbers_sum += int(num)
                num = ""
                is_adjacent = False

        if is_adjacent:
            numbers_sum += int(num)

    print(numbers_sum)


def part_2():
    gear_ratio_sum = 0
    for y, l in enumerate(lines):
        for x, ch in enumerate(l):
            if ch != "*":
                continue

            adjacent_nums = set()

            for yd, xd in [(y - 1, x), (y - 1, x + 1), (y, x + 1), (y + 1, x + 1), (y + 1, x), (y + 1, x - 1),
                           (y, x - 1), (y - 1, x - 1)]:
                try:
                    chd = lines[yd][xd]
                except IndexError:
                    continue

                if not chd.isdigit():
                    continue

                num = chd

                xdd = xd
                while True:
                    xdd -= 1
                    if xdd < 0 or not lines[yd][xdd].isdigit():
                        break
                    num = lines[yd][xdd] + num

                xdd = xd
                while True:
                    xdd += 1
                    if xdd >= len(l) or not lines[yd][xdd].isdigit():
                        break
                    num = num + lines[yd][xdd]

                adjacent_nums.add(int(num))

            if len(adjacent_nums) == 2:
                gear_ratio_sum += adjacent_nums.pop() * adjacent_nums.pop()

    print(gear_ratio_sum)


part_1()
part_2()
