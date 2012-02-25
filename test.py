from csv import Csv

csv = Csv("test.csv")
for i in csv.read():
    print i.Name
    print dir(i)
    print i._2nd_name
