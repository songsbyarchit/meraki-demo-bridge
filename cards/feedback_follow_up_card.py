def get_feedback_follow_up_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.2",
        "body": [
            {"type": "TextBlock", "text": "✅ Feedback saved!", "weight": "Bolder", "size": "Medium"},
            {"type": "TextBlock", "text": "Would you like to give more feedback or return to the homepage?"}
        ],
        "actions": [
            {"type": "Action.Submit", "title": "Give more feedback", "data": {"action": "give_feedback"}},
            {"type": "Action.Submit", "title": "Return home", "data": {"action": "restart"}}
        ]
    }