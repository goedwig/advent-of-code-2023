plan_1, plan_2 = [], []
with open("./input.txt") as f:
    for line in f:
        direction_1, distance_1, hex_code = line.split()
        plan_1.append((direction_1, int(distance_1)))
        distance_2 = {"0": "R", "1": "D", "2": "L", "3": "U"}[hex_code[-2]]
        value_2 = int(hex_code[2:-2], base=16)
        plan_2.append((distance_2, value_2))

deltas = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def process_instructions(plan):
    row = col = 0
    vertices = []
    perimeter = 0

    for instruction in plan:
        direction, distance = instruction
        d_row, d_col = deltas[direction]
        perimeter += distance
        row += d_row * distance
        col += d_col * distance
        vertices.append((row, col))

    return vertices, perimeter


def area(vertices, perimeter):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    area = (abs(area) / 2) + (perimeter / 2) + 1
    return area


# part 1
print(area(*process_instructions(plan_1)))

# part 2
print(area(*process_instructions(plan_2)))
