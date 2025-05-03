def get_vertical_selector_card():
    choices = [
        {"title": "Healthcare", "value": "healthcare"},
        {"title": "Education", "value": "education"},
        {"title": "Manufacturing", "value": "manufacturing"},
        {"title": "Retail", "value": "retail"},
        {"title": "Government", "value": "government"}
    ]
    return {
        "type": "AdaptiveCard",
        "version": "1.2",
        "body": [
            {"type": "TextBlock", "text": "Select vertical", "weight": "Bolder", "size": "Medium"},
            {"type": "Input.ChoiceSet", "id": "vertical", "style": "compact", "choices": choices}
        ],
        "actions": [
            {"type": "Action.Submit", "title": "Continue", "data": {"action": "select_vertical"}},
            {"type": "Action.Submit", "title": "Restart", "data": {"action": "restart"}}
        ]
    }