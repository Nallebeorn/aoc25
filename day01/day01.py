def part1(input: str):
    signs = {'L': -1, 'R': 1}
    
    password = 0
    dial = 50

    for delta in [signs[line[0]] * int(line[1:]) for line in input.splitlines()]:
        dial = (dial + delta) % 100
        if dial == 0:
            password += 1

    return password


def part2(input: str):
    pass


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
        
    # print(part1(example))
    print(part1(input))
    # print(part2(input))
