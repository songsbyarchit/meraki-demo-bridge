def build_datasheet_buttons_card(models, product_family):
    card_body = [
        {
            "type": "TextBlock",
            "text": f"📄 Datasheets for {product_family} Models",
            "weight": "Bolder",
            "size": "Medium"
        }
    ]

    for model in models:
        card_body.append({
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.OpenUrl",
                    "title": model.model_name,
                    "url": model.datasheet_url
                }
            ]
        })

    card_body.append({
        "type": "TextBlock",
        "text": "---",
        "separator": True
    })

    actions = [
        {
            "type": "Action.Submit",
            "title": "🔁 Return to Last Filter",
            "data": {"action": "return_to_filter"}
        },
        {
            "type": "Action.Submit",
            "title": "🧭 Return to Product Family Selection",
            "data": {"action": "return_to_family"}
        },
        {
            "type": "Action.Submit",
            "title": "🏠 Return Home",
            "data": {"action": "return_home"}
        }
    ]

    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": card_body,
        "actions": actions
    }