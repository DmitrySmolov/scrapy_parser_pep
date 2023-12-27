
# Проект парсинга scrapy_parser_pep

scrapy_parser_pep это асинхронный парсер, удобно компилирующий информацию по статьям PEP (Python Enhancement Proposals) с официального сайта языка программирования Python. Он автоматически создаёт два файла формата csv: первый - со списком всех известных на текущий момент статей PEP (с указанием их номеров, названия и текущего статуса), второй - со сводными данными о количестве статей PEP по всем обнаруженным статусам и итоговым числом всех статей.

## Возможности приложения

- Парсинг всех статей PEP с официального сайта Python
- Генерация списка всех найденых PEP в формате csv
- Генерация отчёта по количеству PEP в зависимости от текущего статуса в формате csv

## Технологии

[![Python][Python-badge]][Python-url]
[![Scrapy][Scrapy-badge]][Scrapy-url]

## Установка

Клонируйте репозиторий на ваш компьютер, в локальном репозитории создайте и активируйте виртуальное окружение, обновите менеджер пакетов pip и установите зависимости из файла requirements.txt.

```bash
git clone <адрес репозитория>
python -m venv venv
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Использование

Находясь в корневой директории приложения, запустите парсер при помощи следующей команды:

```bash
scrapy crawl pep
```
В результате работы парсера в корневой директории приложения в папке results (она будет создана автоматически, если её нет) появятся два описаных выше файла:
- pep_<дата_создания>T<время_содания>.csv
- status_summary_<дата_создания>_<время_содания>.csv

## Авторство

Code - Дима Смолов

## Лицензия

[MIT](https://choosealicense.com/licenses/mit/)

<!-- MARKDOWN LINKS & BADGES -->

[Python-url]: https://www.python.org/
[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

[Scrapy-url]: https://scrapy.org/
[Scrapy-badge]: https://img.shields.io/badge/Scrapy-64E27C?style=for-the-badge&logo=scrapy&logoColor=white
