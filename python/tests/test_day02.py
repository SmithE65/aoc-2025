import day02


def test_sample_data_parses():
    input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    result = day02.parse(input)
    result = list(result)
    assert(11, len(result))

def test_expand_ranges():
    input = day02.parse("3-9876")
    result = day02.expand_ranges(input)
    assert(4, len(result))

    parsed = [
        (int(l), int(h))
        for l, h in result
    ]

    l, h = parsed[0]
    assert(l == 3)
    assert(h == 9)

    l, h = parsed[1]
    assert(l == 10)
    assert(h == 99)

    l, h = parsed[2]
    assert(l == 100)
    assert(h == 999)

    l, h = parsed[3]
    assert(l == 1000)
    assert(h == 9876)

def test_simple_run1():
    result = day02.run1("11-22,22-23")
    assert(33 == int(result))

def test_run1_sample_data():
    input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124\n"
    result = day02.run1(input)
    assert(1227775554 == int(result))
