def get_joltage(bank: str):
    banki = [int(d) for d in bank]

    tens = 0
    left_limit = 0
    ones = 0

    for idx, digit in enumerate(banki[:-1]):
        if digit > tens:
            left_limit, tens = idx, digit

    ones = max(banki[left_limit+1:])
    
    # print(tens * 10 + ones)
    return tens * 10 + ones

def part1(input: str):
    return sum([get_joltage(line) for line in input.splitlines()])

def get_unsafe_joltage(bank: str, num_batteries: int):
    joltage = ""
    left_limit = 0

    for i in range(num_batteries):
        end_limit = len(bank) - num_batteries + i + 1
        highest = 0
        for i in range(left_limit, end_limit):
            digit = int(bank[i])
            if digit > highest:
                left_limit, highest = i + 1, digit
        joltage += str(highest)
    
    # print(joltage)
    return int(joltage) if joltage else 0

def part2(input: str):
    return sum([get_unsafe_joltage(line, 12) for line in input.splitlines()])


if __name__ == "__main__":
    example = """\
987654321111111
811111111111119
234234234234278
818181911112111"""

    with open("input.txt", "r") as f:
        input = f.read()
        
    # print(part1(example))
    # print(part2(example))
    # print(part2("234234234234278"))
    # assert part2(example) == 3121910778619

    # print(extend_str_to_len("1", 5))
    # print(extend_str_to_len("12", 5))
    # print(extend_str_to_len("12", 6))
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
