from dotenv import load_dotenv
import requests, os
load_dotenv()
token = os.getenv("WEBEX_BOT_TOKEN")

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def send_card(room_id, card_json, markdown=""):
    payload = {
        "roomId": room_id,
        "markdown": markdown,
        "attachments": [{
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": card_json
        }]
    }
    r = requests.post("https://webexapis.com/v1/messages",
                      headers=headers,
                      json=payload)
    print("⇢ send_card →", r.status_code, r.text)
    return r