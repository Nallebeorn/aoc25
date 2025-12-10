
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
    red_tiles = [tuple(int(x) for x in line.split(",")) for line in input.splitlines()]

    minx = min(x for x, y in red_tiles) - 1
    maxx = max(x for x, y in red_tiles) + 1
    miny = min(y for x, y in red_tiles) - 1
    maxy = max(y for x, y in red_tiles) + 1
    
    edges = []
    for i, a in enumerate(red_tiles):
        b = red_tiles[(i+1) % len(red_tiles)]
        edges.append((min(a, b), max(a, b)))

    # print(edges)

    def is_point_in_green(px: int, py: int):
        intersections = 0
        intersections2 = 0
        intersections3 = 0
        intersections4 = 0
        for (ax, ay), (bx, by) in edges:
            if px > ax and px > bx and py >= ay and py < by:
                intersections += 1
            if px > ax and px > bx and py > ay and py <= by:
                intersections2 += 1
            if px >= ax and px >= bx and py >= ay and py < by:
                intersections3 += 1
            if px >= ax and px >= bx and py > ay and py <= by:
                intersections4 += 1
        
        return intersections % 2 == 1 or intersections2 % 2 == 1 or intersections3 % 2 == 1 or intersections4 % 2 == 1

    def is_rectangle_all_green(x1, y1, x2, y2):
        for y in range(y1, y2):
            for x in range(x1, x2):
                if not is_point_in_green(x, y):
                    return False
        return True

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
    for i, (ax, ay) in enumerate(red_tiles):
        for bx, by in red_tiles[i+1:]:
            x1, x2 = min(ax, bx), max(ax, bx) + 1
            y1, y2 = min(ay, by), max(ay, by) + 1
            area = (x2 - x1) * (y2 - y1)
            if area > largest_area and is_rectangle_all_green(x1, y1, x2, y2):
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

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
