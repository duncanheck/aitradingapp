import os
import json
from cryptography.fernet import Fernet

CONFIG_FILE = "user_config.json"

# ✅ Generate Encryption Key (Only once, stored securely)
KEY_FILE = "encryption.key"
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as key_file:
        key = Fernet.generate_key()
        key_file.write(key)
else:
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()

cipher_suite = Fernet(key)

# ✅ Function to Get API Credentials
def get_api_credentials():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as file:
                encrypted_data = json.load(file)
                api_key = cipher_suite.decrypt(encrypted_data["api_key"].encode()).decode()
                api_secret = cipher_suite.decrypt(encrypted_data["api_secret"].encode()).decode()
                return api_key, api_secret
        except Exception as e:
            print(f"[❌] Error loading API credentials: {e}")

    # ✅ Prompt user for API key input
    print("🔐 Welcome! Please enter your Kraken API credentials:")
    api_key = input("🔑 Enter your Kraken API Key: ")
    api_secret = input("🔑 Enter your Kraken API Secret: ")

    # ✅ Encrypt and Save API Keys
    encrypted_data = {
        "api_key": cipher_suite.encrypt(api_key.encode()).decode(),
        "api_secret": cipher_suite.encrypt(api_secret.encode()).decode()
    }

    with open(CONFIG_FILE, "w") as file:
        json.dump(encrypted_data, file)

    return api_key, api_secret

# ✅ Load API Credentials
KRAKEN_API_KEY, KRAKEN_API_SECRET = get_api_credentials()

# ✅ Trading Settings
TRADE_PAIR = "BTC/USD"  
COPY_TRADE_AMOUNT = 0.01  
LEVERAGE = 2  
STOP_LOSS_PERCENT = 5  

# ✅ Whale Wallets for Copy Trading
WHALE_WALLETS = {
    "Bitcoin": [
        "3D2oetdNuZUqQHPJmcMDDHYoqkyNVsFk9r",
        "3Cbq7aT1tY8kMxWLbitaG7yT6bPbKChq64",
        "3Nxwenay9Z8Lc9JBiywExpnEFiLp6Afp8v",
        "1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF"
    ],
    "Ethereum": [
        "0x0A869d79a7052C7f1b55a8EbAbb5a8E3d0e88888",
        "0x3F5CE5FBFe3E9af3971dD833D26BA9b5C936f0bE",
        "0x28C6c06298d514Db089934071355E5743bf21d60"
    ]
}
