from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="TS Model (dummy)")

class Payload(BaseModel):
    symbol: str
    candles: list = None

@app.post("/predict")
def predict(payload: Payload):
    trend = "up" if np.random.rand() > 0.5 else "down"
    conf = float(np.round(np.random.rand() * 0.6 + 0.2, 3))
    return {"trend": trend, "confidence": conf, "horizon": "1h"}
