# api_yamdb
### Описание
Проект YaMDb собирает отзывы пользователей на различные произведения.
### Технологии
- Python 3.7
- Django 2.2.19
- Django REST framework 3.12.4
### Запуск проекта в dev-режиме (Windows)
- Создайте и активируйте виртуальное окружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
``` 
- Выполните миграции:
```
python manage.py migrate
```
- Запустите проект:
```
python manage.py runserver
```
### Пример использования
- Получить список всех произведений.
```
http://127.0.0.1:8000/api/v1/titles/
```
```
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "name": "string",
      "year": 0,
      "rating": 0,
      "description": "string",
      "genre": [
        {
          "name": "string",
          "slug": "string",
        }
      ]
      "categoty": {
          "name": "string",
          "slug": "string",
      }  
    }
  ]
}
```
### Авторы
alexbulavkin, lovechy, VankoID


















