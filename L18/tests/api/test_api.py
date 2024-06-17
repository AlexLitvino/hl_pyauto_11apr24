import pytest

def test_api_passing():
    assert 3 == 3

@pytest.mark.api
def test_api_failing():
    assert 3 == 5, 'api test failed'
