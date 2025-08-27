FROM python:3.13-slim

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/

RUN pip install poetry

COPY pyproject.toml .

RUN poetry install --no-root

COPY . .

CMD taskiq scheduler app:scheduler
