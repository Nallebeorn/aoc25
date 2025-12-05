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
    ...


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
    # print(part2(example))

    print(f"Part 1: {part1(input)}")
    # print(f"Part 2: {part2(input)}")
