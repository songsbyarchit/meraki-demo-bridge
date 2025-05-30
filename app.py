from flask import Flask, request
from dotenv import load_dotenv
from cards.homepage import get_homepage_card
from cards.feedback_card import get_feedback_card
from cards.options_selector import get_options_selector_card_with_defaults
from cards.case_study_card import get_case_study_card
from utils.webex import send_card
import os, requests, sys
from cards.demo_length_selector import get_demo_length_card
from cards.demo_done_selector     import get_demo_done_card
from cards.case_study_follow_up import get_follow_up_card
from utils.demo_loader            import get_demo_flow
from utils.label_maps import audience_map, vertical_map, product_map
from cards.sizing_selector import get_sizing_entry_card
from cards.filters.mr_filters import get_mr_filter_card
from cards.filters.ms_filters import get_ms_filter_card
from cards.filters.mx_filters import get_mx_filter_card
from cards.filters.mv_filters import get_mv_filter_card
from cards.sizing_follow_up import get_sizing_follow_up_card
from utils.filter_engine import filter_mx_models, filter_mr_models, filter_ms_models, filter_mv_models
from cards.feedback_follow_up_card import get_feedback_follow_up_card
from models.feedback import Feedback
from database import SessionLocal
from datetime import datetime

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
    db = SessionLocal()
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
            room_state[room_id] = {"mode": "demo"}
            context = get_user_context(room_id)
            if context.get("audience") and context.get("vertical") and context.get("product_line"):
                msg = f"""You last selected:

                **• Audience:** {audience_map.get(context['audience'], context['audience'])}  
                **• Vertical:** {vertical_map.get(context['vertical'], context['vertical'])}  
                **• Product Line:** {product_map.get(context['product_line'], context['product_line'])}

                Would you like to change any of these?"""
                send_card(room_id, {
                    "type": "AdaptiveCard",
                    "version": "1.3",
                    "body": [{"type": "TextBlock", "text": msg, "wrap": True}],
                    "actions": [
                        {"type": "Action.Submit", "title": "Change", "data": {"action": "change_options"}},
                        {"type": "Action.Submit", "title": "Continue", "data": {"action": "use_previous_options"}},
                        {"type": "Action.Submit", "title": "Return Home 🏠", "data": {"action": "restart"}}
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
        elif action == "use_previous_case_study_options":
            context = get_user_context(room_id)
            vertical = context.get("vertical")
            product_line = context.get("product_line")

            from utils.static_case_study_lookup import get_static_case_studies
            matches = get_static_case_studies(vertical, product_line)
            set_user_context(room_id, "last_top3_matches", matches)
            send_card(room_id, get_case_study_card(matches), markdown="📚 Here are relevant case studies based on your selection.")
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
                set_user_context(room_id, "audience", audience)
                set_user_context(room_id, "vertical", vertical)
                set_user_context(room_id, "product_line", product_line)

                mode = room_state.get(room_id, {}).get("mode", "demo")

                if mode == "case_study":
                    from utils.static_case_study_lookup import get_static_case_studies
                    matches = get_static_case_studies(vertical, product_line)
                    set_user_context(room_id, "last_top3_matches", matches)
                    send_card(room_id, get_case_study_card(matches), markdown="📚 Here are relevant case studies based on your selection.")
                else:
                    room_state[room_id] = {
                        "stage": "awaiting_demo_length",
                        "audience": audience,
                        "vertical": vertical,
                        "product_line": product_line
                    }
                    send_card(room_id, get_demo_length_card(), markdown="Got it! Now, choose how much time you have for the demo.")
        elif action == "case_study_selected":
            index = int(action_detail.get("inputs", {}).get("index", 0))
            context = get_user_context(room_id)
            vertical = context.get("vertical")
            product_line = context.get("product_line")

            from utils.static_case_study_lookup import get_static_case_studies
            from cards.case_study_card import get_case_study_detail_card

            matches = get_static_case_studies(vertical, product_line)
            set_user_context(room_id, "last_top3_matches", matches)
            if index < len(matches):
                case = matches[index]
                send_card(room_id, get_case_study_detail_card(case, index), markdown=f"🔍 Here's more info about **{case['title']}**.")
            else:
                send_card(room_id, get_homepage_card(), markdown="⚠️ Could not find that case study. Returning home.")
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
        elif action == "show_summary":
            context = get_user_context(room_id)
            vertical = context.get("vertical")
            product_line = context.get("product_line")
            from utils.static_case_study_lookup import get_static_case_studies
            matches = get_static_case_studies(vertical, product_line)
            set_user_context(room_id, "last_top3_matches", matches)
            index = int(action_detail.get("inputs", {}).get("index", 0))  # fallback index
            if index < len(matches):
                summary = matches[index].get("summary", "⚠️ No summary available.")

                # First send plain summary text
                requests.post(
                    "https://webexapis.com/v1/messages",
                    headers={
                        "Authorization": f"Bearer {WEBEX_TOKEN}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "roomId": room_id,
                        "markdown": f"📝 **Summary:**\n\n{summary}"
                    }
                )

                # Then send a follow-up card
                send_card(room_id, get_follow_up_card(), markdown="ℹ️ Please choose what to do next:")
            else:
                send_card(room_id, get_homepage_card(), markdown="⚠️ Summary not found. Returning home.")
        elif action == "restart":
            room_state.pop(room_id, None)
            send_card(room_id, get_homepage_card(), markdown="Restarted")
        elif action == "show_top_3_again":
            matches = get_user_context(room_id).get("last_top3_matches", [])
            if matches:
                text_lines = [
                    f"**Top 3 Case Studies:**\n"
                ]
                for i, match in enumerate(matches[:3]):
                    text_lines.append(f"{i+1}. {match['title']} — Score: {match['score']:.2f}")
                markdown_text = "\n".join(text_lines)

                # Send plain text top 3 list
                send_card(
                    room_id,
                    get_case_study_card(matches),
                    markdown="📚 Here are your top 3 recommended case studies again."
                )

                # Send follow-up card with buttons
                send_card(room_id, get_follow_up_card(), markdown="ℹ️ Please choose what to do next:")
        elif action == "sizing":
            send_card(room_id, get_sizing_entry_card(), markdown="📏 Let’s begin the sizing process. Select a product family to begin.")
        elif action == "sizing_select_family":
            selected_family = action_detail.get("inputs", {}).get("product_family", "")
            if not selected_family:
                requests.post(
                    "https://webexapis.com/v1/messages",
                    headers={
                        "Authorization": f"Bearer {WEBEX_TOKEN}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "roomId": room_id,
                        "markdown": "⚠️ Please select a product family before continuing."
                    }
                )
                send_card(room_id, get_sizing_entry_card(), markdown="🔁 Please choose a valid option to continue.")
                return "OK"


            set_user_context(room_id, "sizing_family", selected_family)
            room_state[room_id] = {"stage": "awaiting_sizing_filters", "sizing_family": selected_family}

            context = get_user_context(room_id)
            if selected_family == "MX":
                defaults = get_user_context(room_id).get("last_filters_MX", {})
                send_card(room_id, get_mx_filter_card(defaults), markdown="🔍 Let’s narrow down your MX options.")
            elif selected_family == "MR":
                defaults = get_user_context(room_id).get("last_filters_MR", {})
                send_card(room_id, get_mr_filter_card(defaults), markdown="🔍 Let’s narrow down your MR options.")
            elif selected_family == "MS":
                defaults = get_user_context(room_id).get("last_filters_MS", {})
                send_card(room_id, get_ms_filter_card(defaults), markdown="🔍 Let’s narrow down your MS options.")
            elif selected_family == "MV":
                defaults = get_user_context(room_id).get("last_filters_MV", {})
                send_card(room_id, get_mv_filter_card(defaults), markdown="🔍 Let’s narrow down your MV options.")

                
        elif action == "filter_mx_models":
            filters = action_detail.get("inputs", {})
            set_user_context(room_id, "last_filters_MX", filters)
            results, error = filter_mx_models(filters)
            if error:
                requests.post(
                    "https://webexapis.com/v1/messages",
                    headers={
                        "Authorization": f"Bearer {WEBEX_TOKEN}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "roomId": room_id,
                        "markdown": "⚠️ Please apply at least one MX filter and press **Show Matching Models** on the card above again."
                    }
                )
            else:
                formatted = "\n".join(f"- {r.model}" for r in results) or "No models matched."
                requests.post(
                    "https://webexapis.com/v1/messages",
                    headers={
                        "Authorization": f"Bearer {WEBEX_TOKEN}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "roomId": room_id,
                        "markdown": f"🔎 **Matching MX Models:**\n\n{formatted}"
                    }
                )
                send_card(room_id, get_sizing_follow_up_card("MX"), markdown="✅ You’ve completed MX sizing.")

        elif action == "filter_mr_models":
            filters = action_detail.get("inputs", {})
            set_user_context(room_id, "last_filters_MR", filters)
            results, error = filter_mr_models(filters)
            if error:
                requests.post(
                    "https://webexapis.com/v1/messages",
                    headers={
                        "Authorization": f"Bearer {WEBEX_TOKEN}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "roomId": room_id,
                        "markdown": "⚠️ Please apply at least one MR filter and press **Show Matching Models** on the card above again."
                    }
                )
            else:
                formatted = "\n".join(f"- {r.model}" for r in results) or "No models matched."
                requests.post(
                    "https://webexapis.com/v1/messages",
                    headers={
                        "Authorization": f"Bearer {WEBEX_TOKEN}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "roomId": room_id,
                        "markdown": f"🔎 **Matching MR Models:**\n\n{formatted}"
                    }
                )
                send_card(room_id, get_sizing_follow_up_card("MR"), markdown="✅ You’ve completed MX sizing.")


        elif action == "filter_ms_models":
            filters = action_detail.get("inputs", {})
            set_user_context(room_id, "last_filters_MS", filters)
            results, error = filter_ms_models(filters)
            if error:
                requests.post(
                    "https://webexapis.com/v1/messages",
                    headers={
                        "Authorization": f"Bearer {WEBEX_TOKEN}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "roomId": room_id,
                        "markdown": "⚠️ Please apply at least one MS filter and press **Show Matching Models** on the card above again."
                    }
                )
            else:
                formatted = "\n".join(f"- {r.model}" for r in results) or "No models matched."
                requests.post(
                    "https://webexapis.com/v1/messages",
                    headers={
                        "Authorization": f"Bearer {WEBEX_TOKEN}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "roomId": room_id,
                        "markdown": f"🔎 **Matching MS Models:**\n\n{formatted}"
                    }
                )
                send_card(room_id, get_sizing_follow_up_card("MS"), markdown="✅ You’ve completed MX sizing.")


        elif action == "filter_mv_models":
            filters = action_detail.get("inputs", {})
            set_user_context(room_id, "last_filters_MV", filters)
            results, error = filter_mv_models(filters)
            if error:
                requests.post(
                    "https://webexapis.com/v1/messages",
                    headers={
                        "Authorization": f"Bearer {WEBEX_TOKEN}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "roomId": room_id,
                        "markdown": "⚠️ Please apply at least one MV filter and press **Show Matching Models** on the card above again."
                    }
                )
            else:
                formatted = "\n".join(f"- {r.model}" for r in results) or "No models matched."
                requests.post(
                    "https://webexapis.com/v1/messages",
                    headers={
                        "Authorization": f"Bearer {WEBEX_TOKEN}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "roomId": room_id,
                        "markdown": f"🔎 **Matching MV Models:**\n\n{formatted}"
                    }
                )
                send_card(room_id, get_sizing_follow_up_card("MV"), markdown="✅ You’ve completed MX sizing.")


        elif action == "case_study":
            room_state[room_id] = {"mode": "case_study"}
            context = get_user_context(room_id)
            if context.get("audience") and context.get("vertical") and context.get("product_line"):
                msg = f"""You last selected:

                **• Audience:** {audience_map.get(context['audience'], context['audience'])}  
                **• Vertical:** {vertical_map.get(context['vertical'], context['vertical'])}  
                **• Product Line:** {product_map.get(context['product_line'], context['product_line'])}

                Would you like to change any of these?"""
                send_card(room_id, {
                    "type": "AdaptiveCard",
                    "version": "1.3",
                    "body": [{"type": "TextBlock", "text": msg, "wrap": True}],
                    "actions": [
                        {"type": "Action.Submit", "title": "Change", "data": {"action": "change_options"}},
                        {"type": "Action.Submit", "title": "Continue", "data": {"action": "use_previous_case_study_options"}}
                    ]
                }, markdown="Previous selections found.")
            else:
                send_card(
                    room_id,
                    get_options_selector_card_with_defaults(audience="", vertical="", product_line=""),
                    markdown="Select your options"
                )
        elif action == "submit_feedback":
            inputs = action_detail.get("inputs", {})

            def is_blank(value):
                return value in ("", None)

            required_fields = {
                "role": "role",
                "audience": "audience",
                "product_line": "product line",
                "industry": "industry",
                "used_tool": "tool used",
                "usual_minutes": "time without tool",
                "bridge_minutes": "time using tool",
                "quality_rating": "quality rating"
            }

            missing = [
                label for key, label in required_fields.items()
                if is_blank(inputs.get(key))
            ]

            # Save current inputs to re-populate the form
            user_context = {
                "role": inputs.get("role", ""),
                "audience": inputs.get("audience", ""),
                "product_line": inputs.get("product_line", ""),
                "industry": inputs.get("industry", ""),
                "used_tool": inputs.get("used_tool", ""),
                "usual_minutes": inputs.get("usual_minutes", ""),
                "bridge_minutes": inputs.get("bridge_minutes", ""),
                "quality_rating": inputs.get("quality_rating", ""),
                "extra_feedback": inputs.get("extra_feedback", "")
            }
            for k, v in user_context.items():
                set_user_context(room_id, k, v)

            if missing:
                requests.post(
                    "https://webexapis.com/v1/messages",
                    headers={
                        "Authorization": f"Bearer {WEBEX_TOKEN}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "roomId": room_id,
                        "markdown": f"⚠️ Please select a value for: {', '.join(missing)}.\n\n🔁 Update your selections and press **Submit Feedback** again."
                    }
                )
                send_card(room_id, get_feedback_card(defaults=user_context), markdown="Please review your selections.")
                return "OK"

            # Save feedback to DB
            new_entry = Feedback(
                room_id         = room_id,
                role            = inputs.get("role"),
                audience        = inputs.get("audience"),
                product_line    = inputs.get("product_line"),
                industry        = inputs.get("industry"),
                tool_used       = inputs.get("used_tool"),
                usual_minutes   = int(inputs.get("usual_minutes") or 0),
                bridge_minutes  = int(inputs.get("bridge_minutes") or 0),
                quality_rating  = int(inputs.get("quality_rating") or 0),
                extra_feedback  = inputs.get("extra_feedback", ""),
                percentage_time_saved = round(
                    (int(inputs.get("usual_minutes") or 0) - int(inputs.get("bridge_minutes") or 0)) 
                    / max(int(inputs.get("usual_minutes") or 1), 1) * 100
                )
            )
            db.add(new_entry)
            db.commit()

            from utils.google_sheets import push_feedback_to_sheets
            try:
                push_feedback_to_sheets({
                    "room_id": room_id,
                    "tool_used": inputs.get("used_tool"),
                    "usual_minutes": int(inputs.get("usual_minutes") or 0),
                    "bridge_minutes": int(inputs.get("bridge_minutes") or 0),
                    "percentage_time_saved": round(
                        (int(inputs.get("usual_minutes") or 0) - int(inputs.get("bridge_minutes") or 0)) 
                        / max(int(inputs.get("usual_minutes") or 1), 1) * 100
                    ),
                    "quality_rating": int(inputs.get("quality_rating") or 0),
                    "extra_feedback": inputs.get("extra_feedback", ""),
                    "role": inputs.get("role", ""),
                    "audience": inputs.get("audience", ""),
                    "product_line": inputs.get("product_line", ""),
                    "industry": inputs.get("industry", "")
                })
            except Exception as e:
                print(f"⚠️ Failed to push to Google Sheets: {e}")

            requests.post(
                "https://webexapis.com/v1/messages",
                headers={
                    "Authorization": f"Bearer {WEBEX_TOKEN}",
                    "Content-Type": "application/json"
                },
                json={
                    "roomId": room_id,
                    "markdown": "✅ Thanks for your feedback! It’s been saved to our database.\nOur developers take all feedback into consideration for future versions!"
                }
            )
            send_card(room_id, get_feedback_follow_up_card(), markdown="What would you like to do next?")
        elif action == "give_feedback":
            room_state[room_id] = {"stage": "giving_feedback"}
            previous = get_user_context(room_id)
            send_card(room_id, get_feedback_card(defaults=previous), markdown="📝 We'd love your feedback.")
        else:
            send_card(room_id, get_homepage_card(), markdown="⚠️ Couldn’t find your previous top 3. Returning home.")
    return "OK"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5099)