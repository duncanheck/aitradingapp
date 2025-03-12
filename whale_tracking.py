import requests
import time
import threading
import json
from config import WHALE_WALLETS, KRAKEN_API_KEY, KRAKEN_API_SECRET

def fetch_whale_activity():
    """Fetches large whale transactions and checks if they are buying or selling."""
    print("[🐋] Tracking Whale Transactions...")
    
    while True:
        try:
            for coin, wallets in WHALE_WALLETS.items():
                for wallet in wallets:
                    url = f"https://api.blockchair.com/{coin.lower()}/dashboards/address/{wallet}"
                    response = requests.get(url)
                    data = response.json()

                    if "data" in data and wallet in data["data"]:
                        balance = data["data"][wallet]["address"]["balance"]
                        print(f"[📊] {wallet} Balance: {balance} {coin}")

                        # 🔹 If balance suddenly increases, whale is BUYING
                        if balance > 100000:  # Threshold for whale transaction
                            print(f"[🚀] Whale bought {coin} - Copy Trading Activated!")
                            # TODO: Trigger trade function in main.py

            time.sleep(30)  # Reduce API calls to avoid rate limits
        except Exception as e:
            print(f"[❌] Error tracking whales: {e}")
            time.sleep(60)  # Wait longer on errors

# Start Whale Tracking in a Background Thread
def start_whale_tracking():
    tracking_thread = threading.Thread(target=fetch_whale_activity, daemon=True)
    tracking_thread.start()
