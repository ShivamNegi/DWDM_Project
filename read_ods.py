import pyexcel_ods as pyod
from collections import OrderedDict

filename = raw_input("enter file location:")
data = pyod.get_data(filename)
new_data = OrderedDict()
