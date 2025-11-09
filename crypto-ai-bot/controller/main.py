import os, uuid, asyncio, json
from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import redis
from dotenv import load_dotenv

load_dotenv()
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

app = FastAPI(title="Controller - Orquestrador")

class MarketRequest(BaseModel):
    symbol: str
    candles: list = None

async def call_model(url, payload):
    async with httpx.AsyncClient(timeout=20) as client:
        resp = await client.post(url, json=payload)
        return resp.json()

@app.post("/process")
async def process(req: MarketRequest):
    payload = req.dict()
    # 1) chamar predictor e sentiment em paralelo
    try:
        m1, m2 = await asyncio.gather(
            call_model("http://ts_model:8000/predict", payload),
            call_model("http://sentiment_model:8000/predict", payload)
        )
    except Exception as e:
        return {"error": "failed to call models", "detail": str(e)}

    # 2) decisor simulado (GPT desativado)
    content = "WAIT (simulação)"  

    # 3) enfileira ordem
    request_id = str(uuid.uuid4())
    order = {
        "request_id": request_id,
        "symbol": req.symbol,
        "models": {"ts": m1, "sentiment": m2},
        "decision": content
    }
    r.lpush("orders_queue", json.dumps(order))
    return {"status": "queued", "request_id": request_id, "decision": content}
