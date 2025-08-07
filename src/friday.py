from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

app = FastAPI(title="Friday Assistant API")


class TradeRequest(BaseModel):
    """Модель запроса от торгового движка KIT."""

    trade_id: str
    pattern: str
    symbol: str
    entry_price: float
    current_price: float
    volume: str
    btc_change: str
    score: float
    trigger_factors: list[str]
    reasoning: str


class FridayResponse(BaseModel):
    """Модель ответа, возвращаемого Friday."""

    trade_id: str
    friday_comment: str
    advice: str
    humor: str


@app.post("/api/friday", response_model=FridayResponse)
async def friday_endpoint(request: TradeRequest) -> FridayResponse:
    """
    Эндпоинт для генерации комментариев к сделкам.

    Принимает описание сделки, формирует prompt, отправляет его на LLM (в будущем)
    и возвращает краткий комментарий, рекомендацию и шуточный комментарий.

    В текущей базовой реализации комментарии фиксированы и служат в качестве примера.
    """
    try:
        # TODO: Интегрировать вызов LLM с использованием шаблонов из configs/prompts.yaml
        comment = (
            "🚀 Прекрасный пробой коробки по ETH! Когда BTC поддерживает — это как ехать по автобану. "
            "Не забудь пристегнуться (SL), и приятной поездки! 🐳"
        )
        advice = "Поставь стопы чуть ниже 3450, там был сильный уровень поддержки."
        humor = "С такими сделками скоро на луне окажешься! 🌕"

        return FridayResponse(
            trade_id=request.trade_id,
            friday_comment=comment,
            advice=advice,
            humor=humor,
        )
    except Exception as exc:
        # Логирование исключения с полным стеком
        logging.exception("Ошибка обработки запроса Friday: %s", exc)
        raise HTTPException(status_code=503, detail="Сервис недоступен, попробуйте позднее.")
