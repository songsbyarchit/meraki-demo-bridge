import os
import gspread
from dotenv import load_dotenv
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from pytz import timezone

load_dotenv()

def push_feedback_to_sheets(data):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("google_creds.json", scope)
    client = gspread.authorize(creds)

    sheet_id = os.getenv("GOOGLE_SHEET_ID")
    if not sheet_id:
        raise ValueError("Missing GOOGLE_SHEET_ID in environment variables.")

    tab_name = "All Feedback"
    sheet = client.open_by_key(sheet_id)

    try:
        worksheet = sheet.worksheet(tab_name)
    except gspread.WorksheetNotFound:
        worksheet = sheet.add_worksheet(title=tab_name, rows="1000", cols="20")
        worksheet.append_row([
            "Room ID", "Tool Used", "Usual Minutes", "Bridge Minutes",
            "Percentage Time Saved", "Quality Rating", "Extra Feedback", "Timestamp",
            "Role", "Audience", "Product Line", "Industry"
        ])

    row = [
        data.get("room_id", ""),
        data.get("tool_used", ""),
        data.get("usual_minutes", ""),
        data.get("bridge_minutes", ""),
        data.get("percentage_time_saved", ""),
        data.get("quality_rating", ""),
        datetime.now(timezone("Europe/London")).strftime("%Y-%m-%d %H:%M:%S"),
        data.get("role", ""),
        data.get("audience", ""),
        data.get("product_line", ""),
        data.get("industry", ""),
        data.get("extra_feedback", ""),
    ]

    worksheet.append_row(row)
    print(f"✅ Pushed feedback row to '{tab_name}' tab.")