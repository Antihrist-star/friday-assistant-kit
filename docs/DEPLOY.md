# Инструкция по развёртыванию Friday API

## Минимальные системные требования

- **CPU:** 4 ядра
- **RAM:** от 8 GB (рекомендуется 16 GB)
- **Диск:** 20 GB SSD

## Установка (Linux / macOS)

    git clone <repo_url>
    cd friday-assistant

    # Установка Ollama и модели PhiPhi-‑3-mini3‑mini
    curl -fsSL https://ollama.com/install.sh | sh
    ollama pull phi3

    # Установка Python‑зависимостей
    pip install fastapi uvicorn pydantic requests

    # Запуск FastAPI сервиса
    uvicorn src.friday:app --host 0.0.0.0 --port 8000

## Запуск через Docker

Docker‑образ будет добавлен после реализации MVP. В будущем будет предоставлен `Dockerfile` для развёртывания в изолированном контейнере.

## Примечания

Все вычисления по генерации ответов выполняются локально — данные о сделках не покидают пределы вашего сервера.
