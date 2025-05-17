def get_homepage_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.2",
        "body": [
            {"type": "TextBlock", "text": "Meraki Demo Bridge", "weight": "Bolder", "size": "Large"},
            {"type": "TextBlock", "text": "Pick a path to craft the right Meraki demo and upsell story."}
        ],
    "actions": [
        {"type": "Action.Submit", "title": "Tailored demo + FAQs", "data": {"action": "start_demo"}},
        {"type": "Action.Submit", "title": "View case studies", "data": {"action": "case_study"}},
        {"type": "Action.Submit", "title": "Give feedback", "data": {"action": "give_feedback"}}
    ]
    }