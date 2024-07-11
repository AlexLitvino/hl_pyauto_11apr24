# HTTPClient
import pytest


class API:

    SUCESSFUL_HEADERS = {}
    INVALID_HEADERS = {}

    def get_all_users(self, headers=SUCESSFUL_HEADERS):
        pass


@pytest.mark.parametrize(api, [API0, API1, API2])
def test_get_users(api):

    assert api.get_all_users() > 0

