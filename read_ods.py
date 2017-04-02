import pyexcel_ods as pyod
from collections import OrderedDict

filename = raw_input("enter file location:")
data = pyod.get_data(filename)

sheets = [
    "North_East",
    "North_West",
    "Yorks_&_The_Humber",
    "East_Midlands",
    "West_Midlands",
    "East",
    "London",
    "South_East",
    "South_West",
    "England",
    "Wales",
    "Scotland",
    "Northern_Ireland",
    "3yr_average"]

for sheet in sheets:
    data[sheet] = data[sheet][7:]
