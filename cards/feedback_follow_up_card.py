def get_feedback_follow_up_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {"type": "TextBlock", "text": "🙌 Would you like to give more feedback or return home?", "wrap": True}
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Give More Feedback",
                "data": {"action": "give_feedback"}
            },
            {
                "type": "Action.Submit",
                "title": "Return Home 🏠",
                "data": {"action": "restart"}
            }
        ]
    }