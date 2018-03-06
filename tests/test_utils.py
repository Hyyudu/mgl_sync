from magellan import group


def test_group():
    assert group((1, 2, 3, 4), 2) == [(1, 2), (3, 4)]
    assert group([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]
