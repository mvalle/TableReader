from reader import Reader
from xlrd import open_workbook

class Excel(Reader):
    def __init__(self, file_name, sheet=None):
        self.work_book = open_workbook(file_name)
        self.worksheet = None

        if sheet is None:
            self.worksheet = self.work_book.sheets()[0]
        elif isinstance(sheet, (int, long)):
            self.worksheet = self.work_book.sheets()[sheet]
        else: #string
            self.worksheet = self.work_book.sheet_by_name(sheet)

        self.Value = self._generateValueClass([c.value for c in self.worksheet.row(0)])
    
    def read(self):
        def _excel_valer(cell):
            if cell.ctype == 1: # text cells is represented as unicode
                return cell.value
            elif cell.ctype == 2: # numbers are represented as floats
                if cell.value.is_integer():
                    return unicode(int(cell.value))
                return unicode(cell.value)
            else: # catch all
                return cell.value

        for row in xrange(1, self.worksheet.nrows+1):
            v = self.Value()
            v.__autoadd__(self.worksheet.row(row), valer = _excel_valer)
            yield v



        
        
