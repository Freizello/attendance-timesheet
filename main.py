#!/usr/bin/env python3
import csv
import getopt
import os
import sys

import src.config.constant as const
from src.helper.attendance import Attendance
from src.helper.date import get_today, get_delta_time

# Global variable in main
filename = const.FILENAME_CSV


def absensi(type, message):
    data_absen = Attendance(
        date=get_today("%d-%b-%Y"),
        attendance_type=type,
        attendance_status="P",
        activity=message
    )

    return data_absen


def insert_csv(object): # TODO : Ada penjagaan harus satu kali checkin dalam sehari
    fieldname = list(object.__dict__.keys())
    data_dict = dict(object.__dict__)

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

    data_dict = dict(object.__dict__)
    fieldname = list(object.__dict__.keys())

    # prepare temporary file to store updated end column data.
    tempfile = NamedTemporaryFile(mode='w', delete=False, newline='')
    with open(filename, 'r', newline='') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldname)
        writer = csv.DictWriter(tempfile, fieldnames=fieldname)

        # loop for searching value row by row
        for row in reader:
            # find row that end column is empty and date column == date value from absensi("checkout")
            if row['end'] == '' and row['date'] == str(data_dict['date']):
                # update end and total_hour column value
                row['end'] = data_dict['end']
                row['total_hour'] = get_delta_time(str(row['start']), str(data_dict['end']))
            writer.writerow(row)

    # replace old csv with updated data csv
    shutil.move(tempfile.name, filename)


def main(argv):
    attendance_type = ''
    message_activity = ''

    try:
        opts, args = getopt.getopt(argv, "ha:m:", ["attendance=", "message="])
    except getopt.GetoptError:
        print(const.MSG_HELP)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(const.MSG_HELP)
            sys.exit()
        elif opt in ['-a', '--attendance']:
            attendance_type = arg
        elif opt in ['-m', '--message']:
            message_activity = arg

    data_absen = absensi(attendance_type, message_activity)
    if attendance_type == "checkin":
        insert_csv(data_absen)
        print("kamu sudah absen masuk hari ini. Selamat bekerja")
    elif attendance_type == "checkout":
        update_csv(data_absen)
        print("Terima kasih atas kerja kerasnya. Hati hati di jalan")
    else:
        print(const.MSG_UNKNOWN_COMMAND)


if __name__ == '__main__':

    main(sys.argv[1:])