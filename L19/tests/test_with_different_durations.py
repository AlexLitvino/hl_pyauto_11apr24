from time import sleep


def test_3s_1():
    sleep(3)
    assert 1 == 1


def test_3s_2():
    sleep(3)
    assert 1 == 1


def test_5s():
    sleep(5)
    assert 1 == 1


def test_1s_1():
    sleep(1)
    assert 1 == 1


def test_1s_2():
    sleep(1)
    assert 1 == 1
