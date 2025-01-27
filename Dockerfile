FROM python:3.9-slim as builder

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip && \
    pip install poetry
RUN poetry config virtualenvs.in-project true && \
    poetry install --no-root --no-dev
COPY . .

FROM python:3.9-slim

WORKDIR /app
COPY --from=builder /app/.venv ./.venv
COPY . .
ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]