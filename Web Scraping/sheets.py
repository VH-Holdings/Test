import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("My Database").sheet1

data = sheet.get_all_records()

row = sheet.row_values(3)
col = sheet.col_values(3)
cell = sheet.cell(3,3).value

insertRow = [12, "Subaru", "Forester", 2019, 0, "Manual", "Petrol", 1000000]

sheet.insert_row(insertRow, 13)

pprint(cell)