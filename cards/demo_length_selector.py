def get_demo_length_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.2",
        "body": [
            {
                "type": "TextBlock",
                "text": "⏱️ How much time do you have for the demo?",
                "weight": "Bolder",
                "size": "Medium"
            }
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "30 minutes (Quick Overview)",
                "data": {
                    "action": "select_demo_length",
                    "duration": "30"
                }
            },
            {
                "type": "Action.Submit",
                "title": "60 minutes (Deep Dive)",
                "data": {
                    "action": "select_demo_length",
                    "duration": "60"
                }
            },
            {
                "type": "Action.Submit",
                "title": "Return Home 🏠",
                "data": {
                    "action": "restart"
                }
            }
        ]
    }