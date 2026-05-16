import requests

# =========================
# TELEGRAM CONFIG
# =========================
BOT_TOKEN = "8345659236:AAFfZH7zy33QS7crhfVJycL_2qWJm5EKCpc"
CHAT_ID = "5835490642"


# =========================
# SEND MESSAGE FUNCTION
# =========================
def send_telegram_message(message: str):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        payload = {
            "chat_id": CHAT_ID,
            "text": message,
            "parse_mode": "HTML"
        }

        response = requests.post(url, data=payload)

        if response.status_code != 200:
            print(f"[TELEGRAM ERROR] {response.text}")

    except Exception as e:
        print(f"[TELEGRAM EXCEPTION] {e}")
