from test import add
import pytest

def add_test():
    assert add(1,2) == 3

@pytest.mark.parametrize(
    "a, b, expected",
    [(2, 3, 5,), (-1, 1, 0), (0, 0, 0,), (1.5, 2.5, 4)] )

def test_add(a, b, expected):
    assert add(a, b) == expected
