$ErrorActionPreference = "Stop"

Write-Host "Starting database (Docker Compose)..."
docker compose -f "back/docker-compose.yml" up -d --build

Write-Host "Building front..."
Push-Location "front"
bun run build
Pop-Location

Write-Host "Starting backend server..."
Push-Location "back"
python run.py
