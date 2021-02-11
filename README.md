## Тестовое задание для backend разработчика

#### Клонируем проект из репозитория: 
```
git clone https://github.com/MisterLenivec/image_resizer.git
```

#### Переходим в корневую папку проекта.(Там где лежит файл manage.py)
```
cd image_resizer
```

#### Если вдруг у вас нет venv, то:
```
sudo apt-get install python3-venv
```

#### Создаём виртуальное окружение:
```
python3 -m venv my_super_env
```

#### И активируем его:
```
source my_super_env/bin/activate
```

#### Если нужно обновить pip:
```
python3 -m pip install --upgrade pip
```

#### Установить зависимости в уже активированное нами виртуальное окружение:
```
pip3 install -r requirements.txt
```

#### Создадим и применим миграции:
```
python manage.py makemigrations
python manage.py migrate
```

#### Суперпользователя создавать нет необходимости.
#### Запускаем локльный сервер:
```
python manage.py runserver
```

#### И переходим по адресу:
```
http://127.0.0.1:8000/
```
