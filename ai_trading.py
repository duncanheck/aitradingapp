import time
import threading
import random
from trading_utils import get_live_price, place_trade  # ✅ Fix Import

# 🔹 AI Trading Algorithm
def ai_trading():
    while True:
        crypto_pair = "BTC/USD"
        live_price = get_live_price(crypto_pair)

        if live_price:
            decision = random.choice(["BUY", "SELL", "HOLD"])

            if decision == "BUY":
                print(f"[🤖] AI Decision: Buying {crypto_pair} at ${live_price}")
                place_trade(crypto_pair, 0.01)
            elif decision == "SELL":
                print(f"[🤖] AI Decision: Selling {crypto_pair} at ${live_price}")
                place_trade(crypto_pair, -0.01)

        time.sleep(10)

# ✅ Start AI Trading in a Background Thread
def start_ai_trading():
    thread = threading.Thread(target=ai_trading, daemon=True)
    thread.start()
