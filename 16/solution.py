with open("./input.txt") as f:
    field = f.read().strip().split("\n")


def get_energized_num(starting_beam):
    beams = [starting_beam]
    passed_beams = set()
    energized = set()

    while True:
        if not beams:
            break

        new_beams = []
        for beam in beams:
            if beam in passed_beams:
                continue

            (row, col), (d_row, d_col) = beam

            if row < 0 or row >= len(field) or col < 0 or col >= len(field[0]):
                continue

            cell = field[row][col]
            energized.add((row, col))

            match cell:
                case ".":
                    new_beams.append(((row + d_row, col + d_col), (d_row, d_col)))
                case "\\":
                    if d_col == 1:  # moving right
                        new_beams.append(((row + 1, col), (1, 0)))
                    elif d_col == -1:  # moving left
                        new_beams.append(((row - 1, col), (-1, 0)))
                    elif d_row == 1:  # moving down
                        new_beams.append(((row, col + 1), (0, 1)))
                    elif d_row == -1:  # moving up
                        new_beams.append(((row, col - 1), (0, -1)))
                    else:
                        raise ValueError
                case "/":
                    if d_col == 1:  # moving right
                        new_beams.append(((row - 1, col), (-1, 0)))
                    elif d_col == -1:  # moving left
                        new_beams.append(((row + 1, col), (1, 0)))
                    elif d_row == 1:  # moving down
                        new_beams.append(((row, col - 1), (0, -1)))
                    elif d_row == -1:  # moving up
                        new_beams.append(((row, col + 1), (0, 1)))
                    else:
                        raise ValueError
                case "|":
                    if d_col != 0:  # moving left or right:
                        new_beams.append(((row - 1, col), (-1, 0)))
                        new_beams.append(((row + 1, col), (1, 0)))
                    else:
                        new_beams.append(((row + d_row, col + d_col), (d_row, d_col)))
                case "-":
                    if d_row != 0:  # moving up or down
                        new_beams.append(((row, col - 1), (0, -1)))
                        new_beams.append(((row, col + 1), (0, 1)))
                    else:
                        new_beams.append(((row + d_row, col + d_col), (d_row, d_col)))
                case _:
                    raise ValueError

            passed_beams.add(beam)

        beams = new_beams

    return len(energized)


# Beam is defined as: ((row, col), (row delta, col delta))
# part 1
print(get_energized_num(((0, 0), (0, 1))))

# part 2
beams = []
max_row, max_col = len(field) - 1, len(field[0]) - 1

for i in range(len(field)):
    beams += [
        ((i, 0), (0, 1)),
        ((i, max_col), (0, -1)),
    ]

for i in range(len(field[0])):
    beams += [
        ((0, i), (1, 0)),
        ((max_row, i), (-1, 0)),
    ]

max_energized = 0
for beam in beams:
    max_energized = max(max_energized, get_energized_num(beam))

print(max_energized)
