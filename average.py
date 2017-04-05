import pyexcel_ods as pyod
from collections import OrderedDict
from preprocess_ods import sheets

Accepted = [284,
61,
1,
1.31,
34.5,
0.126,
0.165,
0.203,
5.74,
0.44]


def preprocess_columns(data):
    for sheet in sheets:
        data[sheet] = data[sheet][0][:-4]
        for i in range(2, 12):
            data[sheet][i] = data[sheet][i][:-2]
    return data


def adding_accvalues(data):
    for sheet in sheets:
        data[sheet][0].append("Accepted Values")
        for i in range(2, 12):
            data[sheet][i].append(Accepted[i - 2])
    return data


def adding_class(data):
    new_data = OrderedDict()
    for sheet in sheets:
        k_new = []
        for i in range(2, 12):
            k_new = []
            for k in range(4, 18):
                if data[sheet][i][-1] > data[sheet][i][k]:
                    data[sheet][i].insert("N", i + 1)
                else:
                    data[sheet][i].append("Y")
    return data


def write_data(data):
    filename = raw_input("Enter file to write to:")
    pyod.write_data(filename, data)


def div_10(data):
    for sheet in sheets:
        for i in range(2, 12):
            for k in range(4, 18):
                try:
                    data[sheet][i][k] = data[sheet][i][k] / 10
                except:
                    print(k)
    return data

def main(data, new_data):
    for sheet in sheets:
        k_new = []
        for i in range(12):
            if i == 0:
                data[sheet][i].append("Average")
            elif i == 1:
                pass
            else:
                try:
                    value = sum(data[sheet][i][4:17]) / 13
                    data[sheet][i].append(value)
                except:
                    print(i, sheet)
            k_new.append(data[sheet][i])
        new_data[sheet] = k_new
    return new_data

if __name__ == '__main__':
    filename = raw_input("Enter inside file name:")
    data = pyod.get_data(filename)
    new_data = OrderedDict()
    data = div_10(data)
    new_data = main(data, new_data)
    new_data = adding_accvalues(new_data)
    new_data = adding_class(new_data)
    write_data(new_data)
