import json
import time

import src.config.constant as cons
from src.helper import csv as helper_csv


# Object dasar untuk membuat value pada setiap kolom yang dibutuhkan csv/xls timesheet
# beberapa kolom adalah hasil generate dari parameter yang dilemparkan saat memanggil
# class Attendance.

class Attendance:
    def __init__(self, date, attendance_type, attendance_status, activity):
        self.date = date
        self.start = time.strftime("%H:%M") if attendance_type == cons.CHECKIN else None
        self.end = time.strftime("%H:%M") if attendance_type == cons.CHECKOUT else None
        self.total_hour = None
        self.presents = attendance_status if attendance_status == "P" else None
        self.sick = attendance_status if attendance_status == "S" else None
        self.business_trip = attendance_status if attendance_status == "BT" else None
        self.permit = attendance_status if attendance_status == "PM" else None
        self.vacation = attendance_status if attendance_status == "V" else None
        self.not_working = attendance_status if attendance_status == "X" else None
        self.activity = activity

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def checkin(self):
        # DONE : insert_csv diubah masuk ke sini
        helper_csv.insert_csv(self)

    def checkout(self):
        # DONE : update_csv diubah masuk ke sini
        helper_csv.update_csv(self)

    def create_report(self):
        # TODO : Create report to xlsx file
        pass
