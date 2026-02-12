#!/usr/bin/env bash
set -euo pipefail

echo "Starting database (Docker Compose)..."
docker compose -f back/docker-compose.yml up -d --build

echo "Building front..."
(
  cd front
  bun run build
)

echo "Starting backend server..."
(
  cd back
  python run.py
)
