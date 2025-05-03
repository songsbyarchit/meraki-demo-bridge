def get_options_selector_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.2",
        "body": [
            {"type": "TextBlock", "text": "Choose your demo options", "weight": "Bolder", "size": "Medium"},
            {"type": "Input.ChoiceSet", "id": "audience", "style": "compact", "isRequired": True, "errorMessage": "Select audience",
             "choices": [
                 {"title": "---SELECT AUDIENCE TYPE---", "value": ""},
                 {"title": "Customer", "value": "customer"},
                 {"title": "Partner", "value": "partner"},
                 {"title": "Internal", "value": "internal"}
             ]},
            {"type": "Input.ChoiceSet", "id": "vertical", "style": "compact", "isRequired": True, "errorMessage": "Select vertical",
            "choices": [
                {"title": "---SELECT A VERTICAL---", "value": ""},
                {"title": "K-12 Education/Primary Education", "value": "k12"},
                {"title": "Healthcare", "value": "healthcare"},
                {"title": "Manufacturing", "value": "manufacturing"},
                {"title": "Higher Education", "value": "higher_ed"},
                {"title": "Hospitality", "value": "hospitality"},
                {"title": "Retail", "value": "retail"},
                {"title": "Federal Government", "value": "federal_gov"},
                {"title": "Service Provider", "value": "service_provider"},
                {"title": "Financial Services", "value": "finance"},
                {"title": "Small Business", "value": "small_business"},
                {"title": "State And Local Government", "value": "state_local_gov"},
                {"title": "Professional Services", "value": "professional_services"}
            ]},
            {"type": "Input.ChoiceSet", "id": "product_line", "style": "compact", "isRequired": True, "errorMessage": "Select product line",
             "choices": [
                 {"title": "---SELECT A PRODUCT---", "value": ""},
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