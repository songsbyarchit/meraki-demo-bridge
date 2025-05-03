def get_options_selector_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.2",
        "body": [
            {"type": "TextBlock", "text": "Choose your demo options", "weight": "Bolder", "size": "Medium"},
            {"type": "Input.ChoiceSet", "id": "audience", "style": "compact", "isRequired": True, "errorMessage": "Select audience",
             "choices": [
                 {"title": "---SELECT A VALUE---", "value": ""},
                 {"title": "Customer", "value": "customer"},
                 {"title": "Partner", "value": "partner"},
                 {"title": "Internal", "value": "internal"}
             ]},
            {"type": "Input.ChoiceSet", "id": "vertical", "style": "compact", "isRequired": True, "errorMessage": "Select vertical",
             "choices": [
                 {"title": "---SELECT A VALUE---", "value": ""},
                 {"title": "Healthcare", "value": "healthcare"},
                 {"title": "Education", "value": "education"},
                 {"title": "Manufacturing", "value": "manufacturing"},
                 {"title": "Retail", "value": "retail"},
                 {"title": "Government", "value": "government"},
                 {"title": "Finance", "value": "finance"},
                 {"title": "Hospitality", "value": "hospitality"},
                 {"title": "Transportation", "value": "transportation"},
                 {"title": "Energy", "value": "energy"},
                 {"title": "Telecom", "value": "telecom"}
             ]},
            {"type": "Input.ChoiceSet", "id": "product_line", "style": "compact", "isRequired": True, "errorMessage": "Select product line",
             "choices": [
                 {"title": "---SELECT A VALUE---", "value": ""},
                 {"title": "MX (Security & SD‑WAN)", "value": "mx"},
                 {"title": "MR (Wireless)", "value": "mr"},
                 {"title": "MS (Switching)", "value": "ms"},
                 {"title": "MV (Cameras)", "value": "mv"},
                 {"title": "MT (Sensors)", "value": "mt"},
                 {"title": "SM (Endpoint Mgmt)", "value": "sm"},
                 {"title": "MG (Cellular)", "value": "mg"}
             ]}
        ],
        "actions": [
            {"type": "Action.Submit", "title": "Continue", "data": {"action": "select_options"}},
            {"type": "Action.Submit", "title": "Restart", "data": {"action": "restart"}}
        ]
    }