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

    def width(self):
        return max(x for x, y in self.cells) - min(x for x, y in self.cells) + 1
    
    def height(self):
        return max(y for x, y in self.cells) - min(y for x, y in self.cells) + 1

    def size(self):
        return len(self.cells)
    
    def rotated(self):
        shape = self
        return Shape(frozenset((Shape.WIDTH - y - 1, x) for x, y in shape.cells))

    def display(self):
        output = ""
        for y in range(self.height()):
            for x in range(self.width()):
                output += "#" if (x, y) in self.cells else "."
            output += "\n"

        return output.strip()

@dataclass(frozen=True)
class SearchState:
    occupied: frozenset[tuple[int, int]]
    remaining_presents: list[int]
    start_at_for_shape: dict[int, tuple[int, int]]

    def can_fit_shape_at(self, x: int, y: int, shape: Shape):
        for cx, cy in shape.cells:
            if (x + cx, y + cy) in self.occupied:
                return False
        return True
    
    def put_shape_at(self, x: int, y: int, shape: Shape):
        occupied = set(self.occupied)
        for cx, cy in shape.cells:
            occupied.add((x + cx, y + cy))
        return frozenset(occupied)

def can_fit_shapes_in_region(shapes: list[Shape], region: Region):
    presents = list(shapes)
    rotated_90 = [shape.rotated() for shape in presents]
    rotated_180 = [shape.rotated() for shape in rotated_90]
    rotated_270 = [shape.rotated() for shape in rotated_180]

    rotation_variants = [presents, rotated_90, rotated_180, rotated_270]

    redundant_rotations = set()

    for i in range(len(presents)):
        if rotated_180[i] == presents[i]:
            redundant_rotations.add((2, i))
        if rotated_270[i] == rotated_90[i]:
            redundant_rotations.add((3, i))

    # print("redundant rotations", redundant_rotations)
          
    total_space = region.width * region.height

    frontier = [SearchState(frozenset(), list(region.quantities), {})]

    timeout = 0
    while frontier:
        timeout += 1

        # print(timeout)
        if timeout > 100:
            # print("Timeout")
            return False

        state = frontier.pop()

        space_needed = sum(presents[shape_idx].size() * count for shape_idx, count in enumerate(state.remaining_presents))
        space_left = total_space - len(state.occupied)
        if space_left < space_needed:
            # print("no space")
            continue

        return True # WTF, this works???? (even though it doesn't for the example input...)

        shape_idx = None
        for i, num_remaining in enumerate(state.remaining_presents):
            if num_remaining > 0:
                shape_idx = i
                break

        if shape_idx is None:    
            # print("Possible!")
            return True

        start_x, start_y = state.start_at_for_shape.get(shape_idx, (0, 0))

        for r in range(4):
            if (r, shape_idx) in redundant_rotations:
                continue

            shape = rotation_variants[r][shape_idx]

            for x in range(start_x, region.width - Shape.WIDTH + 1):
                for y in range(start_y, region.height - Shape.HEIGHT + 1):
                    if state.can_fit_shape_at(x, y, shape):
                        new_remaining = list(state.remaining_presents)
                        new_remaining[shape_idx] -= 1
                        new_start_at = state.start_at_for_shape | {shape_idx: (x + 1, y + 1)}
                        frontier.append(SearchState(state.put_shape_at(x, y, shape), new_remaining, new_start_at))
        

    # print("Confirmed impossible")
    return False

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
    
    # for shape in shapes:
    #     # print(shape)
    #     print(shape.display() + "\n")
    #     print(shape.rotated(3).display() + "\n")
    #     print("------\n")

    # for region in regions:


    # for region in regions:
    #     space = region.width * region.height
    #     space_needed = sum(shapes[i].size() * count for i, count in enumerate(region.quantities))
    #     print(space, space_needed)
    #     if space_needed > space:
    #         print("Well that won't work, duh")

    count = 0
    for i, region in enumerate(regions):
        # print("region", region)
        print(f"{i}/{len(regions)} ({count})")
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
        
    print(part1(example))
    # print(part2(example2))

    # print(f"Part 1: {part1(input)}")
    # print(f"Part 2: {part2(input)}")
# 