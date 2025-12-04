def get_grid(grid: list[list[int]], x: int, y: int):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return 0
    
    return grid[y][x]
    
adjacents = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

def part1(input: str):
    grid = [[1 if c == "@" else 0 for c in line] for line in input.splitlines()]
    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                neighbours = sum(get_grid(grid, x + dx, y + dy) for dx, dy in adjacents)
                # print([get_grid(grid, x + dx, y + dy) for dx, dy in adjacents])
                if neighbours < 4:
                    result += 1
                    # print(x, y)

    # print(result)
    return result

def part2(input: str):
    grid = [[1 if c == "@" else 0 for c in line] for line in input.splitlines()]
    result = 0
    while True:
        local_result = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    neighbours = sum(get_grid(grid, x + dx, y + dy) for dx, dy in adjacents)
                    # print([get_grid(grid, x + dx, y + dy) for dx, dy in adjacents])
                    if neighbours < 4:
                        local_result += 1
                        grid[y][x] = 0
                        # print(x, y)
        result += local_result
        if local_result == 0:
            break

    # print(result)
    return result


if __name__ == "__main__":
    example = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    with open("input.txt", "r") as f:
        input = f.read()
        
    # print(part1(example))
    # print(part2(example))

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
