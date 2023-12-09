lines = []
with open("./input.txt") as f:
    for line in f:
        lines.append([int(n) for n in line.split()])

result_1 = 0
result_2 = 0
for history in lines:
    difference = history
    differences = [difference]
    while any(n != 0 for n in difference):
        new_difference = []
        for i in range(len(difference) - 1):
            new_difference.append(difference[i + 1] - difference[i])
        difference = new_difference
        differences.append(difference)

    differences[-1].append(0)
    for i in range(len(differences) - 1, 0, -1):
        differences[i - 1].append(differences[i][-1] + differences[i - 1][-1])
        differences[i - 1].insert(0, differences[i - 1][0] - differences[i][0])

    result_1 += differences[0][-1]
    result_2 += differences[0][0]

print(result_1)
print(result_2)
