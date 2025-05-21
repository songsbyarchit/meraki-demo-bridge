def get_mr_filter_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {"type": "TextBlock", "text": "🔍 Filter MR Access Points", "weight": "Bolder", "size": "Medium"},
            {"type": "TextBlock", "text": "Set any constraints (or leave blank to see all):", "wrap": True},

            # Wi-Fi Standard
            {
                "type": "Input.ChoiceSet",
                "id": "wifi_standard",
                "style": "compact",
                "value": "",
                "choices": [
                    {"title": "--- ANY ---", "value": ""},
                    {"title": "Wi-Fi 5", "value": "Wi-Fi 5"},
                    {"title": "Wi-Fi 6", "value": "Wi-Fi 6"},
                    {"title": "Wi-Fi 6E", "value": "Wi-Fi 6E"},
                    {"title": "Wi-Fi 7", "value": "Wi-Fi 7"},
                ]
            },

            # Radios
            {
                "type": "Input.ChoiceSet",
                "id": "radios",
                "style": "compact",
                "value": "",
                "choices": [
                    {"title": "--- ANY ---", "value": ""},
                    {"title": "2", "value": "2"},
                    {"title": "3", "value": "3"},
                ]
            },

            # Antenna Type
            {
                "type": "Input.ChoiceSet",
                "id": "antenna_type",
                "style": "compact",
                "value": "",
                "choices": [
                    {"title": "--- ANY ---", "value": ""},
                    {"title": "Internal", "value": "Internal"},
                    {"title": "External", "value": "External"},
                ]
            },

            # PoE
            {
                "type": "Input.ChoiceSet",
                "id": "poe",
                "style": "compact",
                "value": "",
                "choices": [
                    {"title": "--- ANY ---", "value": ""},
                    {"title": "Yes", "value": "true"},
                    {"title": "No", "value": "false"},
                ]
            },

            # Catalyst
            {
                "type": "Input.ChoiceSet",
                "id": "catalyst",
                "style": "compact",
                "value": "",
                "choices": [
                    {"title": "--- ANY ---", "value": ""},
                    {"title": "Yes", "value": "true"},
                    {"title": "No", "value": "false"},
                ]
            }
        ],
        "actions": [
            {"type": "Action.Submit", "title": "Find Matching Models", "data": {"action": "filter_mr_models"}},
            {"type": "Action.Submit", "title": "Return to Category Selection", "data": {"action": "sizing"}}
        ]
    }