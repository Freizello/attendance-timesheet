from ..helper.date import get_today

# Header timesheet
PROJECT_NAME = "CBM"
UNIT = "KJT - BRI 2 Sudirman"
NAME = "Hendriktio Freizello"
ID = "00116568"
PERIODE = get_today()

# filename
FILENAME_CSV = "absensi.csv"

# message
MSG_HELP = 'Command : main.py -a "attendance type (checkin/checkout)" -m "your message activity/remark"'
MSG_UNKNOWN_COMMAND = "Error unknown format : run main.py -h for usage."
