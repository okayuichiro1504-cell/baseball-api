
import sqlite3
from pathlib import Path

# database.pyと同じフォルダにDBファイルを作る
DB_PATH = Path(__file__).resolve().parent / "baseball.db"


def get_connection():
    """データベースへの接続を作成する"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """テーブルを作成し、サンプルデータを登録する"""
    conn = get_connection()

    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                home_team TEXT NOT NULL,
                away_team TEXT NOT NULL,
                home_score INTEGER,
                away_score INTEGER,
                status TEXT NOT NULL
            )
        """)

        count = conn.execute(
            "SELECT COUNT(*) FROM games"
        ).fetchone()[0]

        # データがまだない場合だけサンプルを登録
        if count == 0:
            conn.executemany("""
                INSERT INTO games (
                    id, date, home_team, away_team,
                    home_score, away_score, status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, [
                (
                    1, "2026-10-13",
                    "福岡ソフトバンクホークス",
                    "北海道日本ハムファイターズ",
                    3, 2, "finished"
                ),
                (
                    2, "2026-10-13",
                    "阪神タイガース",
                    "読売ジャイアンツ",
                    None, None, "scheduled"
                ),
            ])

        conn.commit()

    finally:
        conn.close()


def get_all_games():
    """すべての試合を取得する"""
    conn = get_connection()

    try:
        rows = conn.execute(
            "SELECT * FROM games ORDER BY id"
        ).fetchall()

        return [dict(row) for row in rows]

    finally:
        conn.close()


def get_game_by_id(game_id: int):
    """IDを指定して試合を1件取得する"""
    conn = get_connection()

    try:
        row = conn.execute(
            "SELECT * FROM games WHERE id = ?",
            (game_id,)
        ).fetchone()

        return dict(row) if row else None

    finally:
        conn.close()

def create_game(game_data: dict):
    """新しい試合をデータベースに登録する"""
    conn = get_connection()

    try:
        cursor = conn.execute("""
            INSERT INTO games (
                date, home_team, away_team,
                home_score, away_score, status
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            game_data["date"],
            game_data["home_team"],
            game_data["away_team"],
            game_data.get("home_score"),
            game_data.get("away_score"),
            game_data["status"],
        ))

        conn.commit()

        game_id = cursor.lastrowid
        row = conn.execute(
            "SELECT * FROM games WHERE id = ?",
            (game_id,)
        ).fetchone()

        return dict(row)

    finally:
        conn.close()
