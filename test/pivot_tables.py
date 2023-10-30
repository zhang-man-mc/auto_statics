

from openpyxl import load_workbook


def refresh_pivot_table(filename, sheet_name, pivot_table_range):
    workbook = load_workbook(filename)
    try:
        sheet = workbook[sheet_name]
        print(sheet.pivot_tables)
        # for pivot_table in sheet._pivot_tables:
        #     if pivot_table.range.ref == pivot_table_range:
        #         pivot_table.cache.refreshOnLoad = True
        # workbook.save('111')
    finally:
        workbook.close()


filename = '../徐汇餐饮-小程序.xlsx'
sheet_name = '台账和自巡查提交情况'
pivot_table_range = 'v14:X177'

refresh_pivot_table(filename, sheet_name, pivot_table_range)
