# QRBanker

QRBanker — это проект для генерации QR-кодов, предназначенных для перевода через Сбербанк. Приложение позволяет пользователю создать QR-код для перевода средств с использованием Системы Быстрого Платежа (СБП).

## Описание проекта

Проект предоставляет интерфейс для создания QR-кодов с реквизитами для перевода через Сбербанк. Он включает:
- Генерацию QR-кодов для перевода средств.
- Поддержку информации о получателе (имя, телефон, сумма).

## Установка и запуск

1. **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/ayhandev/QRBANKER.git
    cd QRBANKER
    ```

2. **Создайте и активируйте виртуальное окружение (необязательно, но рекомендуется):**

    Для Linux/macOS:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    Для Windows:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Установите зависимости:**

    Убедитесь, что у вас установлен `pip` (Python Package Installer). Для установки зависимостей из файла `requirements.txt` выполните команду:

    ```bash
    pip install -r requirements.txt
    ```

4. **Настройте базу данных:**

    Выполните миграции для создания таблиц в базе данных:

    ```bash
    python manage.py migrate
    ```

5. **Запустите сервер разработки:**

    После этого запустите сервер разработки:

    ```bash
    python manage.py runserver
    ```

6. **Откройте приложение в браузере:**

    Перейдите по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/) для доступа к приложению.

## Структура проекта

- `qrcode/`: основной код проекта, включая настройки, URL и представления.
- `manage.py`: утилита для выполнения команд Django.
- `requirements.txt`: файл с зависимостями для установки через pip.

## Лицензия

Этот проект защищён авторскими правами. Все права на использование, распространение, копирование и изменение кода принадлежат автору.

Запрещается использование, копирование, модификация, сублицензирование и распространение этого программного продукта без явного разрешения владельца прав.

Все права защищены. Не может быть использовано без разрешения.