import os
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # Consigue tu id con @userinfobot

def send_message(text: str):
    if not TELEGRAM_TOKEN or not CHAT_ID:
        raise RuntimeError("Faltan variables de entorno TELEGRAM_TOKEN y/o CHAT_ID.")
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    r = requests.post(url, json=payload, timeout=10)
    r.raise_for_status()
    print("✅ Mensaje enviado")

if __name__ == "__main__":
    send_message("🚀 Hola! El bot está funcionando en local 🎉")
