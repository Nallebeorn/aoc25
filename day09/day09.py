from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

@dataclass
class VerticalEdge:
    x: int
    y1: int
    y2: int

    def __init__(self, x, y1, y2):
        self.x = x
        self.y1 = min(y1, y2)
        self.y2 = max(y1, y2)

    def length(self):
        return self.y2 - self.y1 + 1

@dataclass
class HorizontalEdge:
    y: int
    x1: int
    x2: int

    def __init__(self, y, x1, x2):
        self.y = y
        self.x1 = min(x1, x2)
        self.x2 = max(x1, x2)

    def length(self):
        return self.x2 - self.x1 + 1

def intersect(hor: HorizontalEdge, ver: VerticalEdge):
    return hor.x1 < ver.x and hor.x2 > ver.x and hor.y > ver.y1 and hor.y < ver.y2

def point_in_polygon(point: Point, vertical_edges: list[VerticalEdge]):
    hit_count = 0
    for edge in vertical_edges:
        if point.x > edge.x and point.y > edge.y1 and point.y < edge.y2:
            hit_count += 1
    
    return hit_count % 2 == 1

def any_intersect(horizontal_edges: list[HorizontalEdge], vertical_edges: list[VerticalEdge]):
    for hor in horizontal_edges:
        for ver in vertical_edges:
            if intersect(hor, ver):
                return True
    return False

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

    horizontal_edges: list[HorizontalEdge] = []
    vertical_edges: list[VerticalEdge] = []
    for i, a in enumerate(red_tiles):
        b = red_tiles[(i+1) % len(red_tiles)]
        if a.y == b.y:
            horizontal_edges.append(HorizontalEdge(a.y, a.x, b.x))
        if a.x == b.x:
            vertical_edges.append(VerticalEdge(a.x, a.y, b.y))
    
    assert len(horizontal_edges) == len(vertical_edges)
        
    largest_area = 0
    for i, a in enumerate(red_tiles):
        for j, b in enumerate(red_tiles[i+1:]):
            top_edge = HorizontalEdge(min(a.y, b.y), a.x, b.x)
            bottom_edge = HorizontalEdge(max(a.y, b.y), a.x, b.x)
            left_edge = VerticalEdge(min(a.x, b.x), a.y, b.y)
            right_edge = VerticalEdge(max(a.x, b.x), a.y, b.y)

            area = top_edge.length() * right_edge.length()

            if area > largest_area:
                mid_point = Point((top_edge.x1 + top_edge.x2) // 2, (right_edge.y1 + right_edge.y2) // 2)
                # if area > 33:
                #     print(area, Point(left_edge.x, top_edge.y), Point(right_edge.x, bottom_edge.y),
                #           not any_intersect([top_edge, bottom_edge], vertical_edges),
                #           not any_intersect(horizontal_edges, [left_edge, right_edge]),
                #           point_in_polygon(mid_point, vertical_edges)
                #         )

                if (
                    not any_intersect([top_edge, bottom_edge], vertical_edges)
                    and not any_intersect(horizontal_edges, [left_edge, right_edge])
                    and point_in_polygon(Point(left_edge.x + 1, top_edge.y + 1), vertical_edges)
                    and point_in_polygon(Point(right_edge.x - 1, top_edge.y + 1), vertical_edges)
                    and point_in_polygon(Point(left_edge.x + 1, bottom_edge.y - 1), vertical_edges)
                    and point_in_polygon(Point(right_edge.x - 1, bottom_edge.y - 1), vertical_edges)
                    and point_in_polygon(mid_point, vertical_edges)
                ):
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

    example2 = """\
1,1
3,1
3,9
11,9
11,1
13,1
13,11
1,11
"""

    example3 = """\
1,1
3,1
3,9
11,9
11,1
13,1
13,11
1,11
"""

    with open("input.txt", "r") as f:
        input = f.read()
        
    # print(part1(example))
    print(part2(example))
    print(part2(example2))

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")


# 2128582144 - too high
# 2375130720 - presumably also too high 
# 1924954374 - 
# 631669768 -
# 1644094530 - correct