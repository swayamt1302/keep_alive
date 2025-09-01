import requests
import time

URL = "https://www.insearchoutdoors.com"

def ping_site():
    try:
        response = requests.get(URL, timeout=10)
        print(f"Pinged {URL} - Status: {response.status_code}")
    except Exception as e:
        print(f"Failed to ping {URL}: {e}")

if __name__ == "__main__":
    while True:
        ping_site()
        time.sleep(300)  # every 5 minutes
