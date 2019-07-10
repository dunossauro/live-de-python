from unittest import mock

import aiohttp
import pytest
import requests
from vcr import VCR

from ex1 import get

vcr = VCR(
    cassette_library_dir="resources/cassettes",
    path_transformer=VCR.ensure_suffix(".yaml"),
    record_mode="once",
    filter_headers=["authorization"],
)


@vcr.use_cassette
def test_get():
    response = get("https://httpbin.org/status/302")

    assert response.status_code == 200
    assert len(response.history) == 2


@vcr.use_cassette
@pytest.mark.asyncio  # pytest-asyncio
async def test_get_async():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbin.org/status/302") as response:
            assert response.status == 200


@vcr.use_cassette
def test_get_auth():
    response = get(
        "https://httpbin.org/anything",
        params={
            "param1": "value1",
            "param2": "value2",
        },
        headers={
            "Authorization": "Token imatoken",
            "Content-Type": "application/json",
        },
    )

    assert response.status_code == 200


@vcr.use_cassette
def test_patch_auth():
    response = requests.patch(
        "https://httpbin.org/anything",
        {"field1": "foo", "field2": "bar"},
        auth=("user", "pass"),
        params={
            "param1": "value1",
            "param2": "value2",
        },
    )

    assert response.status_code == 200


@mock.patch("ex1.requests.get")
def test_get_using_mock(get_mock):
    get_mock.return_value = mock.Mock(status_code=200, history=(mock.Mock(), mock.Mock()))

    response = get("https://httpbin.org/status/302")

    get_mock.assert_called_with("https://httpbin.org/status/302")
    assert response.status_code == 200
    assert len(response.history) == 2
