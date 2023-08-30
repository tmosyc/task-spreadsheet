import gspread
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv
load_dotenv()

def connect():
    scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']
    credentials = Credentials.from_service_account_file(".key/task-spreedsheet-ef930c974f9d.json", scopes=scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = os.environ.get("SHEET_ID")
    workbook = gc.open_by_key(SPREADSHEET_KEY)
    worksheet = workbook.worksheet('シート1')
    return worksheet

def insert(title, content):
    worksheet = connect()
    list_of_lists = worksheet.get_all_values()
    length = len(list_of_lists)
    insert_row = length + 1
    worksheet.update_cell(insert_row, 1, title)
    worksheet.update_cell(insert_row, 2, content)

