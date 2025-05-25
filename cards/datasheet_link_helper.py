from webexteamssdk.models.cards import AdaptiveCard, CardElement, TextBlock, ActionOpenUrl, ActionSubmit

def generate_device_buttons_card(devices, last_filter=None):
    """
    devices: List of dicts like {"model": "MX67", "datasheet_url": "..."}
    last_filter: Optional string to return to previous context
    """

    if not devices or len(devices) < 1:
        return {"type": "AdaptiveCard", "body": [{"type": "TextBlock", "text": "No matching devices."}], "actions": []}

    elements = [
        {
            "type": "TextBlock",
            "text": f"{len(devices)} matching device(s) found:",
            "weight": "Bolder",
            "wrap": True
        }
    ]

    for device in devices:
        elements.append({
            "type": "ActionSet",
            "actions": [
                {
                    "type": "Action.OpenUrl",
                    "title": device["model"],
                    "url": device["datasheet_url"]
                }
            ]
        })

    # Navigation actions
    nav_buttons = [
        {
            "type": "Action.Submit",
            "title": "Return to last filter",
            "data": {"action": "return_last_filter", "last_filter": last_filter}
        },
        {
            "type": "Action.Submit",
            "title": "Return to product family selection",
            "data": {"action": "return_family_selection"}
        },
        {
            "type": "Action.Submit",
            "title": "Return home",
            "data": {"action": "return_home"}
        },
    ]

    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": elements,
        "actions": nav_buttons
    }