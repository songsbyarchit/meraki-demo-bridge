import csv
from datetime import datetime
from sqlalchemy import text
from database import SessionLocal
from models.feedback import Feedback

db = SessionLocal()

# 1. Delete all existing rows
db.execute(text("TRUNCATE TABLE feedback RESTART IDENTITY CASCADE;"))

# 2. Insert rows from the CSV
with open("Meraki Demo Bridge Feedback - All Feedback (2).csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        entry = Feedback(
            room_id=row["Room ID"],
            tool_used=row["Tool Used"],
            usual_minutes=int(row["Usual Minutes"]),
            bridge_minutes=int(row["Bridge Minutes"]),
            percentage_time_saved=int(row["Percentage Time Saved"]),
            quality_rating=int(row["Quality Rating"]),
            extra_feedback=row.get("Extra Feedback", ""),
            timestamp=datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S"),
            role=row["Role"],
            audience=row["Audience"],
            product_line=row["Product Line"],
            industry=row["Industry"]
        )
        db.add(entry)

db.commit()
db.close()

print("✅ Feedback table reset and repopulated from CSV.")