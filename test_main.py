
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Baseball Game API is running!"
    }


def test_get_games():
    response = client.get("/games")

    assert response.status_code == 200

    data = response.json()
    assert "count" in data
    assert "games" in data
    assert data["count"] == len(data["games"])
    assert data["count"] >= 2


def test_get_existing_game():
    response = client.get("/games/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_missing_game():
    response = client.get("/games/999999")

    assert response.status_code == 404


def test_create_game():
    game = {
        "date": "2026-10-13",
        "home_team": "ソフトバンク",
        "away_team": "日本ハム",
        "home_score": None,
        "away_score": None,
        "status": "scheduled",
    }

    response = client.post("/games", json=game)

    assert response.status_code == 201
    assert response.json()["home_team"] == "ソフトバンク"


def test_search_games_by_team():
    response = client.get("/games?team=ソフトバンク")

    assert response.status_code == 200

    data = response.json()

    for game in data["games"]:
        assert (
            "ソフトバンク" in game["home_team"]
            or "ソフトバンク" in game["away_team"]
        )


def test_search_games_by_date():
    response = client.get("/games?date=2026-10-13")

    assert response.status_code == 200

    data = response.json()

    for game in data["games"]:
        assert game["date"] == "2026-10-13"
