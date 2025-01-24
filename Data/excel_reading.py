import xlrd
path = r'C:\Users\7000040947\PycharmProjects\PythonProject\Excel_Files\Test_data.xls'
work_book = xlrd.open_workbook(path)
sheet_name = work_book.sheet_by_name('Sheet1')
rows = sheet_name.get_rows()
header = next(rows)

def search_data():
    data = [ele[0].value for ele in rows]
    return data


sheet_name1 = work_book.sheet_by_name('Sheet2')
rows1 = sheet_name1.get_rows()
header1 = next(rows1)
def get_data():
    data = [(row[0].value,row[1].value)for row in rows1]
    return data


sheet_name2 = work_book.sheet_by_name('Sheet3')
rows2 = sheet_name2.get_rows()
header2 = next(rows2)
def get_links():
    data = [(ele[0].value ,ele[1].value)for ele in rows2]
    return data

sheet_name3 = work_book.sheet_by_name('Sheet5')
rows3 = sheet_name3.get_rows()
header3 = next(rows3)
def get_games():
    data = [ele[0].value for ele in rows3]
    return data