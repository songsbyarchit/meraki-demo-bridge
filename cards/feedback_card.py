def get_feedback_card():
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
                "value": "",
                "choices": [
                    {"title": "-- Select a Role --", "value": ""},
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
                "value": "",
                "choices": [
                    {"title": "-- Select an Audience --", "value": ""},
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
                "value": "",
                "choices": [
                    {"title": "-- Select a Product --", "value": ""},
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
                "value": "",
                "choices": [
                    {"title": "-- Select an Industry --", "value": ""},
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
                "choices": [
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
                "max": 180
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
                "max": 180
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
                "choices": [
                    {"title": "-- Select a quality rating --", "value": ""},
                    {"title": "1 – Poor", "value": "1"},
                    {"title": "2 – Fair", "value": "2"},
                    {"title": "3 – Good", "value": "3"},
                    {"title": "4 – Very Good", "value": "4"},
                    {"title": "5 – Excellent", "value": "5"}
                ]
            },
            {
                "type": "TextBlock",
                "text": "Any feedback for us?",
                "wrap": True
            },
            {
                "type": "Input.Text",
                "id": "extra_feedback",
                "placeholder": "Optional",
                "isMultiline": True
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