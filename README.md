# baseball-api
FastAPIとSQLiteを使った野球試合情報API
# Baseball Game API

FastAPIとSQLiteを使用して作成した、野球の試合情報を管理するREST APIです。

## 概要

野球の試合情報を取得・登録できるAPIを開発しました。

## 使用技術

- Python 3.12
- FastAPI
- SQLite
- Pytest
- Git / GitHub

## 主な機能

- APIの稼働確認
- 試合情報の一覧取得
- 試合IDによる詳細取得
- 試合情報の新規登録
- 試合が存在しない場合の404エラー処理
- 自動テストによる動作確認
- チーム名による試合検索（ホーム・アウェイ両チームに対応）
- 日付による試合検索

## API一覧

| メソッド | パス | 機能 |
|---|---|---|
| GET | `/` | APIの稼働確認 |
| GET | `/games` | 試合一覧の取得 |
| GET | `/games/{game_id}` | 試合詳細の取得 |
| POST | `/games` | 試合情報の登録 |
GET	/games?team=ソフトバンク	チーム名で検索
GET	/games?date=2026-10-13	日付で検索

## ローカルでの起動方法

### 1. リポジトリを取得

```bash
git clone https://github.com/okayuichiro1504-cell/baseball-api.git
cd baseball-api
```

### 2. 仮想環境を作成

```bash
python -m venv .venv
```

### 3. 仮想環境を有効化（Windows PowerShell）

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. 必要なライブラリをインストール

```bash
pip install fastapi "uvicorn[standard]" pytest httpx
```

### 5. APIを起動

```bash
uvicorn main:app --reload
```

ブラウザで http://127.0.0.1:8000/docs を開くと、APIの動作を確認できます。

## テスト

以下のコマンドで自動テストを実行できます。

```bash
pytest -v
```

現時点で5件のテストが成功しています。

## 今後の改善予定

- チーム名や日付による検索機能
- 入力値のバリデーション強化
- AWS環境へのデプロイ
- CI/CDパイプラインの構築
- APIの監視・ログ管理

※ 現在の試合データは動作確認用のサンプルデータです。
