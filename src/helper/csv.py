import csv as csv
import os

from .date import get_today, get_delta_time
from ..config import constant as const

filename = const.FILENAME_CSV
today = get_today("%d-%b-%Y")


def check_exist_row(field, value, _filename=filename, _fieldname=None):
    with open(_filename, mode="r") as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=_fieldname)
        for row in reader:
            if row[field] == value:
                return True


def insert_csv(object):  # DONE : Ada penjagaan harus satu kali checkin dalam sehari
    fieldname = list(object.__dict__.keys())
    data_dict = dict(object.__dict__)

    with open(filename, mode='a', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldname)
        if not (os.path.exists(filename) and os.path.getsize(filename) > 0):
            writer.writeheader()

        row_exist: bool = check_exist_row(field="date", value=today, _filename=filename, _fieldname=fieldname)
        if not row_exist:
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
            # if row['end'] == '' and row['date'] == str(data_dict['date']): # penjagaan sekali checkout doang
            if row['date'] == str(data_dict['date']):
                # update end and total_hour column value
                row['end'] = data_dict['end']
                row['total_hour'] = get_delta_time(str(row['start']), str(data_dict['end']))
                if row['activity'] == '' or row['activity'] is None: row['activity'] = data_dict['activity']
            writer.writerow(row)

    # replace old csv with updated data csv
    shutil.move(tempfile.name, filename)
