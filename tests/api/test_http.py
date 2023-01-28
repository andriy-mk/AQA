import pytest
import requests


@pytest.mark.http
def test_frist_check():
    request = requests.get("https://api.github.com/zen")
    print(f"Response is {request.text}")


@pytest.mark.http
def test_second_request():
    request = requests.get("https://api.github.com/users/defunkt")
    body = request.json()
    headers = request.headers

    assert body["name"] == "Chris Wanstrath"
    assert request.status_code == 200
    assert headers["Server"] == "GitHub.com"


@pytest.mark.http
def test_status_code_request():
    request = requests.get("https://api.github.com/users/sergii_butenko")
    assert request.status_code == 404
