from dataclasses import dataclass
from collections import deque
from sympy import Matrix, Rational, simplify

@dataclass
class LightMachine:
    lights: tuple[bool, ...]
    buttons: list[tuple[int, ...]]

@dataclass
class LightState:
    lights: tuple[bool, ...]
    presses: int

@dataclass
class JoltageMachine:
    joltages: list[int]
    buttons: list[tuple[int, ...],]

@dataclass
class JoltageState:
    joltage: list[int]
    presses: list[int]
    next_button: int

def parse_lights(string: str):
    return tuple(c == "#" for c in string.strip("[]"))

def parse_buttons(buttons: list[str]):
    return [tuple(int(x) for x in b.strip("()").split(",")) for b in buttons if b.startswith("(")]

def parse_joltages(string: str):
    return [int(x) for x in string.strip("{}").split(",")]

def toggle(lights: tuple[bool, ...], button: tuple[int, ...]):
    result = tuple(not light if i in button else light for i, light in enumerate(lights))
    # print(lights, result)
    return result

def increment(joltages: tuple[int, ...], button: tuple[int, ...]):
    result = tuple(jolt + 1 if i in button else jolt for i, jolt in enumerate(joltages))
    # print(joltages, result)
    return result

def press_button(presses: tuple[int, ...], button_index: int):
    return tuple(p + 1 if i == button_index else p for i, p in enumerate(presses))

def solve_machine_lights(machine: LightMachine):
    queue = deque[LightState]()
    queue.append(LightState(tuple(False for _ in machine.lights), 0))

    best_for_state = {}

    while queue:
        state = queue.popleft()

        if state.lights in best_for_state and state.presses >= best_for_state[state.lights]:
            continue

        best_for_state[state.lights] = state.presses

        if state.lights == machine.lights:
            continue
            
        for button in machine.buttons:
            queue.append(LightState(toggle(state.lights, button), state.presses + 1))

    assert machine.lights in best_for_state
    return best_for_state[machine.lights]

def is_joltage_exceeded(maximums: tuple[int, ...], joltages: tuple[int, ...]):
    for max, current in zip(maximums, joltages):
        if current > max:
            return True
    return False

def solve_machine_joltages(target_joltages: list[int], buttons: list[tuple[int, ...]]):
    best = None

    print("unsorted", buttons)
    buttons.sort(key = len, reverse = True)
    print("sorted", buttons)
    queue = deque[JoltageState]()
    queue.append(JoltageState([0 for _ in target_joltages], [0 for _ in buttons], 0))

    i = 0
    while queue:
        i += 1
        # print(i)
        state = queue.popleft()

        total_presses = sum(state.presses)

        # print(state)

        if best is not None and total_presses >= best:
            continue

        if target_joltages == state.joltage:
            if best is None or total_presses < best:
                best = total_presses
            continue

        if state.next_button >= len(buttons):
            continue

        button = buttons[state.next_button]
        remaining = [target_joltages[machine] - state.joltage[machine] for machine in button]

        for press_count in range(min(remaining) + 1):
            new_presses = list(state.presses)
            new_presses[state.next_button] += press_count

            new_joltage = list(state.joltage)
            for machine in button:
                new_joltage[machine] += press_count

            queue.append(JoltageState(new_joltage, new_presses, state.next_button + 1))

    print("iteration count", i)

    assert best is not None
    return best

def part1(input: str):
    machines = []

    for line in input.splitlines():
        segments = line.split()
        machines.append(LightMachine(parse_lights(segments[0]), parse_buttons(segments[1:])))

    return sum(solve_machine_lights(machine) for machine in machines)

def part2(input: str):
    machines: list[JoltageMachine] = []

    for line in input.splitlines():
        segments = line.split()
        machines.append(JoltageMachine(parse_joltages(segments[-1]), parse_buttons(segments[:-1])))

    # print(machines)

    m = Matrix([
        [0, 0, 0, 0, 1, 1, 3],
        [0, 1, 0, 0, 0, 1, 5],
        [0, 1, 1, 1, 0, 0, 4],
        [1, 1, 0, 1, 0, 0, 7]
    ])
    # print(m.rref(pivots=False).col(-1).values())

    result = 0
    for machine in machines:
        # print(machine)
        matrix = Matrix([
            [1 if i in button else 0 for button in machine.buttons] + [0, target_joltage]
            for i, target_joltage in enumerate(machine.joltages)
        ] + [
            [1 for _ in machine.buttons] + [-1, 0]
        ])

        # print(matrix)

        rref, pivots = matrix.rref(normalize_last=False)
        solutions = rref.col(-1).values()
        foo = [row[-1] * row[-2].q / row[-2].p for row in rref.values()]
        foo2 = [(row[-2], row[-1]) for row in rref.tolist()]
        # foo = max(-row[-1] for row in rref.tolist() if row[-2] != 0)
        # answer = 1
        # while not all(coefficient - sign * answer >= 0 for sign, coefficient in foo):
        # for answer in range(13):
        #     print(answer, [coefficient - sign * answer for sign, coefficient in foo2], sum([coefficient - sign * answer for sign, coefficient in foo2]))
        #     answer += 1

        print(foo)

        continue

        answer = min(foo) * -1
        # assert answer > 0
        # assert answer.q == 1
        print([f"{coefficient} + {-sign}x" for sign, coefficient in foo2])
        if (foo2[-1][0] == 1):
            answer = foo2[-1][1]
        assert answer >= 0
        # answer = answer.p * answer.q
        assert answer.q == 1
        # while sum(coefficient - sign * answer for sign, coefficient in foo2) != answer or not all(coefficient - sign * answer >= 0 for sign, coefficient in foo2):
        #     print(answer, [coefficient - sign * answer  for sign, coefficient in foo2], sum(coefficient - sign * answer for sign, coefficient in foo2))
        #     answer += 1
        # if answer <= 0:
        #     print(machine, foo)
        #     print([f"{coefficient} + {-sign}x" for sign, coefficient in foo2])
        # print(answer)
        result += answer
        # # print(matrix)
        # # print(sum(solutions) - min(solutions))
        # summed = sum(solutions) - min(solutions)
        # if summed.q != 1:
        #     print(machine)
        #     print(solutions, pivots, sum(solutions), sum(solutions) - min(solutions), summed)
        # # print(sum(solutions) - min(solutions), summed, summed.p * summed.q)
        # # result += sum(solutions) - min(solutions)
        # result += summed.p * summed.q
        # # print(sum(solutions))

    return result

if __name__ == "__main__":
    example = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

    with open("input.txt", "r") as f:
        input = f.read()
        
    # print(part1(example))
    print(part2(example))

    # print(f"Part 1: {part1(input)}")
    # print(f"Part 2: {part2(input)}")


# 52070 - too high
# 67271 - well fuck that can't be right then
# 104920 - lmao, no
# 104977 - well no