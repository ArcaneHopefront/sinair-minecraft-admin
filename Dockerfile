FROM python:3.14-slim AS builder

WORKDIR /build

RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps \
    --wheel-dir /build/wheels -r requirements.txt


FROM python:3.14-slim

RUN useradd -m -u 1000 appuser

WORKDIR /app

COPY --from=builder /build/wheels /wheels

RUN pip install --no-cache-dir --no-index --find-links=/wheels /wheels/* \
    && rm -rf /wheels

COPY --chown=appuser:appuser ./app ./app

USER appuser

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
