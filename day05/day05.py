def is_fresh(ingredient: int, ranges: list[tuple[int, int]]):
    for first, last in ranges:
        if ingredient >= first and ingredient <= last:
            return True
    return False

def part1(input: str):
    ranges = []
    ingredients = []
    segment = 0
    for line in input.splitlines():
        if line == "":
            segment += 1
        elif segment == 0:
            ranges.append(tuple(int(limit) for limit in line.split("-")))
        elif segment == 1:
            ingredients.append(int(line))
        else:
            raise
    # print(ranges)
    # print(ingredients)

    fresh_count = 0
    for ingredient in ingredients:
        if is_fresh(ingredient, ranges):
            # print("Fresh", ingredient)
            fresh_count += 1
    
    return fresh_count

def part2(input: str):
    ranges = []

    for line in input.splitlines():
        if line == "":
            break
        ranges.append(tuple(int(limit) for limit in line.split("-")))

    lowest = min(start for start, end in ranges)
    highest = max(end for start, end in ranges)

    spoiled_ranges = [(lowest, highest)]

    for fresh_start, fresh_end in ranges:
        old_spoiled = [s for s in spoiled_ranges]
        # print(spoiled_ranges)
        spoiled_ranges = []
        for spoiled_start, spoiled_end in old_spoiled:
            if fresh_end >= spoiled_start or fresh_start <= spoiled_end:
                if fresh_start > spoiled_start:
                    spoiled_ranges.append((spoiled_start, min(fresh_start - 1, spoiled_end)))
                if fresh_end < spoiled_end:
                    spoiled_ranges.append((max(fresh_end + 1, spoiled_start), spoiled_end))
            else:
                spoiled_ranges.append((spoiled_start, spoiled_end))

    # print(spoiled_ranges)

    total_count = highest - lowest + 1
    spoiled_count = sum(end - start + 1 for start, end in spoiled_ranges)
    fresh_count = total_count - spoiled_count
    
    return fresh_count


if __name__ == "__main__":
    example = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

    with open("input.txt", "r") as f:
        input = f.read()
        
    print(part1(example))
    print(part2(example))

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
