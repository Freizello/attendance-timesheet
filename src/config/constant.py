from ..helper.date import get_today

# OPTIONS
CHECKIN = "in"
CHECKOUT = "out"

# TIMESHEET HEADER
TS_HEADER_START_COL: int = 3
TS_HEADER_START_ROW: int = 1
# TS_HEADER_VAL_COL: int = 3

PROJECT_NAME = "CBM"
UNIT = "KJT - BRI 2 Sudirman"
NAME = "Hendriktio Freizello"
ID = "00116568"
PERIODE = get_today()

# filename
FILENAME_PATH = "src/files/"
# FILENAME_CSV = FILE_PATH+"absensi.csv" EXISTING
FILENAME_CSV = FILENAME_PATH+"absensi.dev.csv"
FILENAME_XLSX = FILENAME_PATH+"template.xlsx"

# message
MSG_HELP = 'Command : main.py -a --attendance ('+CHECKIN+'/'+CHECKOUT+')" -m --message "your message activity/remark"'
MSG_UNKNOWN_COMMAND = "Error unknown format : run main.py -h for usage."
MSG_CHECKIN = "Kamu sudah absen hari ini, Semangat bekerja"
MSG_CHECKOUT = "Terima kasih atas kerja kerasnya. Hati hati di jalan"
