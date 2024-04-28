FROM python:3.12.2-slim

EXPOSE 8000

ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install poetry
COPY pyproject.toml poetry.lock .
RUN poetry install --no-root
COPY . .

RUN opentelemetry-bootstrap -a install

CMD opentelemetry-instrument \
    uvicorn dt.app:app \
    --host 0.0.0.0
