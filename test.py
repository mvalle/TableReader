from csv import Csv

csv = Csv("test.csv")
for i in csv.read():
    print i.Name
