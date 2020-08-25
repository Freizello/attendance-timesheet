from openpyxl import Workbook, load_workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font


class Excel:
    def __init__(self, filename):
        self.filename = filename
        self.project_name = None
        self.division = None
        self.employee_name = None
        self.employee_id = None
        self.period = None
        self.sheetname: str = ''
        self.sheetnames: list = []

    def read_exist(self):
        sheetname = self.sheetname
        try:
            if self.filename is not None:
                wbook = load_workbook(filename=self.filename)
                self.sheetnames = list(wbook.sheetnames)
                # wsheet = wbook[sheetname] if sheetname in self.sheetnames else None
                if sheetname in self.sheetnames: wsheet = wbook[sheetname]
                return wbook, wsheet
        except Exception as e:
            raise

    def set_header(self, header_cell: list, value_cell: list, value: list):
        # TODO : Refactor this, make efficient with params
        wbook, wsheet = self.read_exist()
        try:
            if len(header_cell) >= len(value):
                for i in range(len(header_cell)):
                    print("Writing " + value[i] + " to " + value_cell[i])
                    wsheet[value_cell[i]].value = value[i]

            wbook.save(self.filename)
        except Exception as e:
            raise

    def set_row(self, data:list, start_row):
        # TODO : Implement this (fill row based on row setting)
        pass
