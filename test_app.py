import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200

def test_health(client):
    res = client.get("/health")
    assert res.json["healthy"] == True