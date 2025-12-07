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
    ...


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
        
    print(part1(example))
    # print(part2(example))

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
