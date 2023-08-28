""" Module used to call health check endpoint """
import requests


def test_health():
    resp = requests.get("http://localhost:5000/health", timeout=30)
    assert resp.status_code == 200
