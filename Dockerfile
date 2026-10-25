FROM python:3.14-slim AS builder

WORKDIR /build

RUN pip install --no-cache-dir --upgrade pip

COPY ./requirements ./requirements

RUN pip wheel --no-cache-dir --no-deps \
    --wheel-dir /build/wheels -r ./requirements/requirements.txt


FROM python:3.14-slim

RUN useradd -m -u 1000 appuser

WORKDIR /app

COPY --from=builder /build/wheels /wheels

COPY ./requirements ./requirements

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --no-index --find-links=/wheels -r ./requirements/requirements.txt \
    && rm -rf /wheels ./requirements~

COPY --chown=appuser:appuser ./app ./app

USER appuser

CMD ["python", "-m", "app.main"]
