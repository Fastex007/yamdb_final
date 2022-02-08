# YaMDb
![yamdb_final](https://github.com/Fastex007/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

#### Автор
Oleg Pronkin
https://github.com/Fastex007/

### Описание
Сервис сбора отзывов пользователей о фильмах, музыке и книгах.

### Регистрация:
1. POST-запрос с параметром *email* на */api/v1/auth/email/.*
2. YaMDB отправляет письмо с кодом подтверждения (*confirmation_code*) на адрес *email* .
3. Пользователь отправляет POST-запрос с параметрами *email* и *confirmation_code* на 
*/api/v1/auth/token/*, в ответе на запрос ему приходит *token* (JWT-токен).
Подробная документация API находится по адресу *redoc/*

---

## Запуск проекта:

```bash
git clone git@github.com:Fastex007/yamdb_final.git
```

```bash
cd api_yamdb/
```

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

Запустить приложение в контейнерах:

*из директории `infra/`*
```bash
docker-compose up -d --build
```

Выполнить миграции:

*из директории `infra/`*
```bash
docker-compose exec web python manage.py migrate
```

Создать суперпользователя:

*из директории `infra/`*
```bash
docker-compose exec web python manage.py createsuperuser
```

Собрать статику:

*из директории `infra/`*
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

Остановить приложение в контейнерах:

*из директории `infra/`*
```bash
docker-compose down -v
```
Запуск `pytest`:

*при запущенном виртуальном окружении*
```bash
cd infra_sp2 && pytest
```

### Документация API с примерами:

```json
/redoc/
```

### шаблон наполнения env-файла
Переименовать env в .env