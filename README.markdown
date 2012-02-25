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
example
```python
from csv import Csv
csv = Csv("path_to_file/websites.csv")
for row in csv.read():
    # process the file.
    name = row.Name
    url = row.URL
```

