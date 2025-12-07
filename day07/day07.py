def part1(input: str):
    lines = input.splitlines()
    splitters = set[tuple[int, int]]()
    beams = set[int]()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            match c:
                 case "S":
                    beams.add(x)
                 case "^":
                    splitters.add((x, y))
                 case ".":
                    pass
                 case _:
                    raise
    
    split_count = 0
    for y in range(len(lines)):
        for beamx in beams.copy():
            if (beamx, y) in splitters:
                beams.remove(beamx)
                beams.add(beamx - 1)
                beams.add(beamx + 1)
                split_count += 1

    return split_count

def part2(input: str):
    lines = input.splitlines()
    splitters = set[tuple[int, int]]()
    startx = None
    height = len(lines)

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            match c:
                 case "S":
                    startx = x
                 case "^":
                    splitters.add((x, y))
                 case ".":
                    pass
                 case _:
                    raise

    assert startx is not None

    memo = {}
    def explore_timeline(x: int, y: int, counter: int):
        if y >= height:
            return counter
        
        if (x, y) in memo:
            return memo[(x, y)]
        
        if (x, y) in splitters:
            counter = (
                explore_timeline(x - 1, y + 1, counter)
                +
                explore_timeline(x + 1, y + 1, counter)
            )
        else:
            counter = explore_timeline(x, y + 1, counter)

        memo[(x, y)] = counter
        return counter
            
    return explore_timeline(startx, 0, 1)


if __name__ == "__main__":
    example = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

    with open("input.txt", "r") as f:
        input = f.read()
        
    # print(part1(example))
    # print(part2(example))

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
