from flask import Flask
import requests
import os
import time
import threading

app = Flask(__name__)

# URL of the service you want to keep alive
TARGET_URL = "www.insearchoutdoors.com"

@app.route("/")
def health():
    """Health check endpoint for Render"""
    return {"status": "ok", "message": "Keep-alive service running!"}, 200

def ping_service():
    """Background thread that pings your service every 10 minutes"""
    while True:
        try:
            resp = requests.get(TARGET_URL, timeout=10)
            print(f"Pinged {TARGET_URL}, status: {resp.status_code}")
        except Exception as e:
            print(f"Ping failed: {e}")
        time.sleep(300)  # 600s = 10 min

def start_pinger():
    thread = threading.Thread(target=ping_service, daemon=True)
    thread.start()

if __name__ == "__main__":
    # Start background pinger
    start_pinger()

    # Run a small web service (Render needs this)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
