
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import init_db, get_all_games, get_game_by_id, create_game

app = FastAPI(
    title="Baseball Game API",
    description="プロ野球の試合情報を取得するAPI",
    version="1.0.0",
)

class GameCreate(BaseModel):
    date: str
    home_team: str
    away_team: str
    home_score: int | None = None
    away_score: int | None = None
    status: str = "scheduled"

# アプリ起動時にデータベースを準備する
init_db()


@app.get("/")
def home():
    return {"message": "Baseball Game API is running!"}


@app.get("/games")
def get_games(team: str | None = None, date: str | None = None):
    games = get_all_games(team=team, date=date)
    return {"count": len(games), "games": games}


@app.get("/games/{game_id}")
def get_game(game_id: int):
    game = get_game_by_id(game_id)

    if game is None:
        raise HTTPException(
            status_code=404,
            detail="Game not found"
        )

    return game
@app.post("/games", status_code=201)
def create_new_game(game: GameCreate):
    return create_game(game.model_dump())

    