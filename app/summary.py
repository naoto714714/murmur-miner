# 参考：https://docs.perplexity.ai/api-reference/chat-completions
import os

import requests
from dotenv import load_dotenv

PROMPT = """
これは会議の音声を文字起こししたものです。
要約して。
"""


def summary(transcribed_text, output_path):
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
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    return content
