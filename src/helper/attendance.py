# from src.helper.date import get_today
import json
import time


class Attendance:
    def __init__(self, date, attendance_type, attendance_status, activity):
        # self.date = date
        # self.attendance_type = attendance_type
        # self.attendance_status = attendance_status
        # self.activity = activity

        self.date = date
        self.start = time.strftime("%H:%M") if attendance_type == "checkin" else None
        self.end = time.strftime("%H:%M") if attendance_type == "checkout" else None
        self.total_hour = None
        self.presents = attendance_status if attendance_status == "P" else ""
        self.sick = attendance_status if attendance_status == "S" else ""
        self.business_trip = attendance_status if attendance_status == "BT" else ""
        self.permit = attendance_status if attendance_status == "PM" else ""
        self.vacation = attendance_status if attendance_status == "V" else ""
        self.not_working = attendance_status if attendance_status == "X" else ""
        self.activity = activity

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)