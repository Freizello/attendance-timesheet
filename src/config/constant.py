from ..helper.date import get_today

# options
CHECKIN = "in"
CHECKOUT = "out"

# Header timesheet
PROJECT_NAME = "CBM"
UNIT = "KJT - BRI 2 Sudirman"
NAME = "Hendriktio Freizello"
ID = "00116568"
PERIODE = get_today()

# filename
# FILENAME_CSV = "absensi.csv" # PROD
FILENAME_CSV = "absensi.dev.csv" # DEV

# message
MSG_HELP = 'Command : main.py -a --attendance ('+CHECKIN+'/'+CHECKOUT+')" -m --message "your message activity/remark"'
MSG_UNKNOWN_COMMAND = "Error unknown format : run main.py -h for usage."
MSG_CHECKIN = "Kamu sudah absen hari ini, Semangat bekerja"
MSG_CHECKOUT = "Terima kasih atas kerja kerasnya. Hati hati di jalan"
