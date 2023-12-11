with open("./input.txt") as f:
    lines = [list(s) for s in f.read().split()]

pipes = {
    "|": {"U": ((-1, 0), "U"), "D": ((1, 0), "D")},
    "-": {"L": ((0, -1), "L"), "R": ((0, 1), "R")},
    "L": {"D": ((0, 1), "R"), "L": ((-1, 0), "U")},
    "J": {"D": ((0, -1), "L"), "R": ((-1, 0), "U")},
    "7": {"R": ((1, 0), "D"), "U": ((0, -1), "L")},
    "F": {"L": ((1, 0), "D"), "U": ((0, 1), "R")},
}


def next_pipe(current_pipe, direction_taken):
    current_pipe_type = lines[current_pipe[0]][current_pipe[1]]
    delta, next_direction = pipes[current_pipe_type][direction_taken]
    return (current_pipe[0] + delta[0], current_pipe[1] + delta[1]), next_direction


S = (107, 110)

lines[S[0]][S[1]] = "F"

current_pipe = (108, 110)
direction_taken = "D"
steps = 1
involved_nodes = [S]

while current_pipe != S:
    involved_nodes.append(current_pipe)
    current_pipe, direction_taken = next_pipe(current_pipe, direction_taken)
    steps += 1

# Part 1
print(steps // 2)


def actual_intersections(possible_intersections):
    s = "".join(possible_intersections)
    replacements = ("L7", "FJ")
    for replacement in replacements:
        s = s.replace(replacement, "|")
    return sum(ch == "|" for ch in s)


enclosed_nodes = []
for i in range(len(lines)):
    min_j = min(j for i, j in involved_nodes if i == i) + 1
    max_j = max(j for i, j in involved_nodes if i == i) + 1

    for j in range(min_j, max_j - 1):
        if (i, j) in involved_nodes:
            continue
        possible_intersections = []
        for k in range(j + 1, max_j):
            if (i, k) in involved_nodes and lines[i][k] != "-":
                possible_intersections.append(lines[i][k])

        if actual_intersections(possible_intersections) % 2:
            enclosed_nodes.append((i, j))

# Part 2
print(len(enclosed_nodes))
