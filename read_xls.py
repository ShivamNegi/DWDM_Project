import xlrd

filename = raw_input("enter file location:")
workbook = xlrd.open_workbook(filename)

worksheet_name = raw_input("enter the name of worksheet")
worksheet = xlrd.sheet_by_name(worksheet_name)
