import pytest


@pytest.mark.ui
def test_ui_passing():
    assert 3 == 3


def test_ui_failing():
    assert 3 == 5, 'ui test failed'
