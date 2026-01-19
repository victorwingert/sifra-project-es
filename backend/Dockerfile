## --------------------------------- Builder Stage --------------------------------- ##
FROM python:3.13.9-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:0.9.13 /uv /uvx /bin/

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY ./pyproject.toml ./uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-install-project

## --------------------------------- Production Stage --------------------------------- ##
FROM python:3.13.9-slim AS production

RUN useradd --create-home appuser
USER appuser
WORKDIR /app

COPY ./src ./src
COPY --from=builder /app/.venv .venv

ENV PATH="/app/.venv/bin:$PATH"

CMD ["fastapi", "run", "src/main.py", "--proxy-headers", "--port", "80"]