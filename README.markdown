PyCSV: A simple Pythonic CSV library
====================================

It enables the user to process the CSV by the name of the column.

Example
--------------------
example.csv

```
Name, URL
GitHub, www.github.com
SourceForge, www.sourceforge.com
```

example.py

```python
from csv import Csv
csv = Csv("path_to_file/websites.csv")
for row in csv.read():
    # process the file.
    name = row.Name
    url = row.URL
```

Naming
------
Headers in CSV files can be anything, as long it does not have a comma.
SimpleCSV tries to convert headers that are not valid Python.
* Spaces are converted into underlines, "First Name" => "First_Name"
* Numbers as the first character are prefixed with undersocres, "1st Name" => "_1st_Name"


