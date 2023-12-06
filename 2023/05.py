lines = open("input/05.txt").read().splitlines()

# parse input
seeds = [int(num) for num in lines[0].split(":")[1].split()]
maps = {}
for line in lines[1:]:
    if len(line) == 0:
        continue
    elif ":" in line:
        src_cat, dst_cat = line.split()[0].split("-to-")
        maps[src_cat] = [dst_cat]
    else:
        maps[src_cat].append([int(num) for num in line.split()])


class Range:
    def __init__(self, start=None, length=None):
        if start is None and length is None:
            self.range = []
        else:
            self.range = [[start, start + length - 1]]

    def __contains__(self, item):
        for r in self.range:
            if r[0] <= item <= r[1]:
                return True
        return False

    def __len__(self):
        return sum(r[1] - r[0] + 1 for r in self.range)

    def append(self, other):
        if isinstance(other, Range):
            self.range.extend(other.range)
        else:
            self.range.append(other)

    def intersection(self, other):
        new = Range()
        for a in self.range:
            for b in other.range:
                if b[0] <= a[0] <= b[1] or a[0] <= b[0] <= a[1]:
                    new.append([max(b[0], a[0]), min(b[1], a[1])])
        return new

    def difference(self, other):
        new = self
        for b in other.range:
            _new = Range()
            for a in new.range:
                if a[1] < b[0] or b[1] < a[0]:
                    _new.append(a)
                elif b[0] <= a[0] and b[1] < a[1]:
                    _new.append([b[1] + 1, a[1]])
                elif a[0] < b[0] and b[1] < a[1]:
                    _new.append([a[0], b[0] - 1])
                    _new.append([b[1] + 1, a[1]])
                elif a[0] < b[0] and a[1] <= b[1]:
                    _new.append([a[0], b[0] - 1])
            new = _new
        return new

    def min(self):
        return min(r[0] for r in self.range)


def map_src_to_dst(src_val, src_cat, dst_cat):
    for map in maps[src_cat][1:]:
        if src_val in Range(map[1], map[2]):
            dst_val = src_val + (map[0] - map[1])
            break
    else:
        dst_val = src_val
    if maps[src_cat][0] != dst_cat:
        return map_src_to_dst(dst_val, maps[src_cat][0], dst_cat)
    return dst_val


def map_src_range_to_dst_range(src_range, src_cat, dst_cat):
    dst_range = Range()
    inter_range = Range()
    for map in maps[src_cat][1:]:
        inter = src_range.intersection(Range(map[1], map[2]))
        if len(inter) > 0:
            dst_range.append(Range(inter.range[0][0] + (map[0] - map[1]), len(inter)))
            inter_range.append(inter)
    dst_range.append(src_range.difference(inter_range))
    if maps[src_cat][0] != dst_cat:
        return map_src_range_to_dst_range(dst_range, maps[src_cat][0], dst_cat)
    return dst_range


# part one
print(min(map_src_to_dst(seed, "seed", "location") for seed in seeds))

# part two
print(
    min(
        map_src_range_to_dst_range(Range(a, b), "seed", "location").min()
        for a, b in zip(seeds[::2], seeds[1::2])
    )
)
