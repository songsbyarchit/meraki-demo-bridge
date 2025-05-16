def get_case_study_card(matches):
    return {
        "type": "AdaptiveCard",
        "version": "1.2",
        "body": [
            {"type": "TextBlock", "text": "Top 3 Case Studies", "weight": "Bolder", "size": "Medium"},
        ] + [
            {
                "type": "TextBlock",
                "text": f"{i+1}. {match['url']}",
                "wrap": True
            }
            for i, match in enumerate(matches)
        ],
        "actions": [
            {
                "type": "Action.OpenUrl",
                "title": "View Full Case Study",
                "url": match["url"]
            }
            for match in matches
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
    }