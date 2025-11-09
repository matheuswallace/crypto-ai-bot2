from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="Sentiment Model (dummy)")

class Payload(BaseModel):
    symbol: str
    candles: list = None

@app.post("/predict")
def predict(payload: Payload):
    score = float(np.round(np.random.uniform(-0.6, 0.6), 3))
    summary = "positivo" if score > 0 else "negativo" if score < 0 else "neutro"
    return {"score": score, "summary": summary}
