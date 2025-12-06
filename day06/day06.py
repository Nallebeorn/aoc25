from math import prod

def part1(input: str):
    lines = input.splitlines()
    numbers = [[int(n) for n in line.split()] for line in lines[:-1]]
    operators = lines[-1].split()

    result = 0
    for i, op in enumerate(operators):
        args = [row[i] for row in numbers]
        match op:
            case "+":
                result += sum(args)
            case "*":
                result += prod(args)
            case _:
                raise
        # print(i, op, args)
    
    return result

def part2(input: str):
    lines = [line + " " for line in input.splitlines()]
    numbers = []
    left_limit = 0
    for i in range(len(lines[0])):
        if all(line[i] == " " for line in lines):
            nums = []
            for j in range(left_limit, i):
                n = ""
                for row in range(len(lines) - 1):
                    n += lines[row][j]
                nums.append(int(n))
            left_limit = i + 1
            numbers.append(nums)

    # print(numbers)
        
    operators = lines[-1].split()

    result = 0
    for i, op in enumerate(operators):
        args = numbers[i]
        match op:
            case "+":
                result += sum(args)
            case "*":
                result += prod(args)
            case _:
                raise
        # print(i, op, args)
    
    return result


if __name__ == "__main__":
    example = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

    with open("input.txt", "r") as f:
        input = f.read()
        
    # print(part1(example))
    # print(part2(example))

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
