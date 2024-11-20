# syntax=docker/dockerfile:1
FROM python:3.11-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    # gitはdevcontainer用
    # git \
    ffmpeg \
    sox \
    && apt clean && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
# 参考：https://docs.astral.sh/uv/guides/integration/docker/#installing-uv

COPY pyproject.toml uv.lock README.md .env ./
# README.mdもコピーしないと、uv syncでエラーが出る

RUN uv sync --frozen
# --frozenは、uv.lockを更新しないようにするため

COPY ./app ./
COPY ./input_audios ./input_audios
COPY ./output_summaries ./output_summaries

ENTRYPOINT ["uv", "run", "main.py"]
