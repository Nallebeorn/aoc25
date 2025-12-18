from dataclasses import dataclass
from collections import deque
import numpy as np
from scipy.optimize import linprog

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

    # print(m.rref(pivots=False).col(-1).values())

    result = 0
    for machine in machines:
        # print(machine)
        button_matrix = np.array([
            [1 if i in button else 0 for button in machine.buttons]
            for i in range(len(machine.joltages))
        ])

        joltages = np.array(machine.joltages)

        to_minimize = np.array([1 for _ in machine.buttons])

        res = linprog(to_minimize, A_eq=button_matrix, b_eq=joltages, bounds = (0, None), integrality=1)
        assert res.success
        assert int(res.fun) == res.fun
        answer = int(res.fun)

        # print(button_matrix, joltages, to_minimize)
        # print(answer)

        result += answer

    return result

if __name__ == "__main__":
    example = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

    with open("input.txt", "r") as f:
        input = f.read()
        
    # print(part1(example))
    # print(part2(example))

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")


# 52070 - too high
# 67271 - well fuck that can't be right then
# 104920 - lmao, no
# 104977 - well no