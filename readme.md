## Описание

Проект с загрузкой файлов и отдачей их с помощью REST методов.

Страница загрузки файлов отдается на `/`. После запуск сервера доступна по адресу `localhost:8000/`.
Список доступных методов:
- загрузка файлов через api — `POST localhost:8000/api/images/`;
- список всех файлов — `GET localhost:8000/api/images/`;
- конкретный файл — `GET localhost:8000/api/images/{id}/`;
- удаление файла — `DELETE localhost:8000/api/images/{id}/`;

## Подготовка

Необходимо накатить миграции для локльной sqlite базы.

`python manage.py migrate`

## Запуск

Запуск тестового сервера без веб-сервера и сервера приложения.

`python manage.py runserver`