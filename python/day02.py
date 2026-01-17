

def parse(input: str) -> list[tuple[str, str]]:
    ranges = [
        (l, h)
        for l, h in (r.strip().split("-") for r in input.split(","))
    ]
    
    return ranges

# 1-9876 becomes:
# 1-9
# 10-99
# 100-999
# 1000-9876
def expand_ranges(ranges: list[tuple[str, str]]) -> list[tuple[str, str]]:
    result = []

    for l, h in ranges:
        l_len = len(l)
        h_len = len(h)
        if l_len == h_len:
            result.append((l, h))
        else:
            temp_h = "".join(["9" for _ in range(l_len)])
            result.append((l, temp_h))

            for i in range(l_len + 1, h_len):
                temp_l = "1" + "".join(["0" for _ in range(i - 1)])
                temp_h = "".join(["9" for _ in range(i)])
                result.append((temp_l, temp_h))

            temp_l = "1" + "".join(["0" for _ in range(h_len - 1)])
            result.append((temp_l, h))
    
    return result
                
def get_invalid_ids(range: tuple[str, str], size: int) -> list[int]:
    ids = []
    l, h = range

    if len(l) % size != 0:
        return []

    value = l[:len(l)//size]
    stop = int(h)
    start = int(value + value)

    while start < int(l):
        value = str(int(value) + 1)
        start = int(value + value)

    while start <= stop:
        ids.append(start)
        value = str(int(value) + 1)
        start = int(value + value)

    return ids
                
def get_invalid_ids2(ranges: list[tuple[str, str]]) -> list[int]:
    ids = []

    for l, h in [r for r in ranges if len(r[0]) % 2 == 0]:
        value = l[:len(l)//2]
        stop = int(h)
        start = int(value + value)

        while start < int(l):
            value = str(int(value) + 1)
            start = int(value + value)

        while start <= stop:
            ids.append(start)
            value = str(int(value) + 1)
            start = int(value + value)

    return ids

def run1(input: str) -> str:
    ranges = parse(input)
    ranges = expand_ranges(ranges)
    ids = get_invalid_ids(ranges)
    count = sum(set(ids))
    return str(count)

def run2(input: str) -> str:
    ranges = parse(input)
    ranges = expand_ranges(ranges)
    ids = get_invalid_ids2(ranges)
    count = sum(set(ids))
    return str(count)
