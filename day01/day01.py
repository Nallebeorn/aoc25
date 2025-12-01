signs = {'L': -1, 'R': 1}

def part1(input: str):
    password = 0
    dial = 50

    for delta in [signs[line[0]] * int(line[1:]) for line in input.splitlines()]:
        dial = (dial + delta) % 100
        if dial == 0:
            password += 1

    return password


def part2(input: str):
    password = 0
    dial = 50

    for delta in [signs[line[0]] * int(line[1:]) for line in input.splitlines()]:
        dial = dial + delta
        wraps = abs(dial // 100)
        dial = dial % 100
        password += wraps

    return password


if __name__ == "__main__":
    example = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

    with open("input.txt", "r") as f:
        input = f.read()
        
    # print(part2(example))
    # print(part2("R1000"))
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
