import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os

def push_feedback_to_sheets(data):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("google-creds.json", scope)
    client = gspread.authorize(creds)

    sheet_map = {
        "demo_flow": "Demo Feedback",
        "sizing": "Sizing Feedback",
        "case_study": "Case Study Feedback"
    }

    tab_name = sheet_map.get(data["tool_used"], "General Feedback")
    sheet = client.open("Meraki Feedback Tracker").worksheet(tab_name)

    row = [
        data["room_id"],
        data["tool_used"],
        data["usual_minutes"],
        data["bridge_minutes"],
        data["quality_rating"],
        data["extra_feedback"],
        datetime.utcnow().isoformat()
    ]
    sheet.append_row(row)