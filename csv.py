from reader import Reader

class Csv(Reader):
    def __init__(self, file_name):
        self.open_file = open(file_name)
        headers = self.open_file.readline().split(',')

        self.Value = self._generateValueClass(headers)
    
    def read(self):
        """Generator that reads a line from the file, and returns a Value class. """
        for line in self.open_file:
            if not line:
                break
            v = self.Value()
            v.__autoadd__(line, lambda x:x.split(','), lambda x:x)
            yield v
        self.open_file.close()
