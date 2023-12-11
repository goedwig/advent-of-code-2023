with open("./input.txt") as f:
    lines = [list(s) for s in f.read().split()]

ROWS, COLS = len(lines), len(lines[0])

expand_rows = []
for i in range(ROWS):
    for j in range(COLS):
        if lines[i][j] == "#":
            break
    else:
        expand_rows.append(i)

expand_cols = []
for j in range(COLS):
    for i in range(ROWS):
        if lines[i][j] == "#":
            break
    else:
        expand_cols.append(j)

galaxies = []
for i in range(ROWS):
    for j in range(COLS):
        if lines[i][j] == "#":
            galaxies.append((i, j))


def shortest_path(g1, g2, expand_value):
    deltas = []

    d = (g1[0] < g2[0]) - (g1[0] > g2[0])
    row_d = (d, 0)
    if d:
        deltas.append(row_d)

    d = (g1[1] < g2[1]) - (g1[1] > g2[1])
    col_d = (0, d)
    if d:
        deltas.append(col_d)

    path_length = 0
    i = 0
    while g1 != g2:
        d = deltas[i % len(deltas)]

        g1 = g1[0] + d[0], g1[1] + d[1]

        if d == row_d and g1[0] in expand_rows or d == col_d and g1[1] in expand_cols:
            path_length += expand_value
        else:
            path_length += 1

        if len(deltas) == 2:
            if g1[0] == g2[0]:
                deltas.pop(0)
            elif g1[1] == g2[1]:
                deltas.pop(1)

        i += 1

    return path_length


result_1, result_2 = 0, 0
for i in range(len(galaxies) - 1):
    current_galaxy = galaxies[i]
    for next_galaxy in galaxies[i + 1:]:
        result_1 += shortest_path(current_galaxy, next_galaxy, expand_value=2)
        result_2 += shortest_path(current_galaxy, next_galaxy, expand_value=1000000)

print(result_1)
print(result_2)
