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

def find_paths(start: str, end: str, mapping, exclude: set[str]):
    paths_found = []
    frontier = [[start]]

    while frontier:
        path = frontier.pop()
        device = path[-1]

        if device == end:
            paths_found.append(path)
            continue

        if device not in mapping:
            continue

        if device in exclude:
            continue
        
        for output in mapping[device]:
            frontier.append(path + [output])

    return paths_found

def part2(input: str):
    device_mapping = {k: tuple(v.split()) for k, v in [line.split(":") for line in input.splitlines()]}

    reverse_mapping = {}
    for whence, to_list in device_mapping.items():
        for to in to_list:
            if to not in reverse_mapping:
                reverse_mapping[to] = []
            reverse_mapping[to].append(whence)

    paths_out = find_paths("dac", "out", device_mapping, set())
    exclude_out = set(device for path in paths_out for device in path[1:])
    paths_in = find_paths("fft", "svr", reverse_mapping, set())
    exclude_in = set(device for path in paths_in for device in path[1:])
    paths_2 = find_paths("dac", "fft", reverse_mapping, exclude_out)


    print(len(paths_out), len(paths_in), len(paths_2))
    return len(paths_out)

    # paths_out = []
    # frontier = [Path(["svr"])]

    # while frontier:
    #     path = frontier.pop()
    #     device = path.devices[-1]

    #     match device:
    #         case "out":
    #             if path.has_dac and path.has_fft:
    #                 paths_out.append(path)
    #             continue
    #         case "dac":
    #             path.has_dac = True
    #         case "fft":
    #             path.has_fft = True
        
    #     for output in device_mapping[device]:
    #         frontier.append(path.concat(output))

    # print(paths_out)
    # print(valid_paths_out)
    return len(paths_out)

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
    print(part2(example2))

    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
# 