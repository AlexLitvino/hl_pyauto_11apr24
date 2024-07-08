import pytest


@pytest.mark.custom_marker
def test_some_test_pass():
    assert True


def test_some_test_fail():
    assert False


@pytest.mark.skip(reason="For some reason")
def test_some_test_skipped():
    assert False


@pytest.fixture()
def fixture_with_exception():
    raise Exception


def test_with_exception_in_fixture(fixture_with_exception):
    assert True
