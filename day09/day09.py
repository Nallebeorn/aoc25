from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

class Line(NamedTuple):
    start: Point
    end: Point

    def minx(self):
        return min(self.start.x, self.end.x)
    
    def maxx(self):
        return max(self.start.x, self.end.x)
    
    def miny(self):
        return min(self.start.y, self.end.y)
    
    def maxy(self):
        return max(self.start.y, self.end.y)

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
    red_tiles = [Point(*(int(x) for x in line.split(","))) for line in input.splitlines()]
    print(red_tiles)

    minx = min(x for x, y in red_tiles) - 1
    maxx = max(x for x, y in red_tiles) + 1
    miny = min(y for x, y in red_tiles) - 1
    maxy = max(y for x, y in red_tiles) + 1
    
    edges: list[Line] = []
    for i, a in enumerate(red_tiles):
        b = red_tiles[(i+1) % len(red_tiles)]
        edges.append(Line(min(a, b), max(a, b)))

    def lines_intersect(a: Line, b: Line):
        return (
            a.minx() > b.minx() and
            a.maxx() < b.maxx() and
            a.miny() < b.miny() and
            a.maxy() > b.maxy()
        ) or (
            a.minx() < b.minx() and
            a.maxx() > b.maxx() and
            a.miny() > b.miny() and
            a.maxy() < b.maxy()
        )
    
    def any_lines_intersect(list1: list[Line], list2: list[Line]):
        for a in list1:
            for b in list2:
                if lines_intersect(a, b):
                    print("Intersection!")
                    return True
        return False
    
    print(lines_intersect(
        Line(Point(-2, 0), Point(2, 0)),
        Line(Point(0, -2), Point(0, 2))
    ))

    # output = ""
    # for y in range(miny, maxy + 1):
    #     for x in range(minx, maxx + 1):
    #         # if (x, y) in vertical_edges or (x, y) in horizontal_edges:
    #         #     if (x, y) in red_tiles:
    #         #         output += "#"
    #         #     else:
    #         #         output += "X"
    #         # elif is_point_in_green(x, y):
    #         #     output += " "
    #         if is_point_in_green(x, y):
    #             output += "#"
    #         else:
    #             output += "."
    #     output += "\n"
    
    # print(output)

    print("Finding largest valid rectangle...")
    largest_area = 0
    for i, a in enumerate(red_tiles):
        for b in red_tiles[i+1:]:
            area = (abs(b.x - a.x) + 1) * (abs(b.y - a.y) + 1)
            if area > largest_area:
                rect_edges = [
                    Line(Point(a.x, a.y), Point(b.x, a.y)),
                    Line(Point(b.x, a.y), Point(b.x, b.y)),
                    Line(Point(b.x, b.y), Point(a.x, b.y)),
                    Line(Point(a.x, b.y), Point(a.x, a.y)),
                ]
                if not any_lines_intersect(rect_edges, edges):
                    largest_area = area

    return largest_area


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
        
    # print(part1(example))
    print(part2(example))

    # print(f"Part 1: {part1(input)}")
    # print(f"Part 2: {part2(input)}")
