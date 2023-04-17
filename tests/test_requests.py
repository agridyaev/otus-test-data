import pytest
import requests

from csv import DictReader
from csv import reader


def http_method(name: str):
    return requests.get if name.lower() == "get" else requests.post


test_data = DictReader(open("test_data.csv"))


@pytest.mark.parametrize('td', test_data)
def test_reader(td):
    url = td['url']
    method = td['method']
    status = int(td['status'])
    assert http_method(method)(url, allow_redirects=False).status_code == int(status)


reader = reader(open("test_data.csv"))
headers = next(reader)


@pytest.mark.parametrize(headers, reader)
def test_reader_v2(url, method, status):
    assert http_method(method)(url, allow_redirects=False).status_code == int(status)
