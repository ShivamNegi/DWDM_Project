import pyexcel_ods as pyod
from collections import OrderedDict

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
    "Energy"
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



def preprocess(data):
    for sheet in sheets:
        data[sheet] = data[sheet][7:]
    return data

def preprocess_remove_citation(data):
    for sheet in sheets:
        data[sheet] = data[sheet][:-13]
    return data

def preprocess_remove_extra_params(data):
    for sheet in sheets:
        data[sheet] = data[sheet][:-28]
    return data

def preprocess_description(data, new_data):
    for sheet in sheets:
        k = data[sheet]
        k_new = []
        for i in range(len(k)):
            if i < 3:
                k_new.append(k[i])
            elif k[i][1] in description:
                k_new.append(k[i])
        new_data[sheet] = k_new
    return new_data


def write_data(data):
    filename = raw_input("Enter file to write to:")
    pyod.write_data(filename, data)


def write_newdata(new_data):
    filename = raw_input("Enter filename to write to:")
    pyod.write_data(filename, new_data)


def main():
    outside_filename = raw_input("Enter outside file name:")
    inside_filename = raw_input("Enter inside file name:")
    data = pyod.get_data(outside_filename)
    new_data = OrderedDict()

    data = preprocess(data)
    data = preprocess_remove_citation(data)
    data = preprocess_remove_extra_params(data)
    new_data = preprocess_description(data, new_data)
    write_newdata(new_data)

    data = pyod.get_data(inside_filename)
    new_data = OrderedDict()

    data = preprocess(data)
    data = preprocess_remove_citation(data)
    data = preprocess_remove_extra_params(data)
    new_data = preprocess_description(data, new_data)
    write_newdata(new_data)


if __name__ == '__main__':
    main()
