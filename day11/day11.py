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

    path_count_from: dict[str, int] = {k: 0 for k in mapping.keys()}

    i = 0
    while frontier:
        path = frontier.pop()
        device = path[-1]
        i += 1
            
        if device == end:
            paths_found.append(path)
            for p in path[:-1]:
                path_count_from[p] += 1
            continue

        if path_count_from[device]:
            for p in path[:-1]:
                path_count_from[p] += path_count_from[device]
            continue

        if device not in mapping:
            continue

        # if device in exclude:
        #     continue
        
        for output in mapping[device]:
            frontier.append(path + [output])
    
    print("iterations", i)
    print("path_count", path_count_from[start])

    return path_count_from[start]

def part2(input: str):
    device_mapping = {k: tuple(v.split()) for k, v in [line.split(":") for line in input.splitlines()]}

    reverse_mapping = {}
    for whence, to_list in device_mapping.items():
        for to in to_list:
            if to not in reverse_mapping:
                reverse_mapping[to] = []
            reverse_mapping[to].append(whence)

    path_count = find_paths("svr", "out", device_mapping, set())

    return path_count

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