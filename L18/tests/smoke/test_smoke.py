import pytest

def test_smoke_passing():
    assert 3 == 3


def test_smoke_failing():
    assert 3 == 5, 'smoke test failed'

@pytest.mark.smoke
@pytest.mark.ui
def test_smoke_ui_test():
    assert 3 == 5, 'smoke ui failing'

@pytest.mark.api
def test_smoke_api_test():
    assert 3 == 5, 'smoke api failing'
