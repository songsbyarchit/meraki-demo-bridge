def get_ms_filter_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {
                "type": "TextBlock",
                "text": "🔌 MS Switch Filters",
                "wrap": True,
                "weight": "Bolder",
                "size": "Medium"
            },
            {
                "type": "TextBlock",
                "text": "Set filters to narrow down MS models:",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "poe_support",
                "style": "compact",
                "choices": [
                    {"title": "PoE", "value": "PoE"},
                    {"title": "PoE+", "value": "PoE+"},
                    {"title": "UPOE", "value": "UPOE"},
                    {"title": "UPOE+", "value": "UPOE+"},
                ]
            },
            {
                "type": "Input.Toggle",
                "id": "catalyst",
                "title": "Catalyst only",
                "valueOn": "true",
                "valueOff": "false"
            }
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Show Matching Models",
                "data": {"action": "filter_ms_models"}
            },
            {
                "type": "Action.Submit",
                "title": "Back",
                "data": {"action": "sizing"}
            }
        ]
    }