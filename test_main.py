
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# 1. トップページが正常に動くか
def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Baseball Game API is running!"
    }


# 2. 試合一覧を正常に取得できるか
def test_get_games():
    response = client.get("/games")

    assert response.status_code == 200

    data = response.json()
    assert data["count"] == len(data["games"])
    assert data["count"] >= 2
    


# 3. 存在する試合を取得できるか
def test_get_existing_game():
    response = client.get("/games/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


# 4. 存在しない試合を取得したとき404になるか
def test_get_missing_game():
    response = client.get("/games/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Game not found"



def test_create_game():
    response = client.post(
        "/games",
        json={
            "date": "2026-10-14",
            "home_team": "テストホーム",
            "away_team": "テストビジター",
            "status": "scheduled",
        },
    )

    assert response.status_code == 201

    data = response.json()
    assert data["home_team"] == "テストホーム"
    assert data["away_team"] == "テストビジター"
    assert data["id"] is not None
