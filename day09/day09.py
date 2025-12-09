
def part1(input: str):
    red_tiles = [tuple(int(x) for x in line.split(",")) for line in input.splitlines()]
    largest_area = 0
    for i, (ax, ay) in enumerate(red_tiles):
        for bx, by in red_tiles[i+1:]:
            area = (abs(bx - ax) + 1) * (abs(by - ay) + 1)
            if area > largest_area:
                largest_area = area

    # print(red_tiles)
    return largest_area

def part2(input: str):
    ...


if __name__ == "__main__":
    example = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

    with open("input.txt", "r") as f:
        input = f.read()
        
    print(part1(example))
    print(part2(example))

    print(f"Part 1: {part1(input)}")
    # print(f"Part 2: {part2(input)}")
