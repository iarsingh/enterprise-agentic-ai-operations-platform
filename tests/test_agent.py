from fastapi.testclient import TestClient
from entaops.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'run ops loop', **{'payload': {}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["loop"][0] == "detect"
    refused = client.post("/agent/run", json={"goal": 'reboot prod'}).json()
    assert refused["refused"] is True
