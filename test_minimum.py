from calculator.minimum import minimum


def test_minimum():
    assert minimum(4, 5) == 4
    assert minimum(3, 1) == 1