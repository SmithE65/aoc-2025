import pytest
import day01

def test_sample_data_matches_provided_count():
    data = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
    result = day01.run1(data)
    assert "3" == result

def test_handles_trailing_newline():
    data = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82\n"
    result = day01.run1(data)
    assert "3" == result

def test_run2_matches_provided_sample():
    data = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82\n"
    result = day01.run2(data)
    assert "6" == result

@pytest.mark.parametrize(
    "position, distance, expected",
    [
        (0, 100, 1),
        (0, -100, 1),
        (0, -1, 0),
        (0, 0, 0),
        (0, 200, 2),
        (0, 1, 0),
        (1, -1, 1),
        (-1, 1, 1),
        (50, -68, 1),
        (82, -30, 0),
        (52, 48, 1),
        (0, -5, 0),
        (95, 60, 1),
        (55, -55, 1),
        (99, -99, 1),
        (0, 14, 0),
        (14, -82, 1)
    ]
)
def test_count_wraps(position, distance, expected):
    result = day01.count_wraps(position, distance)
    assert expected == result