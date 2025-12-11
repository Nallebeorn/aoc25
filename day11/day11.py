def part1(input: str):
    device_mapping = {k: tuple(v.split()) for k, v in [line.split(":") for line in input.splitlines()]}

    paths_out = []
    frontier = [["you"]]

    while frontier:
        path = frontier.pop()
        device = path[-1]

        if device == "out":
            paths_out.append(path)
            continue
        
        for output in device_mapping[device]:
            frontier.append(path + [output])

    # print(paths_out)
    return len(paths_out)


def part2(input: str):
    ...

if __name__ == "__main__":
    example = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

    with open("input.txt", "r") as f:
        input = f.read()
        
    print(part1(example))
    print(part2(example))

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
# 