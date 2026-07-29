from fastapi.testclient import TestClient

from src.sentinel_api.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_approved_scenario_returns_guidance() -> None:
    response = client.post("/emergency-prompts", json={"scenario": "fire", "site_id": "site-1"})
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_off_topic_scenario_is_blocked() -> None:
    response = client.post("/emergency-prompts", json={"scenario": "weather", "site_id": "site-1"})
    assert response.json()["status"] == "blocked"
