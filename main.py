#!/usr/bin/env python3
import getopt
import sys

import src.config.constant as const
from src.helper.attendance import Attendance
from src.helper.date import get_today

# Global variable in main
filename = const.FILENAME_CSV
today = get_today("%d-%b-%Y")


def absensi(attendance_type, message, attendance_status='P'):
    # TODO : add feature attendance status
    data_absen = Attendance(
        date=today,
        attendance_type=attendance_type,
        attendance_status=attendance_status,
        activity=message
    )
    return data_absen


def main(argv):
    attendance_type = ''
    attendance_status = ''
    message_activity = ''

    try:
        opts, args = getopt.getopt(argv, "ha:s:m:", ["attendance=", "attendance_status=", "message="])
    except getopt.GetoptError:
        print(const.MSG_HELP)
        sys.exit()

    for opt, arg in opts:
        if opt == '-h':
            print(const.MSG_HELP)
            sys.exit()
        elif opt in ['-s', '--status']:
            attendance_status = arg
        elif opt in ['-a', '--attendance']:
            attendance_type = arg
        elif opt in ['-m', '--message']:
            message_activity = arg

    data_absen = absensi(attendance_type=attendance_type, message=message_activity, attendance_status=attendance_status)
    if attendance_type == const.CHECKIN:
        data_absen.checkin()
        print(const.MSG_CHECKIN)
    elif attendance_type == const.CHECKOUT:
        data_absen.checkout()
        print(const.MSG_CHECKOUT)
        # print("Terima kasih atas kerja kerasnya. Hati hati di jalan")
    else:
        print(const.MSG_UNKNOWN_COMMAND)


if __name__ == '__main__':
    main(sys.argv[1:])
