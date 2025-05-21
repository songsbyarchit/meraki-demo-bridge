def get_mv_filter_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {
                "type": "TextBlock",
                "text": "📷 MV Camera Filters",
                "wrap": True,
                "weight": "Bolder",
                "size": "Medium"
            },
            {
                "type": "TextBlock",
                "text": "Set filters to narrow down MV models:",
                "wrap": True
            },
            {
                "type": "Input.Toggle",
                "id": "wireless",
                "title": "Must be Wireless?",
                "valueOn": "true",
                "valueOff": "false"
            },
            {
                "type": "Input.Toggle",
                "id": "onboard_storage",
                "title": "Require onboard storage?",
                "valueOn": "true",
                "valueOff": "false"
            }
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Show Matching Models",
                "data": {"action": "filter_mv_models"}
            },
            {
                "type": "Action.Submit",
                "title": "Back",
                "data": {"action": "sizing"}
            }
        ]
    }