def get_sizing_entry_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {
                "type": "TextBlock",
                "text": "📏 Product Sizing",
                "wrap": True,
                "weight": "Bolder",
                "size": "Medium"
            },
            {
                "type": "TextBlock",
                "text": "Select a product family to begin:",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "product_family",
                "style": "compact",
                "value": "",
                "choices": [
                    {"title": "--- SELECT AN OPTION ---", "value": ""},
                    {"title": "MR (Access Points)", "value": "MR"},
                    {"title": "MS (Switches)", "value": "MS"},
                    {"title": "MX (Security & SD-WAN)", "value": "MX"},
                    {"title": "MV (Cameras)", "value": "MV"}
                ]
            }
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Continue",
                "data": {"action": "sizing_select_family"}
            },
            {
                "type": "Action.Submit",
                "title": "Return to Home",
                "data": {"action": "restart"}
            }
        ]
    }