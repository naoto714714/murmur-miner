# 参考：https://docs.perplexity.ai/api-reference/chat-completions
import os

import requests
from dotenv import load_dotenv

from utils import measure_time

PROMPT = """
これは会話の音声を文字起こししたものです。
要約して、Markdown記法で以下のフォーマットで出力して。

## 【3行要約】
- 会話全体を3行で要約

## 【主要トピックス】
### タイトル
- 内容

## 【その他】
- 主要トピック以外の役立ちそうな話題を箇条書き
"""


@measure_time
def summary(transcribed_text):
    load_dotenv()
    token = os.getenv("API_TOKEN")
    url = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "llama-3.1-sonar-large-128k-chat",
        "messages": [
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": transcribed_text},
        ],
        # "max_tokens": 1000,
        "temperature": 0.2,
        "top_p": 0.9,
        # "search_domain_filter": ["perplexity.ai"],
        "return_images": False,
        "return_related_questions": False,
        "search_recency_filter": "month",
        "top_k": 0,
        "stream": False,
        "presence_penalty": 0,
        "frequency_penalty": 1,
    }
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    response_json = response.json()
    content = response_json["choices"][0]["message"]["content"]
    return content
