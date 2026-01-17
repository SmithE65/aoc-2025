def apply_direction(input: str):
    direction = input[0]
    distance = int(input[1:])
    if direction == "L":
        return -distance
    return distance

def parse(input: str) -> int:
    return [
        apply_direction(line)
        for line in input.splitlines()
        if line
    ]

def run1(input: str) -> str:
    inputs = parse(input)
    start = 50
    zero_count = 0

    for distance in inputs:
        start += distance
        start %= 100

        if start == 0:
            zero_count += 1

    return str(zero_count)

def count_wraps(position, distance):
    new = position + distance
    neg = 1 if new <= 0 and position != 0 else 0
    return neg + (abs(new) // 100)

def left(position, distance):
    i = abs(distance)
    result = 0
    while i > 0:
        position = (position - 1) % 100
        if position == 0:
            result += 1
        i -= 1
    return result

def right(position, distance):
    i = abs(distance)
    result = 0
    while i > 0:
        position = (position + 1) % 100
        if position == 0:
            result += 1
        i -= 1
    return result

def run2(input: str) -> str:
    inputs = parse(input)
    position = 50
    zero_count = 0

    for distance in inputs:
        zero_count += count_wraps(position, distance)
        position = (position + distance) % 100

    return str(zero_count)