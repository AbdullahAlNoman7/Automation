import openpyxl
wb = openpyxl.load_workbook("G:\\SQA\\Automation\\DataDriven\\Data1.xlsx")
print(wb)
sheet = wb.sheetnames
print(sheet)
print(wb.active.title)