import os, time, json
import redis
import ccxt
from dotenv import load_dotenv

load_dotenv()
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY", "")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET", "")

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

exchange = ccxt.binance({
    'apiKey': BINANCE_API_KEY,
    'secret': BINANCE_API_SECRET,
    'enableRateLimit': True,
    'urls': {
        'api': 'https://testnet.binance.vision/api'
    }
})

print("Executor started, listening for orders...")
while True:
    item = r.brpop("orders_queue", timeout=5)
    if not item:
        time.sleep(1)
        continue
    _, order_raw = item
    try:
        order = json.loads(order_raw)
    except:
        print("Malformed order:", order_raw)
        continue

    decision_text = order.get("decision","").upper()
    symbol = order.get("symbol", os.getenv("DEFAULT_SYMBOL","BTC/USDT"))
    size = float(os.getenv("DEFAULT_ORDER_SIZE", "0.001"))

    try:
        if "BUY" in decision_text:
            print("Placing BUY market order", symbol, size)
            resp = exchange.create_market_order(symbol, 'buy', size)
            print("Executed:", resp)
        elif "SELL" in decision_text:
            print("Placing SELL market order", symbol, size)
            resp = exchange.create_market_order(symbol, 'sell', size)
            print("Executed:", resp)
        else:
            print("No actionable decision:", decision_text)
    except Exception as e:
        print("Failed to execute order:", str(e))
