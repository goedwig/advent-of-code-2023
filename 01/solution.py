with open("./input.txt") as f:
    lines = f.read().split()


def part_1():
    calibration_values_sum = 0
    for line in lines:
        digits = []
        for ch in line:
            if ch.isdigit():
                digits.append(ch)
        calibration_values_sum += int(digits[0] + digits[-1])
    print(calibration_values_sum)


def part_2():
    calibration_values_sum = 0
    replacements = [
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]
    for line in lines:
        first_digit = ""
        for ch in line:
            if ch.isdigit():
                first_digit = ch
                break

            first_digit += ch

            found = False
            for replacement in replacements:
                if replacement[0] in first_digit:
                    first_digit = replacement[1]
                    found = True
                    break
            if found:
                break

        last_digit = ""
        for ch in line[::-1]:
            if ch.isdigit():
                last_digit = ch
                break

            last_digit = ch + last_digit

            found = False
            for replacement in replacements:
                if replacement[0] in last_digit:
                    last_digit = replacement[1]
                    found = True
                    break

            if found:
                break

        calibration_values_sum += int(first_digit + last_digit)

    print(calibration_values_sum)


part_1()  # 52974
part_2()  # 53340
