Table Reader: A simple Pythonic library for reading tabular data
================================================================
A library for processing tabular data.
The library will generate a new class based on the datafile, enableing the user to refer to the columns by their name. So if a data source has a column called Address, then the value class will have a attribute called "Address".

Example
--------------------
websites.csv

```
Name, URL
GitHub, http://www.github.com/
SourceForge, http://www.sourceforge.com/
```

example.py

```python
from reader import Csv
csv_file = Csv("path/to/file/websites.csv")
for row in csv_file.read():
    # process the file.
    print '<a href="%s">%s</a>' % (row.URL, row.Name)
```

Features
========
Allow the user to read data without lots of boilerplate code.


Supported Formats
-----------------
Reading CSV files
Reading Xls files

Planned Formats
---------------
Reading Xlsx files
Reading Ods files
Reading SQL databases
Reading HTML files with <table> tags.



Naming
------
Headers in data sources can be anything, as long as it is a valid Python identifier.
Table Reader tries to convert invalid header names, into valid names.

* Spaces are converted into underlines, "First Name" => "First_Name"
* Numbers as the first character are prefixed with undersocres, "1st Name" => "_1st_Name"
