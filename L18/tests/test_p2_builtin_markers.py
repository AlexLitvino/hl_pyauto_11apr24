import pytest


@pytest.mark.skip(reason="Not implemented yet")
def test_not_implemented():
    """
    Test Case
    """
    raise NotImplementedError

import platform

@pytest.mark.skipif(condition=platform.uname().system != 'Linux', reason="This test related to Linux only")
def test_related_to_linux():
    assert 1 == 1

@pytest.mark.skipif(condition=platform.uname().system != 'windows', reason="This test related to Windows only")
def test_related_to_windows():
    assert 1 == 1

@pytest.mark.xfail(reason='JIRA-123')
def test_failing():
    assert 2 == 2