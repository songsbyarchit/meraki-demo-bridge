# cards/follow_up_card.py

def get_follow_up_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {"type": "TextBlock", "text": "What would you like to do next?", "weight": "Bolder", "size": "Medium", "wrap": True}
        ],
        "actions": [
            {"type": "Action.Submit", "title": "Return to Top 3 List", "data": {"action": "show_top_3_again"}},
            {"type": "Action.Submit", "title": "Return Home", "data": {"action": "restart"}}
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
    }