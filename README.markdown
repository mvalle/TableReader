SimpleCSV: A simple Pythonic CSV library
====================================
A library for processing tabular data.
The library will generate a new class based on the datafile, enableing the user to refer to the columns by name.


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

Naming
------
Headers in CSV files can be anything, as long it does not have a comma.
SimpleCSV tries to convert headers that are not valid Python.

* Spaces are converted into underlines, "First Name" => "First_Name"
* Numbers as the first character are prefixed with undersocres, "1st Name" => "_1st_Name"

Supported Formats
-----------------
Supports CSV files and Xls spreadsheets.

