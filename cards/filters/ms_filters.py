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
                "text": "Set at least one filter to narrow down MS models:",
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "PoE Support",
                "wrap": True,
                "weight": "Bolder"
            },
            {
                "type": "Input.ChoiceSet",
                "id": "poe_support",
                "style": "compact",
                "value": "",
                "choices": [
                    {"title": "--- Show all ---", "value": ""},
                    {"title": "PoE", "value": "poe"},
                    {"title": "PoE+", "value": "poe+"},
                    {"title": "UPOE", "value": "upoe"},
                    {"title": "UPOE+", "value": "upoe+"}
                ]
            },
            {
                "type": "TextBlock",
                "text": "Routing Capabilities",
                "wrap": True,
                "weight": "Bolder"
            },
            {
                "type": "Input.ChoiceSet",
                "id": "routing",
                "style": "compact",
                "value": "",
                "choices": [
                    {"title": "--- Select Routing ---", "value": ""},
                    {"title": "Layer 2 only", "value": "layer 2 only"},
                    {"title": "DHCP Relay", "value": "dhcp relay"},
                    {"title": "Dynamic Routing", "value": "dynamic routing"}
                ]
            },
            {
                "type": "TextBlock",
                "text": "1G Port Count",
                "wrap": True,
                "weight": "Bolder"
            },
            {
                "type": "Input.ChoiceSet",
                "id": "min_ports_1gbe",
                "style": "compact",
                "value": "",
                "choices": [
                    {"title": "--- Show all ---", "value": ""},
                    {"title": "8+", "value": "8"},
                    {"title": "16+", "value": "16"},
                    {"title": "24+", "value": "24"},
                    {"title": "48+", "value": "48"}
                ]
            },
            {
                "type": "TextBlock",
                "text": "mGig Port Count",
                "wrap": True,
                "weight": "Bolder"
            },
            {
                "type": "Input.ChoiceSet",
                "id": "min_ports_mgig",
                "style": "compact",
                "value": "",
                "choices": [
                    {"title": "--- Show all ---", "value": ""},
                    {"title": "1+", "value": "1"},
                    {"title": "2+", "value": "2"},
                    {"title": "4+", "value": "4"}
                ]
            },
            {
                "type": "Input.Toggle",
                "id": "stackable",
                "title": "Only show stackable models",
                "valueOn": "true",
                "valueOff": "false"
            },
            {
                "type": "Input.Toggle",
                "id": "catalyst",
                "title": "Only show Catalyst models",
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