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