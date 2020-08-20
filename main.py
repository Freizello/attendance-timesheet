from src.helper.attendance import Attendance
from src.helper.date import get_today
import src.config.core as core
import csv
import os

filename = core.FILENAME_CSV


def absensi(type):
    data_absen = Attendance(
        date=get_today("%d-%b-%Y"),
        attendance_type=type,
        attendance_status="P",
        activity="Activity 1"
    )

    return data_absen


def insert_csv(object):
    fieldname = list(object.__dict__.keys())
    data_dict = dict(object.__dict__)
    # values = list(object.__dict__.values())

    with open(filename, mode='a', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldname)
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            writer.writerow(data_dict)
        else:
            writer.writeheader()
            writer.writerow(data_dict)


def update_csv(object):
    import shutil
    from tempfile import NamedTemporaryFile

    tempfile = NamedTemporaryFile(mode='w', delete=False, newline="")

    data_dict = dict(object.__dict__)
    fieldname = list(object.__dict__.keys())

    with open(filename, 'r', newline="") as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldname)
        writer = csv.DictWriter(tempfile, fieldnames=fieldname)
        for row in reader:
            if row['end'] == "" and row['date'] == str(data_dict['date']):
                row['end'] = data_dict['end']
            writer.writerow(row)

    shutil.move(tempfile.name, filename)


if __name__ == '__main__':
    data_masuk = absensi("checkin")
    data_keluar = absensi("checkout")
    insert_csv(data_masuk)
    update_csv(data_keluar)
