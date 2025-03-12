import tkinter as tk
from tkinter import ttk
import threading
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from trading_utils import get_live_price, place_trade, track_whale_activity, ai_trading
from config import TRADE_PAIR, WHALE_WALLETS

# ✅ Futuristic UI Colors
BG_COLOR = "#1b1b1b"  # Dark Mode Background
TEXT_COLOR = "#00FFAA"  # Neon Green Text
BUTTON_COLOR = "#00FFFF"  # Neon Cyan Buttons

# ✅ Advanced Trading UI
class TradingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WhaleTracker AI Trading 🚀")
        self.geometry("1000x750")
        self.configure(bg=BG_COLOR)
        self.create_widgets()

    def create_widgets(self):
        # ✅ Title
        self.title_label = tk.Label(self, text="🚀 WhaleTracker AI Trading", fg=TEXT_COLOR, bg=BG_COLOR, font=("Courier", 18))
        self.title_label.pack(pady=10)

        # ✅ Crypto Selection
        self.trade_pair_label = tk.Label(self, text="Select Trading Pair:", fg=TEXT_COLOR, bg=BG_COLOR, font=("Courier", 12))
        self.trade_pair_label.pack()
        self.trade_pair_dropdown = ttk.Combobox(self, values=["BTC/USD", "ETH/USD", "SOL/USD", "ADA/USD"], state="readonly")
        self.trade_pair_dropdown.set(TRADE_PAIR)
        self.trade_pair_dropdown.pack()

        # ✅ Trade Amount Input
        self.amount_label = tk.Label(self, text="Trade Amount (BTC):", fg=TEXT_COLOR, bg=BG_COLOR, font=("Courier", 12))
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self, bg=BG_COLOR, fg=TEXT_COLOR, font=("Courier", 12))
        self.amount_entry.insert(0, "0.01")
        self.amount_entry.pack()

        # ✅ Whale Wallet Selection
        self.whale_wallet_label = tk.Label(self, text="Select Whale Wallet:", fg=TEXT_COLOR, bg=BG_COLOR, font=("Courier", 12))
        self.whale_wallet_label.pack()
        self.whale_wallet_dropdown = ttk.Combobox(self, values=list(WHALE_WALLETS["Bitcoin"]), state="readonly")
        self.whale_wallet_dropdown.set(list(WHALE_WALLETS["Bitcoin"])[0])
        self.whale_wallet_dropdown.pack()

        # ✅ Execute Trade Button
        self.trade_button = tk.Button(self, text="🔥 Execute Trade", command=self.execute_trade, bg=BUTTON_COLOR, fg=BG_COLOR, font=("Courier", 12))
        self.trade_button.pack(pady=10)

        # ✅ Live Price Display
        self.live_price_label = tk.Label(self, text="Fetching Price...", fg=TEXT_COLOR, bg=BG_COLOR, font=("Courier", 12))
        self.live_price_label.pack()

        # ✅ Graph Section
        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack()
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack()

        # ✅ Auto-Update Price & Chart
        self.update_data()

    # ✅ Fetch Live Price & Update Chart
    def update_data(self):
        price = get_live_price()
        if price:
            self.live_price_label.config(text=f"📊 {TRADE_PAIR} Price: ${price}")

            # 🔥 Sleek Graph Update
            self.ax.clear()
            self.ax.plot([price - 50, price, price + 50], marker="o", linestyle="-", color="cyan")
            self.ax.set_title(f"Live {TRADE_PAIR} Price Chart", fontsize=12, color="white")
            self.ax.set_ylabel("Price (USD)", color="white")
            self.ax.set_xlabel("Time", color="white")
            self.ax.grid(True, linestyle="--", alpha=0.5)
            self.canvas.draw()

        self.after(5000, self.update_data)

    # ✅ Execute Trade
    def execute_trade(self):
        amount = self.amount_entry.get()
        try:
            amount = float(amount)
            trade = place_trade(amount)
            if trade:
                print(f"[✅] Trade Successful: {trade}")
        except ValueError:
            print("[❌] Invalid Trade Amount")

# ✅ Start AI & Whale Tracking Threads
def start_threads():
    threading.Thread(target=track_whale_activity, daemon=True).start()
    threading.Thread(target=ai_trading, daemon=True).start()

# ✅ Launch UI
if __name__ == "__main__":
    start_threads()
    app = TradingApp()
    app.mainloop()
