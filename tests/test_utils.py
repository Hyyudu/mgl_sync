import pytest
from src.utils import trunc, group


@pytest.mark.parametrize("lst,items,result", [
    ((1, 2, 3, 4), 2, [(1, 2), (3, 4)]),
    ([1, 2, 3, 4, 5, 6, 7], 3, [[1, 2, 3], [4, 5, 6], [7]]),
    ((), 5, []),
])
def test_group(lst, items, result):
    assert group(lst, items) == result


@pytest.mark.parametrize("inp,out", [
    (12345.67, 12300),
    (1234.567, 1230),
    (123.456, 123),
    (12.345, 12.3),
    (1.2345, 1.23),
    (0.12345, 0.123),
    (0.001234, 0.00123),
    (-12345.67, -12300),
    (-1234.567, -1230),
    (-123.456, -123),
    (-12.345, -12.3),
    (-1.2345, -1.23),
    (-0.12345, -0.123),
    (-0.001234, -0.00123),
])
def test_trunc(inp, out):
    assert trunc(inp) == out
