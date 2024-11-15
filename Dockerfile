FROM python:3.11-slim-bookworm

WORKDIR /app

RUN apt update && apt install -y \
    git \
    curl \
    ffmpeg \
    sox

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
# 参考：https://docs.astral.sh/uv/guides/integration/docker/#installing-uv

COPY pyproject.toml uv.lock README.md ./
# README.mdもコピーしないと、uv syncでエラーが出る

RUN uv sync --frozen
# --frozenは、uv.lockを更新しないようにするため

COPY ./app .
