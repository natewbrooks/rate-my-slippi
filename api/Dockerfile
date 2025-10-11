FROM python:3.10-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel && pip install -r requirements.txt

COPY . .
# Ensure your app exposes /api/health if you keep the proxy config below
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
