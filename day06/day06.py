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
    ...


if __name__ == "__main__":
    example = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

    with open("input.txt", "r") as f:
        input = f.read()
        
    print(part1(example))
    print(part2(example))

    print(f"Part 1: {part1(input)}")
    # print(f"Part 2: {part2(input)}")
