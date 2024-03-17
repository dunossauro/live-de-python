FROM python:3.12.2-slim

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/

RUN pip install poetry

COPY pyproject.toml .

RUN poetry install
RUN opentelemetry-bootstrap -a install

COPY . .

CMD opentelemetry-instrument \
    --logs_exporter console,otlp \
    uvicorn eggs.app:app \
    --port 8002 \
    --host 0.0.0.0
