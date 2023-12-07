with open("./input.txt") as f:
    lines = f.read().strip().split("\n")

seeds = [int(n) for n in lines[0].removeprefix("seeds: ").split()]

maps = []
for start, end in [(3, 51), (53, 89), (91, 121), (123, 149), (151, 195),
                   (197, 204), (206, 248)]:
    m = []
    for line in lines[start:end]:
        m.append([int(n) for n in line.split()])
    maps.append(m)


def part_1():
    source = seeds
    for m in maps:
        new_source = []
        for source_number in source:
            for dest_start, source_start, numbers_range in m:
                if source_start <= source_number < source_start + numbers_range:
                    new_source.append(dest_start + (source_number - source_start))
                    break
            else:
                new_source.append(source_number)

        source = new_source

    print(min(source))


def part_2():
    source = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds) - 1, 2)]
    for m in maps:
        new_source = []
        while len(source):
            source_start, length = source.pop(0)
            source_end = source_start + length

            for dest_start_map, source_start_map, length_map in m:
                source_end_map = source_start_map + length_map

                # Ranges don't intersect
                if source_start >= source_end_map or source_end <= source_start_map:
                    continue

                # Fully covered by mapped
                if source_start >= source_start_map and source_end <= source_end_map:
                    new_source_start = dest_start_map + (source_start - source_start_map)
                    new_length = length
                # Fully covers mapped
                elif source_start < source_start_map and source_end > source_end_map:
                    new_source_start = source_start_map
                    new_length = length_map
                    source += [
                        (source_start, source_start_map - source_start),
                        (source_end_map, source_end - source_end_map),
                    ]
                # Covers from left side
                elif source_start >= source_start_map:
                    new_source_start = dest_start_map + (source_start - source_start_map)
                    new_length = source_end_map - source_start
                    source.append((source_end_map, source_end - source_end_map))
                # Covers from right side
                else:
                    new_source_start = dest_start_map
                    new_length = source_end - source_start_map
                    source.append((source_start, source_start_map - source_start))

                new_source.append((new_source_start, new_length))

                break
            else:
                new_source.append((source_start, length))

        source = new_source

    print(min(t[0] for t in source))


part_1()
part_2()
