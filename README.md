# Архитектурная археология

### Веб-приложение, разработанное для Лаборатории архитектурной археологии Института археологии Российской академии наук


Разработано с применением следующего стека:
1. Python 3
2. Веб-фреймворк Django
3. Django Rest Framework (для отдачи данных на большую карту ИА РАН, пока не используется, фронтендеры карты молчат)
4. СУБД PostgreSQL версии 16
5. Nginx reverse proxy
6. Развернуто в Docker-контейнерах на сервере под управлением Ubuntu


#### Инструкция для запуска приложения в случае переноса на другой сервер, если его будет поддерживать не автор кода

1. Проект необходимо устанавливать на сервере под управлением Linux, также на него необходимо установить [Docker Engine](https://docs.docker.com/engine/install/) и плагин [Docker Compose](https://docs.docker.com/compose/install/linux/#install-using-the-repository)

2. Скачайте исходный код из репозитория:

```git clone https://github.com/Strokman/architecture_archaeology_ia_ras.git ```

3. В корневой папке проекта нужно создать файл ```.env```. Содержимое предоставлю по запросу.

4. В корневую папку также необходимо переместить директорию ```postgres-data```, в которой содержится база данных на текущем сервере. Либо восстановить базу из файла дампа.

5. Запустить проект командой 
```sudo docker compose up --build```

### Структура проекта

Проект в целом полностью следует архитектуре, которую предлагает Django "из коробки".

* [Основные настройки](./architecture_archaeology/architecture_archaeology)

Пакет содержит основные настройки проекта, а также модуль настроек [Celery](./architecture_archaeology/architecture_archaeology/celery.py)

* [API](./architecture_archaeology/api/)

Приложение для получения данных о памятниках из базы данных и выгрузки их на основную ИА РАН [Django Rest Framework](https://www.django-rest-framework.org). Аутентификация - дефолтная с помощью плагина [Django Rest Framework Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

* Следующие приложения содержат представления, фильтры, формы, относящиеся к основным сущностям:
    * [Археологические памятники](./architecture_archaeology/arch_site/)
    * [Постройки](./architecture_archaeology/building/)
    * [Находки](./architecture_archaeology/artefact/)
    * [Фрески/Изображения](./architecture_archaeology/artwork/)
    * [Измерения](./architecture_archaeology/measurement/)

В коде есть комментарии, которые описывают основные блоки и их функции

Тесты в основном черновые и есть только в нескольких приложениях. В идеале их нужно писать с нуля