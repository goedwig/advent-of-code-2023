def part_1():
    races = [(53, 275), (71, 1181), (78, 1215), (80, 1524)]
    result = 1
    for time, distance in races:
        result *= sum(hold_time * (time - hold_time) > distance for hold_time in range(1, time))
    print(result)


def part_2():
    time, distance = 53717880, 275118112151524
    print(sum(hold_time * (time - hold_time) > distance for hold_time in range(1, time)))


part_1()
part_2()
