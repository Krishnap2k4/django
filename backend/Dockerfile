# ============================================================
# Multi-stage Dockerfile for TaskFlow Backend
# ============================================================

# Stage 1: Base image with system dependencies
FROM python:3.14-slim AS base

# Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# ============================================================
# Stage 2: Dependencies (cached layer)
# ============================================================
FROM base AS dependencies

COPY requirements/ requirements/

ARG ENVIRONMENT=production
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements/${ENVIRONMENT}.txt

# ============================================================
# Stage 3: Application
# ============================================================
FROM dependencies AS application

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p logs media staticfiles

# Create non-root user for security
RUN addgroup --system taskflow && \
    adduser --system --ingroup taskflow taskflow && \
    chown -R taskflow:taskflow /app

USER taskflow

# Default command (overridden in docker-compose per service)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
