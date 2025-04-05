import traceback
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.agent import AgentRunResult
from pydantic_ai import Agent
import os
from typing import List, Dict, Any, Optional, Union

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv

# 環境変数の読み込み
load_dotenv()

# AIクライアントの初期化
model = OpenAIModel(
    'deepseek/deepseek-chat-v3-0324:free',
    # 'google/gemini-2.0-flash-exp:free',
    provider=OpenAIProvider(
        base_url='https://openrouter.ai/api/v1', api_key=os.getenv('OPENROUTER_API_KEY')
    ),
)
ai_client = Agent(
    model=model,
    system_prompt='''あなたは有能な アシスタント Agentです。
    ''',
    instrument=True,
)

# Slackアプリの初期化
app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)

@app.event("app_mention")
def handle_mention(event, say):
    """メンションイベントを処理してAIで応答"""
    try:
        prompt = event["text"]
        response:AgentRunResult = ai_client.run_sync(prompt)
        print(response)
        say(f"```{response.data}```")
    except Exception as e:
        say(f"エラーが発生しました: {str(e)}")
        print(e)
        print(traceback.format_exc())

if __name__ == "__main__":
    # Socket Modeでアプリを起動
    handler = SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN"))
    handler.start()
