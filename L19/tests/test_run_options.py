def test_1_pass():
    assert 1 == 1


def test_2_fail():
    assert 1 == 2


def test_3_pass():
    assert 1 == 1


def test_4_fail():
    assert 1 == 2


def test_5_fail():
    assert 1 == 2


def test_6_pass():
    assert 1 == 1

def add(a, b):
    return a + b


def test_add():
    op1 = 3
    op2 = 4
    observed = add(op1, op2)
    assert observed == 9, f"Expected to get 9, but got {observed}"