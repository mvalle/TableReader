import re

class Csv:
    values = []
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
            v.__autoadd__(line)
            yield v

    def _sanitize(self, name, allocated_names):
        name = name.strip().replace(" ", "_")
        if allocated_names.has_key(name):
            raise NameError("%s is already defined" % name)
        if re.match(r'^[0-9]', name):
            name = "_"+name
        elif name == "":
            print "Warning! Empty header in file"
        return name

    def _generateValueClass(self, headers):
        class ValueBase(object):
            def __autoadd__(self, data_line):    
                for (i, datum) in enumerate(data_line.split(',')):
                    setattr(self, self.__attributemap__[i], datum)
        attributes = {}
        attribute_map = {}
        attributes["__attributemap__"] = attribute_map
        
        for (i, header) in enumerate(headers):
            header = self._sanitize(header, attribute_map)
            attributes[header] = ""
            attribute_map[i] = header

        return type("Value", (ValueBase,), attributes)
    

