## Запустите создание докер образа POSTGRES командами:

```bash
cd back
docker compose up --build
```

## API

- `POST /items`
- `GET /items`
- `GET /items/{id}`
- `PUT /items/{id}`
- `DELETE /items/{id}`

Сервер работает на порту [3000](http://localhost:3000/api)
документация расположена на [/api/docs](http://localhost:3000/api/docs)

