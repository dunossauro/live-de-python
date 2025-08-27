#!/bin/sh

poetry run alembic upgrade head
poetry run taskiq scheduler app:scheduler
