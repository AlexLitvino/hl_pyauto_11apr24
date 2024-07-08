import pytest


@pytest.mark.custom_marker
def test_some_test_pass():
    assert True


def test_some_test_fail():
    assert False


@pytest.mark.skip(reason="For some reason")
def test_some_test_skipped():
    assert False
