# api_final
api final
<h1>Описание</h1>
<h4>Это проект "api yatube" предназначенный для взаимодействия фронтенда и/или какого-либо приложения с  бэкендом</h4>
<h4>Это собственный API, через него с помощью JSON передаются запросы</h4>
<h1>Как запустить проект</h1>
Клонировать репозиторий и перейти в него в командной строке:

```
git clone ...
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

<h1>Примеры запросов</h1>
```
http://127.0.0.1:8000/api/v1/posts/
```

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
