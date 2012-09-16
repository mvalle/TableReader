from reader import Reader
import csv

class Csv(Reader):
    def __init__(self, file_name):
        self.open_file = open(file_name, 'rb')
        self.csv_object = csv.reader(self.open_file)
        headers = self.csv_object.next()

        self.Value = self._generateValueClass(headers)
    
    def read(self):
        """Generator that reads a line from the file, and returns a Value class. """
        for line in self.csv_object:
            if not line:
                break
            v = self.Value()
            v.__autoadd__(line)#, enumer=lambda x:x.split(','))
            yield v
        self.open_file.close()
