from ExcelOperations import read_sheet
import re


def cumulate_stocks(asset, destination, master_data):
    stocks_info = dict()
    for fund in master_data.keys():
        file_path = destination + "/" + master_data[fund]["file_name"]
        sheet_name = master_data[fund]["sheet_name"]
        sheet = read_sheet(file_path, sheet_name)
        stocks_from_one_fund(sheet, stocks_info, asset[fund], sheet_name)

    return stocks_info


def stocks_from_one_fund(sheet, stocks_info, invested_amount, sheet_name):

    stocks_column = get_stocks_column(sheet)
    isin_coloumn = get_ISIN_column(sheet)
    row_start = get_row_start(sheet)
    row_end = get_row_end(sheet)

    if is_percentage_factored_in(sheet,row_start,row_end,stocks_column, isin_coloumn, sheet_name):
        division_factor = 1
    else:
        division_factor = 100

    for row_index in range(row_start, row_end):

        if check_addition_validity(sheet, row_index,stocks_column, isin_coloumn):
            try:
                if sheet[row_index][isin_coloumn] in stocks_info:
                    stocks_info[sheet[row_index][isin_coloumn]] += invested_amount * float(sheet[row_index][stocks_column]) / division_factor
                else:
                    stocks_info[sheet[row_index][isin_coloumn]] = invested_amount * float(
                        sheet[row_index][stocks_column]) / division_factor
            except ValueError:
                print("Character error :  " + sheet[row_index][stocks_column] + " in "+ sheet_name)

    return stocks_info


def check_addition_validity(sheet, row_index,stocks_column, isin_coloumn):
    if sheet[row_index][stocks_column] != "NIL" \
            and sheet[row_index][isin_coloumn]!= None \
            and sheet[row_index][stocks_column] != None \
            and len(str(sheet[row_index][isin_coloumn])) != 0:
        return True
    else:
        return False


def get_stocks_column(sheet):
    if sheet is not None:
        for row in sheet:
            for column_index in range(len(row)):
                cell_value = row[column_index]
                if str(cell_value).find('%') != -1 or re.search("percent", str(cell_value), re.IGNORECASE):
                    return column_index

    return None


def get_ISIN_column(sheet):
    if sheet is not None:
        for row in sheet:
            for column_index in range(len(row)):
                cell_value = row[column_index]
                if re.search("isin", str(cell_value), re.IGNORECASE):
                    return column_index

    return None


def get_row_start(sheet):
    if sheet is not None:
        for row_index in range(len(sheet)):
            for cell_value in sheet[row_index]:
                if str(cell_value).find("Listed") != -1:
                    return row_index + 1  # since row after this row is where it starts

    return None


def get_row_end(sheet):
    if sheet is not None:
        for row_index in range(len(sheet)):
            for cell_value in sheet[row_index]:
                if (re.search('total', str(cell_value), re.IGNORECASE)) and not (
                re.search('sub', str(cell_value), re.IGNORECASE)):
                    return row_index - 1  # since row before this is where it ends

    return None


def is_percentage_factored_in(sheet, row_start, row_end, percentage_column, isin_column, sheet_name):
    sum = 0
    if row_end!= None and row_start!= None:
        for row_index in range(row_start, row_end):
            if check_addition_validity(sheet,row_index,percentage_column, isin_column):
                try:
                    sum = sum + float(sheet[row_index][percentage_column])
                except ValueError:
                   print("Character error : " + sheet[row_index][percentage_column] + " in "+ sheet_name)

        if sum<=10:
            return True
        else:
            return False
