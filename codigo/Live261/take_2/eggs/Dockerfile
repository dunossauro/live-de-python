FROM python:3.12.2-slim

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/

RUN pip install poetry

COPY pyproject.toml .

RUN poetry install

COPY . .

CMD uvicorn eggs.app:app \
    --port 8002 \
    --host 0.0.0.0
