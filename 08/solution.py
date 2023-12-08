from math import lcm

with open("./input.txt") as f:
    lines = f.read().strip().split("\n")

instructions = lines[0]
nodes = {line[:3]: (line[7:10], line[12:15]) for line in lines[2:]}


def part_1():
    steps = 0
    node = "AAA"
    while node != "ZZZ":
        instruction = instructions[steps % len(instructions)]
        node = nodes[node][instruction == "R"]
        steps += 1
    print(steps)


def part_2():
    a_nodes = [node for node in nodes if node[2] == "A"]
    steps_to_z_nodes = []
    for node in a_nodes:
        steps = 0
        while node[2] != "Z":
            instruction = instructions[steps % len(instructions)]
            node = nodes[node][instruction == "R"]
            steps += 1
        steps_to_z_nodes.append(steps)

    print(lcm(*steps_to_z_nodes))


part_1()
part_2()
