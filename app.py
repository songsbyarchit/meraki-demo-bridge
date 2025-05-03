from flask import Flask, request
from dotenv import load_dotenv
from cards.homepage import get_homepage_card
from cards.options_selector import get_options_selector_card
from cards.summary import build_summary_card
from utils.webex import send_card
from utils.salesforce import get_customer_purchases
from utils.openai_client import summarise_customer
import os, requests, sys

load_dotenv()
WEBEX_TOKEN = os.getenv("WEBEX_BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if not WEBEX_TOKEN or not OPENAI_KEY:
    print("missing token")
    sys.exit(1)

bot_info = requests.get("https://webexapis.com/v1/people/me",
                        headers={"Authorization": f"Bearer {WEBEX_TOKEN}"}).json()
BOT_ID = bot_info["id"]

app = Flask(__name__)
room_state = {}

@app.route("/messages", methods=["POST"])
def messages():
    data = request.json
    print("⟳ Incoming webhook:", data)
    print("⚙️  BOT_ID is", BOT_ID)
    if data["resource"] == "messages" and data["event"] == "created":
        room_id = data["data"]["roomId"]
        sender = data["data"]["personId"]
        if sender == BOT_ID:
            return "OK"
        stage = room_state.get(room_id, {}).get("stage")
        if stage == "awaiting_customer":
            msg_id = data["data"]["id"]
            text = requests.get(f"https://webexapis.com/v1/messages/{msg_id}",
                                headers={"Authorization": f"Bearer {WEBEX_TOKEN}"}).json().get("text", "")
            vertical = room_state[room_id]["vertical"]
            purchases = get_customer_purchases(text)
            summary = summarise_customer(purchases, vertical)
            send_card(room_id, build_summary_card(text, summary), markdown=summary)
            room_state.pop(room_id, None)
        elif stage == "awaiting_customer_deep_dive":
            msg_id = data["data"]["id"]
            text = requests.get(
                f"https://webexapis.com/v1/messages/{msg_id}",
                headers={"Authorization": f"Bearer {WEBEX_TOKEN}"}
            ).json().get("text", "")
            room_state.pop(room_id, None)
            requests.post(
                "https://webexapis.com/v1/messages",
                headers={
                    "Authorization": f"Bearer {WEBEX_TOKEN}",
                    "Content-Type": "application/json"
                },
                json={
                    "roomId": room_id,
                    "markdown": f"📊 Deep dive coming soon for **{text}**!"
                }
            )
        else:
            room_state.pop(room_id, None)
            send_card(room_id, get_homepage_card(), markdown="Meraki Demo Bridge")
    elif data["resource"] == "attachmentActions" and data["event"] == "created":
        room_id = data["data"]["roomId"]
        action_id = data["data"]["id"]
        action_detail = requests.get(f"https://webexapis.com/v1/attachment/actions/{action_id}",
                                     headers={"Authorization": f"Bearer {WEBEX_TOKEN}"}).json()
        action = action_detail.get("inputs", {}).get("action")
        if action == "start_demo":
            send_card(room_id, get_options_selector_card(), markdown="Select your options")
        elif action == "start_customer_dive":
            room_state[room_id] = {"stage": "awaiting_customer_deep_dive"}
            requests.post(
                "https://webexapis.com/v1/messages",
                headers={
                    "Authorization": f"Bearer {WEBEX_TOKEN}",
                    "Content-Type": "application/json"
                },
                json={
                    "roomId": room_id,
                    "markdown": "Type the customer name you'd like to explore"
                }
            )
        elif action == "select_options":
            inputs = action_detail.get("inputs", {})
            audience     = inputs.get("audience")
            vertical     = inputs.get("vertical")
            product_line = inputs.get("product_line")
            missing = []
            if audience == "":      missing.append("audience")
            if vertical == "":      missing.append("vertical")
            if product_line == "":  missing.append("product line")
            if missing:
                # send plain‑text warning
                requests.post(
                "https://webexapis.com/v1/messages",
                headers={
                    "Authorization": f"Bearer {WEBEX_TOKEN}",
                    "Content-Type": "application/json"
                },
                json={
                    "roomId": room_id,
                    "markdown": f"\n\n⚠️ You still have not selected: {', '.join(missing)}...\n🔁 Please select a value, then press 'Continue' again.\n\n"
                }
                )
                # resend the card
                send_card(
                room_id,
                get_options_selector_card(),
                markdown=""
                )
            else:
                room_state[room_id] = {
                    "stage": "awaiting_customer",
                    "audience": audience,
                    "vertical": vertical,
                    "product_line": product_line
                }
                requests.post(
                    "https://webexapis.com/v1/messages",
                    headers={"Authorization": f"Bearer {WEBEX_TOKEN}",
                             "Content-Type": "application/json"},
                    json={"roomId": room_id,
                          "markdown": "Type the customer name"}
                )
        elif action == "restart":
            room_state.pop(room_id, None)
            send_card(room_id, get_homepage_card(), markdown="Restarted")
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5099)