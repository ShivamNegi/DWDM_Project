import pyexcel_ods as pyod
from collections import OrderedDict

filename = raw_input("enter file location:")
data = pyod.get_data(filename)
new_data = OrderedDict()

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

description = [
    "Protein",
    "Vitamin D",
    "Thiamin",
    "Riboflavin",
    "Vitamin B6",
    "Vitamin C",
    "Calcium",
    "Magnesium",
    "Iron",
    "Zinc"]

def preprocess():
    for sheet in sheets:
        data[sheet] = data[sheet][7:]

def preprocess_remove_citation_rural():
    for sheet in sheets:
        data[sheet] = data[sheet][:-8]

def preprocess_remove_citation_urban():
    for sheet in sheets:
        data[sheet] = data[sheet][:-13]

def preprocess_remove_extra_params_():
    for sheet in sheets:
        data[sheet] = data[sheet][:-28]

def preprocess_description():
    for sheet in sheets:
        k = data[sheet]
        k_new = []
        for i in range(len(k)):
            if i < 3:
                k_new.append(k[i])
                continue
            if k[i][1] in description:
                k_new.append(k[i])
        new_data[sheet] = k_new


def write_data():
    filename = raw_input("Enter file to write to:")
    pyod.write_data(filename, data)


def write_newdata():
    filename = raw_input("Enter file to write to:")
    pyod.write_data(filename, new_data)
