FROM python:3.12-slim-bookworm

WORKDIR /app

ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_HOME=/etc/poetry
ENV PATH=${POETRY_HOME}/bin:${PATH}

RUN curl -sSL https://install.python-poetry.org | python3 -

#COPY pyproject.toml poetry.lock ./

#RUN poetry install --no-interaction

#COPY ./app .
