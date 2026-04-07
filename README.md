# Sprint_9 - Автотесты для Foodgram

Проект содержит набор автоматических тестов для веб-приложения Foodgram, написанных с использованием pytest и Selenium.

## 📋 Содержание

- [Технологии](#технологии)
- [Структура проекта](#структура-проекта)
- [Установка и запуск](#установка-и-запуск)
- [Запуск тестов](#запуск-тестов)
- [Запуск с Allure отчетом](#запуск-с-allure-отчетом)
- [Docker](#docker)
- [Тестовые сценарии](#тестовые-сценарии)

## 🛠 Технологии

- **Python** 3.14+
- **pytest** - фреймворк для тестирования
- **Selenium** - автоматизация браузера
- **Allure** - генерация отчетов
- **Faker** - генерация тестовых данных
- **Docker** - контейнеризация (Selenoid)

## 📁 Структура проекта
📁 Sprint_9/
├── 📁 assets/
│   └── 🖼️ recipe.jpeg
├── 📁 locators/
│   ├── 📄 auth_locators.py
│   ├── 📄 base_locators.py
│   ├── 📄 create_recipe_locators.py
│   ├── 📄 header_locators.py
│   └── 📄 registration_locators.py
├── 📁 pages/
│   ├── 📄 auth_page.py
│   ├── 📄 base_page.py
│   ├── 📄 create_recipe_page.py
│   ├── 📄 header_auth.py
│   ├── 📄 header_unauth.py
│   └── 📄 registration_page.py
├── 📁 tests/
│   ├── 📄 test_auth.py
│   ├── 📄 test_create_recipe.py
│   └── 📄 test_registration.py
├── 📄 .dockerignore
├── 📄 .gitignore
├── 📄 conftest.py
├── 📄 constants.py
├── 📄 data.py
├── 📄 docker-compose.yml
├── 📄 Dockerfile
├── 📄 helpers.py
├── 📄 README.md
└── 📄 requirements.txt

## 🚀 Установка и запуск

### pip install -r requirements.txt -- установка зависимостей
### allure generate allure-results -o allure-report --clean
### allure serve allure-results
### allure open allure-report