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
                "text": "Set filters to narrow down MV models:",
                "wrap": True
            },
            {
                "type": "Input.ChoiceSet",
                "id": "location",
                "label": "Location",
                "style": "compact",
                "choices": [
                    {"title": "Indoor", "value": "indoor"},
                    {"title": "Outdoor", "value": "outdoor"}
                ]
            },
            {
                "type": "Input.ChoiceSet",
                "id": "fov",
                "label": "Field of View",
                "style": "compact",
                "choices": [
                    {"title": "Wide", "value": "wide"},
                    {"title": "Narrow", "value": "narrow"},
                    {"title": "Fisheye", "value": "fisheye"}
                ]
            },
            {
                "type": "Input.ChoiceSet",
                "id": "max_fps",
                "label": "Maximum FPS",
                "style": "compact",
                "choices": [
                    {"title": "15 FPS", "value": "15"},
                    {"title": "24 FPS", "value": "24"}
                ]
            },
            {
                "type": "Input.ChoiceSet",
                "id": "resolution",
                "label": "Resolution",
                "style": "compact",
                "choices": [
                    {"title": "1080p", "value": "1080p"},
                    {"title": "4K", "value": "4K"}
                ]
            },
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