def get_mx_filter_card(defaults=None):
    defaults = defaults or {}
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {
                "type": "TextBlock",
                "text": "🛡️ MX Appliance Filters",
                "wrap": True,
                "weight": "Bolder",
                "size": "Medium"
            },
            {
                "type": "TextBlock",
                "text": "Set at least one filter to narrow down MX models:",
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": "Use Case",
                "wrap": True,
                "weight": "Bolder"
            },
            {
                "type": "Input.ChoiceSet",
                "id": "use_case",
                "style": "compact",
                "value": defaults.get("use_case", ""),
                "choices": [
                    {"title": "--- Show all ---", "value": ""},
                    {"title": "Branch", "value": "branch"},
                    {"title": "Small Office", "value": "small office"},
                    {"title": "Data Center", "value": "data center"},
                    {"title": "SD-WAN", "value": "sd-wan"}
                ]
            },
            {
                "type": "TextBlock",
                "text": "Minimum Throughput (Mbps)",
                "wrap": True,
                "weight": "Bolder"
            },
            {
                "type": "Input.ChoiceSet",
                "id": "min_throughput",
                "style": "compact",
                "value": defaults.get("min_throughput", ""),
                "choices": [
                    {"title": "--- Show all ---", "value": ""},
                    {"title": "200+", "value": "200"},
                    {"title": "500+", "value": "500"},
                    {"title": "1000+", "value": "1000"},
                    {"title": "2000+", "value": "2000"}
                ]
            },
            {
                "type": "TextBlock",
                "text": "Minimum User Count",
                "wrap": True,
                "weight": "Bolder"
            },
            {
                "type": "Input.ChoiceSet",
                "id": "min_users",
                "style": "compact",
                "value": defaults.get("min_users", ""),
                "choices": [
                    {"title": "--- Show all ---", "value": ""},
                    {"title": "50+", "value": "50"},
                    {"title": "100+", "value": "100"},
                    {"title": "250+", "value": "250"},
                    {"title": "500+", "value": "500"}
                ]
            },
            {
                "type": "TextBlock",
                "text": "Uplink Ports",
                "wrap": True,
                "weight": "Bolder"
            },
            {
                "type": "Input.ChoiceSet",
                "id": "uplink_ports",
                "style": "compact",
                "value": defaults.get("uplink_ports", ""),
                "choices": [
                    {"title": "--- Show all ---", "value": ""},
                    {"title": "1G", "value": "1g"},
                    {"title": "10G", "value": "10g"},
                    {"title": "SFP", "value": "sfp"},
                    {"title": "SFP+", "value": "sfp+"}
                ]
            },
            {
                "type": "Input.Toggle",
                "id": "has_wireless",
                "title": "Only show models with wireless support",
                "valueOn": "true",
                "valueOff": "false",
                "value": defaults.get("has_wireless", "false")
            },
            {
                "type": "Input.Toggle",
                "id": "has_cellular",
                "title": "Only show models with cellular support",
                "valueOn": "true",
                "valueOff": "false",
                "value": defaults.get("has_cellular", "false")
            }
        ],
            "actions": [
        {
            "type": "Action.Submit",
            "title": "Find Matching Models",
            "data": {"action": "filter_mx_models"}
        },
        {
            "type": "Action.Submit",
            "title": "Return to Category Selection",
            "data": {"action": "sizing"}
        },
        {
            "type": "Action.Submit",
            "title": "Return Home 🏠",
            "data": {"action": "restart"}
        }
    ]
    }