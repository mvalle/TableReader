from reader import Reader
from openpyxl.reader.excel import load_workbook

class Excel(Reader):
    def __init__(self, file_name, sheet=None):
        self.work_book = load_workbook(file_name)
        self.worksheet = None

        if sheet is None:
            self.worksheet = self.work_book.worksheets[0]
        elif isinstance(sheet, (int, long)):
            self.worksheet = self.work_book.worksheets[sheet]
        else: #string
            self.worksheet = self.work_book.get_sheet_by_name(name = sheet)

        self.Value = self._generateValueClass([c.value for c in self.worksheet.rows[0]])
    
    def read(self):
        for row in self.worksheet.rows[1:]: # all but first row
            if not row:
                break
            v = self.Value()
            v.__autoadd__(row, valer = lambda x:x.value)
            yield v
