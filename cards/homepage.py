def get_homepage_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.2",
        "body": [
            {"type": "TextBlock", "text": "Meraki Demo Bridge", "weight": "Bolder", "size": "Large"},
            {"type": "TextBlock", "text": "Pick a path to craft the right Meraki demo and upsell story."}
        ],
        "actions": [
            {"type": "Action.Submit", "title": "Start demo flow", "data": {"action": "start_demo"}}
        ]
    }