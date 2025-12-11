from dataclasses import dataclass

def part1(input: str):
    device_mapping = {k: tuple(v.split()) for k, v in [line.split(":") for line in input.splitlines()]}

    paths_out = []
    frontier = [["you"]]

    while frontier:
        path = frontier.pop()
        device = path[-1]

        if device == "out":
            paths_out.append(path)
            continue
        
        for output in device_mapping[device]:
            frontier.append(path + [output])

    # print(paths_out)
    return len(paths_out)

@dataclass
class Path:
    devices: list[str]
    has_dac: bool = False
    has_fft: bool = False

    def concat(self, device: str):
        return Path(self.devices + [device], self.has_dac, self.has_fft)

def find_paths(start: str, end: str, mapping, exclude: set[str] = set()):
    # print("find", start, end)
    path_count_from: dict[str, int] = {k: 0 for k in mapping.keys()}
    frontier = [[start]]

    while frontier:
        path = frontier.pop()
        device = path[-1]

        if device in exclude:
            continue
            
        if device == end:
            for p in path[:-1]:
                path_count_from[p] += 1
            continue

        if device in path_count_from and path_count_from[device]:
            for p in path[:-1]:
                path_count_from[p] += path_count_from[device]
            continue

        if device not in mapping:
            continue
        
        for output in mapping[device]:
            frontier.append(path + [output])
    
    # print("path_count", path_count_from[start])

    return path_count_from[start], set(k for k, v in path_count_from.items() if v > 0)

def part2(input: str):
    device_mapping = {k: tuple(v.split()) for k, v in [line.split(":") for line in input.splitlines()]}

    dac_to_fft, reachable_from_dac = find_paths("dac", "fft", device_mapping)
    fft_to_dac, reachabled_from_fft = find_paths("fft", "dac", device_mapping)
    assert (dac_to_fft > 0 and fft_to_dac == 0) or (dac_to_fft == 0 and fft_to_dac > 0)

    first = "dac" if dac_to_fft > 0  else "fft"
    second = "fft" if dac_to_fft > 0 else "dac"

    exclude = reachable_from_dac.union(reachabled_from_fft)
    exclude.remove(first)

    start_to_first, _ = find_paths("svr", first, device_mapping, exclude)
    second_to_out, _ = find_paths(second, "out", device_mapping)

    return start_to_first * max(dac_to_fft, fft_to_dac) * second_to_out

if __name__ == "__main__":
    example = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

    example2 = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

    with open("input.txt", "r") as f:
        input = f.read()
        
    # print(part1(example))
    # print(part2(example2))

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
# 