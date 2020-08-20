# from openpyxl import Workbook
# from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font

from src.helper.attendance import Attendance
from src.helper.date import get_today

absensi = Attendance(
                    date=get_today("%d-%b-%Y"),
                    attendance_type="checkin",
                    attendance_status="P",
                    activity="Activity 1"
                    )

print(absensi)
# absensi.print_self()

# wb = Workbook()
# font = Font(
#             name='Cambria',
#             size=9
#             )
#
# # grab the active worksheet
# ws = wb.active
#
# # Data can be assigned directly to cells
# ws['A1'] = 42
#
# # Rows can also be appended
# ws.append([1, 2, 3])
#
# # Python types will automatically be converted
# import datetime
#
# ws['A2'] = datetime.datetime.now()
#
# # Save the file
# wb.save("sample.xlsx")
