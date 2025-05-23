def get_mv_filter_card():
    return {
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
            {
                "type": "TextBlock",
                "text": "📷 MV Camera Filters",
                "wrap": True,
                "weight": "Bolder",
                "size": "Medium"
            },
            {
                "type": "TextBlock",
                "text": "Set at least one filter to narrow down MV models:",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "location",
                "label": "Location",
                "style": "compact",
                "choices": [
                    {"title": "--- Show all ---", "value": ""},
                    {"title": "Indoor", "value": "indoor"},
                    {"title": "Outdoor", "value": "outdoor"}
                ],
                "value": "all"
            },
            {
                "type": "Input.ChoiceSet",
                "id": "fov",
                "label": "Field of View",
                "style": "compact",
                "choices": [
                    {"title": "--- Show all ---", "value": ""},
                    {"title": "Wide", "value": "wide"},
                    {"title": "Narrow", "value": "narrow"},
                    {"title": "Fisheye", "value": "fisheye"}
                ],
                "value": "all"
            },
            {
                "type": "Input.ChoiceSet",
                "id": "max_fps",
                "label": "Maximum FPS",
                "style": "compact",
                "choices": [
                    {"title": "--- Show all ---", "value": ""},
                    {"title": "15 FPS", "value": "15"},
                    {"title": "24 FPS", "value": "24"}
                ],
                "value": "all"
            },
            {
                "type": "Input.ChoiceSet",
                "id": "resolution",
                "label": "Resolution",
                "style": "compact",
                "choices": [
                    {"title": "--- Show all ---", "value": ""},
                    {"title": "1080p", "value": "1080p"},
                    {"title": "4K", "value": "4K"}
                ],
                "value": "all"
            }
        ],
        "actions": [
            {
                "type": "Action.Submit",
                "title": "Show Matching Models",
                "data": {"action": "filter_mv_models"}
            },
            {
                "type": "Action.Submit",
                "title": "Back",
                "data": {"action": "sizing"}
            }
        ]
    }
