def part1(input: str):
    result = 0

    for start, end in [[int(x) for x in range.split("-")] for range in input.split(",")]:
        for i in range(start, end + 1):
            digits = str(i)
            mid = len(digits) // 2
            if digits[:mid] == digits[mid:]:
                result += i

    return result


def extend_str_to_len(string: str, length: int):
    mult = length / len(string)
    return string * int(mult) if mult > 1 and int(mult) == mult else None

def part2(input: str):
    result = 0

    for start, end in [[int(x) for x in range.split("-")] for range in input.split(",")]:
        # print(f"Range: {start}, {end}")
        for i in range(start, end + 1):
            digits = str(i)
            for j in range(1, len(digits) + 1):
                if extend_str_to_len(digits[:j], len(digits)) == digits:
                    # print(extend_str_to_len(digits[:j], len(digits)))
                    # print("Invalid id: " + digits)
                    result += i
                    break
        # print("")

    return result


if __name__ == "__main__":
    example = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

    with open("input.txt", "r") as f:
        input = f.read()
        
    # print(part1(example))
    # print(part2(example))

    # print(extend_str_to_len("1", 5))
    # print(extend_str_to_len("12", 5))
    # print(extend_str_to_len("12", 6))
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
