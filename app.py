from flask import Flask, request
from dotenv import load_dotenv
from cards.homepage import get_homepage_card
from cards.options_selector import get_options_selector_card_with_defaults
from utils.webex import send_card
import os, requests, sys
from cards.demo_length_selector import get_demo_length_card
from cards.demo_done_selector     import get_demo_done_card
from utils.demo_loader            import get_demo_flow
from utils.label_maps import audience_map, vertical_map, product_map

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
user_contexts = {}

def get_user_context(user_id):
    return user_contexts.get(user_id, {})

def set_user_context(user_id, key, value):
    if user_id not in user_contexts:
        user_contexts[user_id] = {}
    user_contexts[user_id][key] = value

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
            context = get_user_context(room_id)
            if context.get("audience") and context.get("vertical") and context.get("product_line"):
                msg = f"""You last selected:

                **• Audience:** {audience_map.get(context['audience'], context['audience'])}  
                **• Vertical:** {vertical_map.get(context['vertical'], context['vertical'])}  
                **• Product Line:** {product_map.get(context['product_line'], context['product_line'])}

                Would you like to change these?"""
                send_card(room_id, {
                    "type": "AdaptiveCard",
                    "version": "1.3",
                    "body": [{"type": "TextBlock", "text": msg, "wrap": True}],
                    "actions": [
                        {"type": "Action.Submit", "title": "Change", "data": {"action": "change_options"}},
                        {"type": "Action.Submit", "title": "Continue", "data": {"action": "use_previous_options"}}
                    ]
                }, markdown="Previous selections found.")
            else:
                send_card(
                    room_id,
                    get_options_selector_card_with_defaults(audience="", vertical="", product_line=""),
                    markdown="Select your options"
                )
        elif action == "use_previous_options":
            context = get_user_context(room_id)
            room_state[room_id] = {
                "stage": "awaiting_demo_length",
                "audience": context["audience"],
                "vertical": context["vertical"],
                "product_line": context["product_line"]
            }
            send_card(room_id, get_demo_length_card(), markdown="Using your last selections. How much time do you have for the demo?")

        elif action == "change_options":
            context = get_user_context(room_id)
            send_card(
                room_id,
                get_options_selector_card_with_defaults(
                    audience=context.get("audience"),
                    vertical=context.get("vertical"),
                    product_line=context.get("product_line")
                ),
                markdown="No problem! Let’s pick new options."
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
                    "markdown": f"\n\n⚠️ You still have not selected: {', '.join(missing)}.\n🔁 Please select a value, then press 'Continue' again.\n\n"
                }
                )
                # resend the card
                send_card(
                    room_id,
                    get_options_selector_card_with_defaults(
                        audience=audience or "",
                        vertical=vertical or "",
                        product_line=product_line or ""
                    ),
                    markdown=""
                )
            else:
                room_state[room_id] = {
                    "stage": "awaiting_demo_length",
                    "audience": audience,
                    "vertical": vertical,
                    "product_line": product_line
                }
                set_user_context(room_id, "audience", audience)
                set_user_context(room_id, "vertical", vertical)
                set_user_context(room_id, "product_line", product_line)
                send_card(room_id, get_demo_length_card(), markdown="Got it! Now, choose how much time you have for the demo.")
        elif action == "select_demo_length":
            inputs = action_detail.get("inputs", {})
            length = inputs.get("duration")
            state = room_state.get(room_id, {})
            script = get_demo_flow(
                state["audience"],
                state["vertical"],
                state["product_line"],
                length
            )
            requests.post(
                "https://webexapis.com/v1/messages",
                headers={
                    "Authorization": f"Bearer {WEBEX_TOKEN}",
                    "Content-Type": "application/json"
                },
                json={
                    "roomId": room_id,
                    "markdown": script
                }
            )
            send_card(room_id, get_demo_done_card(), markdown="What would you like to do next?")
        elif action == "restart":
            room_state.pop(room_id, None)
            send_card(room_id, get_homepage_card(), markdown="Restarted")
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5099)