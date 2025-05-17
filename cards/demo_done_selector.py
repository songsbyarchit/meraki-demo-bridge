from cards.base_card import create_card

def get_demo_done_card():
    return create_card(
        title="What’s next?",
        text="Choose an action below:",
        buttons=[
            {"title": "Build another Demo + FAQ", "value": "start_demo", "type": "action"},
            {"title": "Return home",        "value": "restart",    "type": "action"},
        ]
    )