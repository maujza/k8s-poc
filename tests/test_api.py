from datetime import datetime, timedelta, timezone

from fastapi.testclient import TestClient
from pydantic.error_wrappers import ValidationError
from simple_app.app.main import app
from simple_app.app.models.encrypt_model import EncryptResponseModel

post_body = {"payload": "do_the_thing"}

client = TestClient(app)


def send_request_to_endpoint():
    return client.post("/encrypt_payload", json=post_body)


def test_response_model(addingjsondata):
    response = send_request_to_endpoint()
    try:
        EncryptResponseModel.parse_obj(response.json())
    except ValidationError as e:
        print(f"Unexpected schema in response: {e}")


def test_datetime(addingjsondata):
    response = send_request_to_endpoint()
    response_body = response.json()
    timestamp = response_body["thing"]["current_time"]
    current_time_utc = datetime.now(timezone.utc)
    parsed_response_timestamp = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ").replace(
        tzinfo=timezone.utc
    )
    five_seconds_before_current_time = current_time_utc - timedelta(seconds=5)
    assert five_seconds_before_current_time <= parsed_response_timestamp <= current_time_utc


def test_encrypt_payload(addingjsondata):
    response = send_request_to_endpoint()
    assert response.status_code == 200
