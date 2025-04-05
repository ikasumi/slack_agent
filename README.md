# Slack AI Bot with OpenRouter

Slack上でOpenRouter経由のAIと会話できるボットアプリケーション

## セットアップ

1. 依存関係のインストール:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

2. 環境変数設定 (`.env`ファイル):
```
SLACK_BOT_TOKEN=xoxb-...
SLACK_SIGNING_SECRET=...
SLACK_APP_TOKEN=xapp-...
OPENROUTER_KEY=sk-or-...
```

3. Slackアプリ設定:
- [Slack APIダッシュボード](https://api.slack.com/)で以下を設定:
  - **Socket Mode** を有効化
  - `app_mentions:read` と `chat:write` ボットスコープを追加
  - イベントサブスクリプションで `app_mention` を有効化

## 実行方法

```bash
venv/bin/python -m uvicorn main:app --reload
```

## 使用方法

1. Slackワークスペースでボットをインストール
2. ボットにメンションしてメッセージを送信
3. AIからの応答を確認

## 注意事項

- OpenRouterのAPIキーは厳重に管理してください
- 本番環境では`.env`をバージョン管理に含めないでください
- 常時稼働が必要な場合はプロセス管理ツールを使用してください

## ライセンス

[MIT License](LICENSE)
Copyright (c) 2025 kenta sugawara
