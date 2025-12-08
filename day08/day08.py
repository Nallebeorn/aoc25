from math import prod

def part1(input: str, pairs_count: int):
    boxes = [tuple(int(x) for x in line.split(",")) for line in input.splitlines()]

    distanced_pairs = []
    for i, boxa in enumerate(boxes):
        for boxb in boxes[i+1:]:
            ax, ay, az = boxa
            bx, by, bz = boxb
            dx, dy, dz = bx - ax, by - ay, bz - az
            distanced_pairs.append((dx * dx + dy * dy + dz * dz, boxa, boxb))
    
    distanced_pairs.sort()

    box_circuit = {}
    circuit_lengths = []

    for box in boxes:
        box_circuit[box] = len(circuit_lengths)
        circuit_lengths.append(1)

    for dist, a, b in distanced_pairs[:pairs_count]:
        if box_circuit[a] != box_circuit[b]:                
            circuit_lengths[box_circuit[a]] += circuit_lengths[box_circuit[b]]
            circuit_lengths[box_circuit[b]] = 0
            for k, v in box_circuit.items():
                if v == box_circuit[b]:
                    box_circuit[k] = box_circuit[a]
        # print(a, b, circuit_lengths)

    circuit_lengths = [cl for cl in circuit_lengths if cl != 0]
    circuit_lengths.sort(reverse=True)
    assert sum(circuit_lengths) == len(boxes)
    return prod(circuit_lengths[:3])

def part2(input: str):
    ...


if __name__ == "__main__":
    example = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

    with open("input.txt", "r") as f:
        input = f.read()
        
    print(part1(example, 10))
    # print(part2(example))

    print(f"Part 1: {part1(input, 1000)}")
    # print(f"Part 2: {part2(input)}")
