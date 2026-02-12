# Запуск проекта

Ниже два скрипта: для Windows (PowerShell) и для Linux/macOS (bash). Они делают одно и то же:
1) запускают БД через docker compose,
2) собирают фронтенд,
3) запускают backend сервер.

## Windows (PowerShell)

```powershell
./start.ps1
```

## Linux / macOS

```bash
chmod +x ./scripts/start.sh
./start.sh
```

## Дополнительно

- Подробности по backend см. в [back/README.md](back/README.md)
- Подробности по frontend см. в [front/README.md](front/README.md)