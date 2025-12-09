
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

NEITHER_GREEN_NOR_RED = 0
GREEN = 1

def part2(input: str):
    red_tiles = [tuple(int(x) for x in line.split(",")) for line in input.splitlines()]

    minx = min(x for x, y in red_tiles) - 1
    maxx = max(x for x, y in red_tiles) + 1
    miny = min(y for x, y in red_tiles) - 1
    maxy = max(y for x, y in red_tiles) + 1
    
    print("Finding green borders...")

    grid: dict[tuple[int, int], int] = {}
    for i, (x1, y1) in enumerate(red_tiles):
        x2, y2 = red_tiles[(i+1) % len(red_tiles)]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1, y] = GREEN
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[x, y1] = GREEN


    print((maxx - minx) * (maxy - miny))
    print("Flood-filling neither green nor red tiles...")
    fill_queue = [(minx, miny)]
    while fill_queue:
        x, y = fill_queue.pop()
        if x < minx or x > maxx or y < miny or y > maxy or (x, y) in grid:
            continue
        grid[(x, y)] = NEITHER_GREEN_NOR_RED
        fill_queue.append((x + 1, y))
        fill_queue.append((x - 1, y))
        fill_queue.append((x, y + 1))
        fill_queue.append((x, y - 1))

    # output = ""
    # for y in range(miny, maxy + 1):
    #     for x in range(minx - 1, maxx + 2):
    #         if grid.get((x, y)) == GREEN:
    #             if (x, y) in red_tiles:
    #                 output += "#"
    #             else:
    #                 output += "X"
    #         elif grid.get((x, y)) == NEITHER_GREEN_NOR_RED:
    #             output += "."
    #         else:
    #             output += " "
    #     output += "\n"
    
    # print(output)

    def is_rectangle_all_green_or_red(x1, y1, x2, y2):
        for y in range(y1, y2):
            for x in range(x1, x2):
                if grid.get((x, y)) == NEITHER_GREEN_NOR_RED:
                    return False
        return True

    print("Finding largest valid rectangle...")
    largest_area = 0
    for i, (ax, ay) in enumerate(red_tiles):
        for bx, by in red_tiles[i+1:]:
            x1, x2 = min(ax, bx), max(ax, bx) + 1
            y1, y2 = min(ay, by), max(ay, by) + 1
            area = (x2 - x1) * (y2 - y1)
            if area > largest_area and is_rectangle_all_green_or_red(x1, y1, x2, y2):
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
    # print(part2(example))

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
