from functools import reduce

with open("./input.txt") as f:
    sequence = f.read().strip().split(",")


def get_hash(step):
    return reduce(lambda r, ch: (r + ord(ch)) * 17 % 256, step, 0)


# part 1
print(sum(get_hash(step) for step in sequence))

boxes = [{} for _ in range(256)]
for step in sequence:
    if step[-1] == "-":
        label = step[:-1]
        box_idx = get_hash(label)
        boxes[box_idx].pop(label, None)
    else:
        focal_length = int(step[-1])
        label = step[:-2]
        box_idx = get_hash(label)
        boxes[box_idx][label] = focal_length

# part 2
result_2 = 0
for i, box in enumerate(boxes, start=1):
    for j, focal_length in enumerate(box.values(), start=1):
        result_2 += i * j * focal_length

print(result_2)
