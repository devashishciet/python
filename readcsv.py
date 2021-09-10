import xlrd
loc = ("D:\\Python Tutorial\\Code\\certificate.xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
for i in range(10):
    print(sheet.cell_value(i, 1))
