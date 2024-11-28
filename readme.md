# Домашняя работа Нетология: Fastapi, part 1

Реализация сервиса объявлений купли/продажи.

## Сервис предполагает CRUD методы, а именно:

*   Создание: POST /v1/advertisement
*   Обновление: PATCH /v1/advertisement/{advertisement_id}
*   Удаление: DELETE /v1/advertisement/{advertisement_id}
*   Получение по id: GET  /v1/advertisement/{advertisement_id}
*   Поиск по полям: GET /v1/advertisement?{query_string}

(примеры запросов в файле request-examples.http)

## Docker-compose
Приложение докеризировано, для запуска контейнера используем команды оркестратора:

```
docker-compose up db -d
docker-compose up app -d
```

Приятной проверки 😉