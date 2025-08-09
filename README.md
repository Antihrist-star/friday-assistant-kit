# Friday Assistant KIT — v2

Friday — интерактивный AI ассистент для трейдеров и комьюнити. Работает локально (через Ollama/llama.cpp) и умеет масштабироваться в облако. Этот репозиторий — расширенная версия (MVP+) с модульной архитектурой и мультиканальной интеграцией.

## Главные фичи
- `POST /api/friday/comment` — комментарий к сделке (юмор, совет, reasoning‑light).
- `POST /api/friday/explain` — пошаговое объяснение (краткий reasoning).
- `POST /api/digest/generate` — утренний дайджест.
- `POST /api/events` — универсальный вебхук (KIT/TradingView).
- Персонализация («скины»): выбор стиля общения (`default`, `strict`, `coach`).
- Переключаемые модели: `fast` | `balanced` | `reasoning` | `vision`.
- Интеграции: KIT dashboard, Telegram (бот), позже — Discord.

## Быстрый старт
1. Склонируй репозиторий и установи зависимости:
   ```bash
   git clone <repo_url>
   cd friday-assistant-kit
   pip install -r requirements.txt
   ```
2. Скачай модель по умолчанию и запусти Ollama:
   ```bash
   # установка Ollama (see docs/DEPLOY.md)
   ollama pull qwen2.5:7b-instruct
   ```
3. Запусти API:
   ```bash
   uvicorn apps.api.main:app --host 0.0.0.0 --port 8000
   ```
4. Пример запроса:
   ```bash
   curl -X POST http://localhost:8000/api/friday/comment \
     -H "Content-Type: application/json" \
     -d '{
       "trade_id": "001",
       "pattern": "Коробка",
       "symbol": "ETHUSDT",
       "entry_price": 3480.0,
       "current_price": 3520.0,
       "volume": "high",
       "btc_change": "+2.3%",
       "score": 0.85,
       "trigger_factors": ["HighVolume+", "BTCUp+"],
       "reasoning": "",
       "persona": "default"
     }'
   ```

## Документация
- Архитектура — `docs/ARCHITECTURE.md`
- API — `docs/API.md`
- Деплой — `docs/DEPLOY.md`
- Персонажи и стили — `docs/CHARACTER.md`
- Выбор моделей — `docs/MODELS.md`

## Roadmap
- [ ] MVP: реализация функций комментариев и объяснений.
- [ ] Интеграция Telegram-бота.
- [ ] Дайджест и обучение на данных.
- [ ] Голос и мемы.
