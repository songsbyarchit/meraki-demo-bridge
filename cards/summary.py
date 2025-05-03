def build_summary_card(customer, summary):
    return {
        "type": "AdaptiveCard",
        "version": "1.2",
        "body": [
            {"type": "TextBlock", "text": f"Summary for {customer}", "weight": "Bolder"},
            {"type": "TextBlock", "text": summary, "wrap": True}
        ],
        "actions": [
            {"type": "Action.Submit", "title": "Start over", "data": {"action": "restart"}}
        ]
    }