from calculator.reminder import reminder


def test_reminder():
    assert reminder(6, 3) == 0
    assert reminder(4, 3) == 1