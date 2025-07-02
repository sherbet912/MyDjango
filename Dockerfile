FROM python:3.13.4-bookworm

# 設定工作目錄
WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get install -y pipx \
    && pipx ensurepath \
    && apt-get install -y python3-venv \
    && pipx install poetry \
    && pipx ensurepath \
    && apt-get install -y iputils-ping

COPY pyproject.toml .

ENV PATH="/root/.local/bin:${PATH}" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN poetry install \
    && rm -rf $POETRY_CACHE_DIR