def get_case_study_card(matches):
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {"type": "TextBlock", "text": "Recommended Case Studies", "weight": "Bolder", "size": "Medium"},
            {"type": "TextBlock", "text": "Here are the top 3 case studies most relevant to the vertical and product line you've selected.", "wrap": True},
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
                "title": "Return Home 🏠",
                "data": {"action": "restart"}
            }
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
    }

def get_case_study_detail_card(case, index):
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {"type": "TextBlock", "text": f"You selected: {case['title']}", "weight": "Bolder", "size": "Medium"},
        ],
        "actions": [
            {
                "type": "Action.OpenUrl",
                "title": "View Full Case Study",
                "url": case["url"]
            },
            {
                "type": "Action.Submit",
                "title": "Show Summary",
                "data": {"action": "show_summary", "index": index}
            },
            {
                "type": "Action.Submit",
                "title": "Return to Top 3 List",
                "data": {"action": "show_top_3_again"}
            },
            {
                "type": "Action.Submit",
                "title": "Return Home 🏠",
                "data": {"action": "restart"}
            }
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
    }
