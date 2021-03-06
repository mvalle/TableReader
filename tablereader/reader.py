import re

class Reader:
    def init_value():
        self.Value = self.generate_value_class(headers)


    def sanitize(self, name, allocated_names):
        name = name.strip().replace(" ", "_")
        if allocated_names.has_key(name):
            raise NameError("%s is already defined" % name)
        if re.match(r'^[0-9]', name):
            name = "_"+name
        elif name == "":
            print "Warning! Empty header in file"
        return name

    def generate_value_class(self, headers):

        class ValueBase(object):
            def __autoadd__(self, data_line, enumer = lambda x:x, valer = lambda x:x.decode('utf-8')):    
                for (i, datum) in enumerate(enumer(data_line)):
                    setattr(self, self.__attributemap__[i], valer(datum))

        attributes = {}
        attribute_map = {}
        attributes["__attributemap__"] = attribute_map
        
        for (i, header) in enumerate(headers):
            header = self.sanitize(header, attribute_map)
            attributes[header] = ""
            attribute_map[i] = header

        return type("Value", (ValueBase,), attributes)













