def get_feedback_card(defaults=None):
    defaults = defaults or {}

    def safe_number(value):
        return int(value) if str(value).isdigit() else None

    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {
                "type": "TextBlock",
                "text": "📝 Help us improve",
                "weight": "Bolder",
                "size": "Medium"
            },
            {
                "type": "TextBlock",
                "text": "What is your role?",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "role",
                "style": "compact",
                "value": defaults.get("role", ""),
                "choices": [
                    {"title": "-- Select a role --", "value": ""},
                    {"title": "Account Executive", "value": "Account Executive"},
                    {"title": "Systems Engineer", "value": "Systems Engineer"},
                    {"title": "Technical Solutions Architect", "value": "Technical Solutions Architect"},
                    {"title": "Sales Leader", "value": "Sales Leader"},
                    {"title": "Other", "value": "Other"}
                ]
            },
            {
                "type": "TextBlock",
                "text": "Who was the audience?",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "audience",
                "style": "compact",
                "value": defaults.get("audience", ""),
                "choices": [
                    {"title": "-- Select an audience --", "value": ""},
                    {"title": "Partner", "value": "partner"},
                    {"title": "Customer", "value": "customer"},
                    {"title": "Internal", "value": "internal"}
                ]
            },
            {
                "type": "TextBlock",
                "text": "Which product line did you use it for?",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "product_line",
                "style": "compact",
                "value": defaults.get("product_line", ""),
                "choices": [
                    {"title": "-- Select a product --", "value": ""},
                    {"title": "MX (Security & SD‑WAN)", "value": "mx"},
                    {"title": "MR (Wireless)", "value": "mr"},
                    {"title": "MS (Switching)", "value": "ms"},
                    {"title": "MV (Cameras)", "value": "mv"},
                    {"title": "MT (Sensors)", "value": "mt"},
                    {"title": "SM (Endpoint Mgmt)", "value": "sm"},
                    {"title": "MG (Cellular)", "value": "mg"}
                ]
            },
            {
                "type": "TextBlock",
                "text": "Which industry was it used for?",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "industry",
                "style": "compact",
                "value": defaults.get("industry", ""),
                "choices": [
                    {"title": "-- Select an industry --", "value": ""},
                    {"title": "Finance", "value": "finance"},
                    {"title": "Healthcare", "value": "healthcare"},
                    {"title": "Retail", "value": "retail"},
                    {"title": "K-12", "value": "k12"},
                    {"title": "Higher Education", "value": "higher_ed"},
                    {"title": "Hospitality", "value": "hospitality"},
                    {"title": "Manufacturing", "value": "manufacturing"},
                    {"title": "Professional Services", "value": "professional_services"},
                    {"title": "Service Provider", "value": "service_provider"},
                    {"title": "Small Business", "value": "small_business"},
                    {"title": "State/Local Government", "value": "state_local_gov"},
                    {"title": "Federal Government", "value": "federal_gov"}
                ]
            },
            {
                "type": "TextBlock",
                "text": "Which part of the Meraki Demo Bridge did you use?",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "used_tool",
                "style": "compact",
                "value": defaults.get("used_tool", ""),
                "choices": [
                    {"title": "-- Select a tool --", "value": ""},
                    {"title": "Demo Flow Generator", "value": "demo_flow"},
                    {"title": "Sizing Assistant", "value": "sizing"},
                    {"title": "Case Study Finder", "value": "case_study"}
                ]
            },
            {
                "type": "TextBlock",
                "text": "How long does this task normally take you without the tool? (minutes)",
                "wrap": True
            },
            {
                "type": "Input.Number",
                "id": "usual_minutes",
                "placeholder": "e.g. 30",
                "min": 0,
                "max": 180,
                "value": safe_number(defaults.get("usual_minutes"))
            },
            {
                "type": "TextBlock",
                "text": "How long did it take you using this tool? (minutes)",
                "wrap": True
            },
            {
                "type": "Input.Number",
                "id": "bridge_minutes",
                "placeholder": "e.g. 20",
                "min": 0,
                "max": 180,
                "value": safe_number(defaults.get("bridge_minutes"))
            },
            {
                "type": "TextBlock",
                "text": "How would you rate the quality of the tool’s output?",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "quality_rating",
                "style": "compact",
                "value": defaults.get("quality_rating", ""),
                "choices": [
                    {"title": "-- Select a quality rating --", "value": ""},
                    {"title": "1 – Poor (doing this task is much better WITHOUT the demo bridge)", "value": "1"},
                    {"title": "2 – Fair (doing this task is not much better regardless of if I use the demo bridge)", "value": "2"},
                    {"title": "3 – Good (doing this task is slightly better WITH the demo bridge than without it)", "value": "3"},
                    {"title": "4 – Very Good (doing this task is NOTICEABLY better WITH the demo bridge)", "value": "4"},
                    {"title": "5 – Excellent (Now that I've used the demo bridge, I'm unlikely to return to the OLD way)", "value": "5"}
                ]
            },
            {
                "type": "TextBlock",
                "text": "Any additional feedback for us (feature requests or how to make existing features better??",
                "wrap": True
            },
            {
                "type": "Input.Text",
                "id": "extra_feedback",
                "placeholder": "Optional",
                "isMultiline": True,
                "value": defaults.get("extra_feedback", "")
            }
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Submit Feedback",
                "data": {"action": "submit_feedback"}
            },
            {
                "type": "Action.Submit",
                "title": "Return Home 🏠",
                "data": {"action": "restart"}
            }
        ]
    }
