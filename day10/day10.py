from dataclasses import dataclass
from collections import deque

@dataclass
class Machine:
    lights: tuple[bool, ...]
    buttons: list[tuple[int, ...]]

@dataclass
class State:
    lights: tuple[bool, ...]
    presses: int

def parse_lights(string: str):
    return tuple(c == "#" for c in string.strip("[]"))

def parse_buttons(buttons: list[str]):
    return [tuple(int(x) for x in b.strip("()").split(",")) for b in buttons if b.startswith("(")]

def toggle(lights: tuple[bool, ...], button: tuple[int, ...]):
    result = tuple(not light if i in button else light for i, light in enumerate(lights))
    # print(lights, result)
    return result

def solve_machine(machine: Machine):
    queue = deque[State]()
    queue.append(State(tuple(False for _ in machine.lights), 0))

    best_for_state = {}

    while queue:
        state = queue.popleft()

        if state.lights in best_for_state and state.presses >= best_for_state[state.lights]:
            continue

        best_for_state[state.lights] = state.presses

        if state.lights == machine.lights:
            continue
            
        for button in machine.buttons:
            queue.append(State(toggle(state.lights, button), state.presses + 1))

    # print(best)
    assert machine.lights in best_for_state
    return best_for_state[machine.lights]

def part1(input: str):
    machines = []

    for line in input.splitlines():
        segments = line.split()
        machines.append(Machine(parse_lights(segments[0]), parse_buttons(segments[1:])))

    return sum(solve_machine(machine) for machine in machines)


def part2(input: str):
    ...


if __name__ == "__main__":
    example = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

    with open("input.txt", "r") as f:
        input = f.read()
        
    print(part1(example))
    # print(part2(example))

    print(f"Part 1: {part1(input)}")
    # print(f"Part 2: {part2(input)}")
