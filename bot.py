import os
import requests
from flask import Flask, request

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # Consigue tu id con @userinfobot
app = Flask(__name__)

def send_message(text: str):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        raise RuntimeError("Faltan variables de entorno TELEGRAM_TOKEN y/o CHAT_ID.")
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    r = requests.post(url, json=payload, timeout=10)
    r.raise_for_status()
    print("✅ Mensaje enviado")

@app.route("/github", methods=["POST"])
def github_webhook():
    data = request.json
    if "pusher" in data:
        repo = data["repository"]["name"]
        pusher = data["pusher"]["name"]
        branch = data["ref"].split("/")[-1]
        send_message(f"📢 Repo: {repo}\n👤 Push por: {pusher}\n🌿 Rama: {branch}")
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

