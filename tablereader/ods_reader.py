from reader import Reader
from ezodf import opendoc

class Ods(Reader):
    def __init__(self, file_name, sheet=None):
        self.document = opendoc(file_name)
        self.sheet = sheet

        if sheet is None:
            self.sheet = self.document.sheets[0]
        else: #int or string
            self.sheet = self.document.sheets[sheet]
            
        self.Value = self.generate_value_class([c.value for c in self.sheet.row(0)])

    def read(self):
        def _ods_valer(cell):
            if cell.value_type == 'string':
                return cell.value
            elif cell.value_type == 'float':
                # all numbers are floats
                # force ints to be ints, let floats be floats
                if cell.value.is_integer():
                    return unicode(int(cell.value)) 
                else:
                    return unicode(cell.value)
            else: # any other type
                return cell.value

        for row in xrange(1, self.sheet.nrows()+1):
            v = self.Value()
            v.__autoadd__(self.sheet.row(row), valer = _ods_valer)
            yield v
