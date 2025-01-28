# Проект калькулятора комплексных чисел

---
## Постановка задачи

Создать проект калькулятора комплексных чисел (достаточно сделать сложение, умножение и деление). Применить при создании программы архитектурные паттерны, добавить логирование калькулятора. Соблюдать принципы SOLID, паттерны проектирования.

---

## Описание проекта

Данное приложение реализовано на языке Python (версия **3.12**) и представляет собой консольный калькулятор, выполняющий базовые математические операции с комплексными числами.  

Основные особенности:
- Использование архитектурных паттернов: **Factory**, **Strategy** и **Dependency Injection**.
- Логирование операций и ошибок.
- Простота масштабирования: легко добавлять новые математические операции.

---

## Структура проекта `complex_calculator`
Проект включает следующие файлы и директории:

- **`complex_calculator/`**
  - `main.py` — Точка входа
  - `requirements.txt` — Зависимости
  - `README.md` — Инструкция по запуску
  - **`calculator/`** — Логика приложения
    - `__init__.py`
    - `operations.py` — Математические операции
    - `complex_number.py` — Класс для работы с комплексными числами
    - `logger.py` — Логирование
    - `factory.py` — Фабрика для объектов
    - `exceptions.py` — Пользовательские исключения
  - **`tests/`** — Тесты
    - `__init__.py`
    - `test_operations.py` — Тесты операций
    - `test_logger.py` — Тесты логирования


---

## Требования

Для запуска приложения вам потребуется:
- Python версии **3.12**.
- Средства для работы с виртуальным окружением Python (например, `venv`).

---

## Установка

1. Установите Python 3.12.  
   Скачать можно с официального сайта:  
   [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
3. Активируйте виртуальное окружение:
    ```bash
    venv\Scripts\activate
4. Установите зависимости:
    ```bash
   pip install -r requirements.txt

---
## Запуск приложения

1. Убедитесь, что вы находитесь в корневой папке проекта.
2. Активируйте виртуальное окружение (если оно еще не активно).
3. Выполните команду:
    ```bash
    python main.py
После запуска вы увидите результаты выполнения операций с комплексными числами в консоли.

---

## Тестирование

Для проверки корректности работы калькулятора предусмотрены автоматические тесты.

* Запуск тестов:
    ```bash
    python -m unittest discover tests

_Тесты включают:
Проверку корректности математических операций.
Обработку исключений (например, деление на ноль)._
