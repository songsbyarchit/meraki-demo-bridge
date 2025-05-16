def get_case_study_card(matches):
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {"type": "TextBlock", "text": "Top 3 Case Studies", "weight": "Bolder", "size": "Medium"},
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": match["title"],
                "data": {"action": "case_study_selected", "index": i}
            }
            for i, match in enumerate(matches)
        ] + [
            {
                "type": "Action.Submit",
                "title": "Return Home",
                "data": {"action": "restart"}
            }
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
    }