def get_mr_filter_card(defaults=None):
    defaults = defaults or {}
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {
                "type": "TextBlock",
                "text": "🔍 Filter MR Access Points",
                "weight": "Bolder",
                "size": "Medium"
            },
            {
                "type": "TextBlock",
                "text": "Set at least one filter to narrow down MR models",
                "wrap": True
            },

            {
                "type": "TextBlock",
                "text": "Wi-Fi Standard",
                "weight": "Bolder",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "wifi_standard",
                "style": "compact",
                "value": defaults.get("wifi_standard", ""),
                "choices": [
                    {"title": "--- Select Wi-Fi Standard ---", "value": ""},
                    {"title": "Wi-Fi 5", "value": "wi-fi 5"},
                    {"title": "Wi-Fi 6", "value": "wi-fi 6"},
                    {"title": "Wi-Fi 6E", "value": "wi-fi 6e"},
                    {"title": "Wi-Fi 7", "value": "wi-fi 7"}
                ]
            },

            {
                "type": "TextBlock",
                "text": "Number of Radios",
                "weight": "Bolder",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "radios",
                "style": "compact",
                "value": defaults.get("radios", ""),
                "choices": [
                    {"title": "--- Show all ---", "value": ""},
                    {"title": "2", "value": "2"},
                    {"title": "3", "value": "3"}
                ]
            },

            {
                "type": "TextBlock",
                "text": "Antenna Type",
                "weight": "Bolder",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "antenna_type",
                "style": "compact",
                "value": defaults.get("antenna_type", ""),
                "choices": [
                    {"title": "--- Show all ---", "value": ""},
                    {"title": "Internal", "value": "internal"},
                    {"title": "External", "value": "external"}
                ]
            },

            {
                "type": "Input.Toggle",
                "id": "poe",
                "title": "Only show models with PoE support",
                "valueOn": "true",
                "valueOff": "false",
                "value": defaults.get("poe", "false")
            },

            {
                "type": "Input.Toggle",
                "id": "catalyst",
                "title": "Only show Catalyst models",
                "valueOn": "true",
                "valueOff": "false",
                "value": defaults.get("catalyst", "false")
            }
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Find Matching Models",
                "data": {"action": "filter_mr_models"}
            },
            {
                "type": "Action.Submit",
                "title": "Return to Category Selection",
                "data": {"action": "sizing"}
            }
        ]
    }