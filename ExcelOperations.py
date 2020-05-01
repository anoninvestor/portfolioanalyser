import gc
import xlrd
import pyxlsb


# returns list of lists
def read_all_format(input_file, sheet_name):
    try:
        book = xlrd.open_workbook(input_file)
        sheet = book.sheet_by_name(sheet_name)
    except xlrd.biffh.XLRDError:
        raise ValueError()

    sheet_as_list = []
    for row_iter in range(sheet.nrows):
        row = list()
        for col_iter in range(sheet.ncols):
            if sheet.cell(row_iter, col_iter).ctype != 0:
                row.append(sheet.cell(row_iter, col_iter).value)
            else:
                row.append(None)
        sheet_as_list.append(row)

    del book
    del sheet
    gc.collect()

    return sheet_as_list


# use this for reading the xlsb files; returns a list of lists
def read_xlsb(input_file, sheet_name):
    book = pyxlsb.open_workbook(input_file)
    sheet = book.get_sheet(sheet_name)

    sheet_as_list =[]
    for row in sheet.rows():
        row_for_list=[]
        for cell in row:
            row_for_list.append(cell.v)
        sheet_as_list.append(row_for_list)

    del book
    del sheet
    gc.collect()

    return sheet_as_list


def read_sheet(input_file, sheet_name):
    try:
        dot_position = input_file.rfind(".")
        file_format = input_file[dot_position+1:len(input_file)].lower()

        if file_format == "xlsb":
            return read_xlsb(input_file, sheet_name)
        else:
            return read_all_format(input_file, sheet_name)
    except FileNotFoundError:
        print("Check file path; Input :" + input_file)
    except ValueError:
        print("Check sheet name : " + sheet_name)

