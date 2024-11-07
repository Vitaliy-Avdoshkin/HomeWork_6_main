# Vitaliy_Avdoshkin_HomeWork_6

# Проект по БД

## Описание

В рамках домашних заданий к разделу №6 "Основы Django" будет создан проект
интернет-магазина, который будете дорабатывать на каждом уроке
в течение всего курса.

## Установка:

1. Клонируйте репозиторий:

```
git clone https://github.com/Vitaliy-Avdoshkin/vitaliy_avdoshkin_CourseWork_5
```
## Конфигурация
1. Создайте виртуальное окружение poetry.

```
poetry env
```

2. Установите следующие библиотеки, используя соответствующие команды:
 - библиотека django
```commandline
poetry add django
```
- библиотека psycopg2
```commandline
poetry add psycopg2
```
или
```
pip install psycopg2
```
- библиотека dotenv
```commandline
poetry add python-dotenv
```
или
```
pip install python-dotenv
```
3. Создайте приложение catalog, используя код ниже
```commandline
 python manage.py startapp catalog
```

