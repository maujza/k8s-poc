import os
import pytest
from requests import get

@pytest.fixture(scope="session")
def addingjsondata(request):
    URL = "https://raw.githubusercontent.com/iamcal/emoji-data/master/emoji.json"
    test_path = "./simple_app/app/utils/emoji.json"

    download_and_write_json(URL, test_path)
    
    request.addfinalizer(lambda: os.remove(test_path))


def download_and_write_json(url, path):
    response = get(url)
    with open(path, 'w') as file:
        file.write(response.text)
