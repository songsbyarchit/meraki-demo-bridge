def create_card(title: str, text: str, buttons: list[dict]) -> dict:
    return {
        "type": "AdaptiveCard",
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2",
        "body": [
            {"type": "TextBlock", "size": "Large", "weight": "Bolder", "text": title},
            {"type": "TextBlock", "text": text, "wrap": True}
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": btn["title"],
                "data": {"action": btn["value"]}
            }
            for btn in buttons
        ]
    }