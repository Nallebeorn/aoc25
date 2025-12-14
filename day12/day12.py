from dataclasses import dataclass

@dataclass
class Region:
    width: int
    height: int
    quantities: tuple[int, ...]

@dataclass(frozen=True)
class Shape:
    WIDTH = 3
    HEIGHT = 3

    cells: frozenset[tuple[int, int]]

    def size(self):
        return len(self.cells)
    
    def rotated(self):
        shape = self
        return Shape(frozenset((Shape.WIDTH - y - 1, x) for x, y in shape.cells))

    def display(self):
        output = ""
        for y in range(Shape.HEIGHT):
            for x in range(Shape.WIDTH):
                output += "#" if (x, y) in self.cells else "."
            output += "\n"

        return output.strip()

def can_fit_shapes_in_region(presents: list[Shape], region: Region):
    total_space = region.width * region.height
    space_needed = sum(presents[shape_idx].size() * count for shape_idx, count in enumerate(region.quantities))
    maximum_space_needed = sum(Shape.WIDTH * Shape.HEIGHT * count for count in region.quantities)

    if space_needed > total_space:
        return False
    if maximum_space_needed <= total_space:
        return True
    
    assert False, "Unsolvable input!"

def part1(input: str):
    lines = input.splitlines()
    regions: list[Region] = []
    shapes: list[Shape] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line and line[-1] == ":":
            i += 1
            y = 0
            shape = set[tuple[int, int]]()
            while lines[i]:
                for x, c in enumerate(lines[i]):
                    if c == "#":
                        shape.add((x, y))

                y += 1
                i += 1
            shapes.append(Shape(frozenset(shape)))

        if "x" in line:
            splitted = line.split()
            width, height = tuple(int(n) for n in splitted[0].rstrip(":").split("x"))
            quantities = tuple(int(n) for n in splitted[1:])
            regions.append(Region(width, height, quantities))
        
        i += 1

    count = 0
    for i, region in enumerate(regions):
        # print("region", region)
        # print(f"{i}/{len(regions)} ({count})")
        if can_fit_shapes_in_region(shapes, region):
            count += 1

    return count
        

def part2(input: str):
    ...

if __name__ == "__main__":
    example = """\
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

    with open("input.txt", "r") as f:
        input = f.read()
        
    # print(part1(example))
    # print(part2(example2))

    print(f"Part 1: {part1(input)}")
    # print(f"Part 2: {part2(input)}")
# 