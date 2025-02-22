from src.api import HeadHunterAPI
from unittest.mock import patch


@patch("requests.get")
def test_api_requests(test_requests_api):

    api = HeadHunterAPI()
    assert type(api) is HeadHunterAPI
