from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

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

    def all_reds_are_on_our_outside_rect(rect_min: Point, rect_max: Point):
        if rect_min == Point(2, 3) and rect_max == Point(9, 5):
            print("hi")

        for red in red_tiles:
            if (
                (red.x >= rect_min.x and red.x <= rect_max.x) and
                (red.y >= rect_min.y and red.y <= rect_max.y) and
                (red != rect_min and red != rect_max)
            ):
                if rect_min == Point(2, 3) and rect_max == Point(9, 5):
                    print("huh", red)
                return False
        return True
        
    largest_area = 0
    for i, a in enumerate(red_tiles):
        for j, b in enumerate(red_tiles[i+1:]):
            rect_min = Point(min(a.x, b.x), min(a.y, b.y))
            rect_max = Point(max(a.x, b.x), max(a.y, b.y))
            area = (rect_max.x - rect_min.x + 1) * (rect_max.y - rect_min.y + 1)
            if area == 24:
                print("24", rect_min, rect_max)
            if area > largest_area and all_reds_are_on_our_outside_rect(rect_min, rect_max):
                if area == 40:
                    print("40", rect_min, rect_max)
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
    print(f"Part 2: {part2(input)}")
