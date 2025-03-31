from fastapi import FastAPI, Request
import os
import requests

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")

TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()

    message = data.get("message")
    if not message:
        return {"ok": True}

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    if text == "/start":
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": "🎬 Benvenuto nel Cineforum Kossuth! Vuoi aprire la Web App?",
            "reply_markup": {
                "keyboard": [[
                    {
                        "text": "Apri Web App",
                        "web_app": { "url": WEB_APP_URL }
                    }
                ]],
                "resize_keyboard": True
            }
        })

    return {"ok": True}
