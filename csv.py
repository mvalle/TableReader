class Csv:
    def __init__(self, file_name):
        self.open_file = open(file_name)
        headers = self.open_file.readline().split(',')

        self.Value = self._generateValueClass(headers)
    
    def read(self):
        data_line = self.open_file.readline()

        data = data_line.split(',')
        print dir(self.Value)
        v = self.Value()
        v.__autoadd__(data_line)
        print v.E_mail

    def _checkHeaderName(self, name, allocated_names):
        name = name.strip().replace(" ", "_")
        if allocated_names.has_key(name):
            raise NameError("%s is already defined" % name)
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
            header = self._checkHeaderName(header, attribute_map)
            attributes[header] = ""
            attribute_map[i] = header

        return type("Value", (ValueBase,), attributes)
    

