import csv

filename = raw_input("enter file location:")
with open(filename, "rb") as f:
    reader = csv.reader(f, delimiter=' ', quotechar='|')
    for row in reader:
        print row
