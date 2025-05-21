def get_mx_filter_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {
                "type": "TextBlock",
                "text": "🛡️ MX Appliance Filters",
                "wrap": True,
                "weight": "Bolder",
                "size": "Medium"
            },
            {
                "type": "TextBlock",
                "text": "Set filters to narrow down MX models:",
                "wrap": True
            },
            {
                "type": "Input.Toggle",
                "id": "has_cellular",
                "title": "Must support Cellular?",
                "valueOn": "true",
                "valueOff": "false"
            },
            {
                "type": "Input.Toggle",
                "id": "has_wireless",
                "title": "Must support Wireless?",
                "valueOn": "true",
                "valueOff": "false"
            }
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Show Matching Models",
                "data": {"action": "filter_mx_models"}
            },
            {
                "type": "Action.Submit",
                "title": "Back",
                "data": {"action": "sizing"}
            }
        ]
    }