from dataclasses import dataclass, field

@dataclass
class Region:
    width: int
    height: int
    quantities: tuple[int, ...]

@dataclass(frozen=True)
class Shape:
    cells: frozenset[tuple[int, int]]

    def width(self):
        return max(x for x, y in self.cells) - min(x for x, y in self.cells) + 1
    
    def height(self):
        return max(y for x, y in self.cells) - min(y for x, y in self.cells) + 1

    def size(self):
        return len(self.cells)
    
    def rotated(self, n = 1):
        assert n >= 1 and n <= 4
        shape = self
        for i in range(n):
            shape = Shape(frozenset((shape.width() - y - 1, x) for x, y in shape.cells))
        return shape

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
    remaining_presents: int

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
    presents: list[Shape] = []
    for i, count in enumerate(region.quantities):
        for c in range(count):
            presents.append(shapes[i])

    total_space_needed = sum(shape.size() for shape in presents)
    total_space = region.width * region.height
    
    if total_space_needed > total_space:
        print("Impossible because space")
        return False
    
    frontier = [SearchState(frozenset(), len(presents))]
    visited = set()

    timeout = 0
    while frontier:
        timeout += 1
        print(timeout)

        if timeout > 1_000:
            print("Timeout")
            return False

        state = frontier.pop()

        if state in visited:
            continue

        visited.add(state)

        if state.remaining_presents == 0:
            print("Possible")
            return True

        # space_needed = sum(shape.size() for shape in presents[:state.remaining_presents])
        # space_left = total_space - len(state.occupied)
        # if space_left < space_needed:
        #     print("no space")
        #     continue

        shape = presents[state.remaining_presents - 1]
        for r in range(4):
            for x in range(region.width - shape.width() + 1):
                for y in range(region.height - shape.height() + 1):
                    if state.can_fit_shape_at(x, y, shape):
                        frontier.append(SearchState(state.put_shape_at(x, y, shape), state.remaining_presents - 1))
                        frontier.append(SearchState(state.occupied, state.remaining_presents - 1))
                        # print("add at", x, y)

            shape = shape.rotated()
    
    print("Confirmed impossible")
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
    for region in regions:
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

    print(f"Part 1: {part1(input)}")
    # print(f"Part 2: {part2(input)}")
# 