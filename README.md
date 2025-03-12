📌 AI Crypto Trading Bot
🚀 Automated Whale Tracking, Sniping, and AI Trading
This bot automatically trades Bitcoin (BTC) and Solana (SOL) meme coins based on AI predictions, whale tracking, and real-time market data. It also features sniping for new Solana meme coins and a live trading UI.

✨ Features
✅ Live Whale Tracking – Monitors large BTC & SOL wallet movements
✅ AI-Based Auto Trading – Predicts price movements and executes trades
✅ Solana Meme Coin Sniping – Auto-buys new tokens before they pump
✅ Live Price & Balance Updates – Tracks holdings in real-time
✅ Manual Trading UI – Allows manual trades with a single click
✅ Binance Paper Trading – Simulate trades without real money

🛠️ Installation
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/duncanheck/aitradingapp.git
cd aitradingapp
2️⃣ Set Up a Virtual Environment
sh
Copy
Edit
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up API Keys
Create a .env file in the project folder.
Add your Binance API keys:
ini
Copy
Edit
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
🚀 How to Run
Start the AI Trading Bot
sh
Copy
Edit
python main.py
This launches the trading UI, whale tracking, and AI trading.

📊 Features Explained
🎯 Sniping for Solana Meme Coins
The bot scans for new Solana meme coins every 60 seconds.
If a coin is trending, it auto-buys before prices rise.
🐋 Whale Tracking
Monitors large Bitcoin & Solana transactions in real time.
If a whale buys a large amount, the bot can follow the trade.
📈 Manual Trading UI
Select a coin from the dropdown and click "Execute Trade".
Live price updates show current market conditions.
Recent trades & balance are displayed in real-time.
🛠️ Updating the Bot
If you make changes and want to update GitHub:

sh
Copy
Edit
git add .
git commit -m "Updated AI trading bot"
git push origin main
📌 Coming Soon
✔️ Stop-loss & take-profit automation
✔️ Advanced AI trading strategies
✔️ Telegram notifications for whale alerts

📞 Need Help?
If you have issues, open a GitHub issue, or contact @duncanheck.
Happy trading! 🚀🎯
