import time
import random


def delay(wait, deviation=0):
    """Performs sleep for wait +/- deviation seconds"""
    # TODO: use only one module with setting wait=0 for fast
    if wait == 0:
        return
    if deviation > wait:
        raise ValueError("deviation parameter should be less than wait parameter")
    if deviation:
        time_to_sleep = wait - deviation + 2 * deviation * random.random()
    else:
        time_to_sleep = wait
    time.sleep(time_to_sleep)


wait = 5
deviation = 1


def test_1():
    delay(wait, deviation)
    assert 1 == 1


def test_2():
    delay(wait, deviation)
    assert 1 == 1


def test_3():
    delay(wait, deviation)
    assert 1 == 1


def test_4():
    delay(wait, deviation)
    assert 1 == 1


def test_5():
    delay(wait, deviation)
    assert 1 == 1


def test_6():
    delay(wait, deviation)
    assert 1 == 1


def test_7():
    delay(wait, deviation)
    assert 1 == 1


def test_8():
    delay(wait, deviation)
    assert 1 == 1


def test_9():
    delay(wait, deviation)
    assert 1 == 1


def test_10():
    delay(wait, deviation)
    assert 1 == 1


def test_11():
    delay(wait, deviation)
    assert 1 == 1


def test_12():
    delay(wait, deviation)
    assert 1 == 1
