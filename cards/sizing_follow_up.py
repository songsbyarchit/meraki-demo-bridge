def get_sizing_follow_up_card(product_family: str):
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {
                "type": "TextBlock",
                "text": "What would you like to do next?",
                "wrap": True,
                "weight": "Bolder",
                "size": "Medium"
            }
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "🔁 Reapply Filters",
                "data": {"action": "sizing_select_family", "product_family": product_family}
            },
            {
                "type": "Action.Submit",
                "title": "🧭 Choose Different Product Family",
                "data": {"action": "sizing"}
            },
            {
                "type": "Action.Submit",
                "title": "🏠 Return Home",
                "data": {"action": "restart"}
            }
        ]
    }