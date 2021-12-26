import pandas as pd
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def auth():
    SP_CREDENTIAL_FILE = 'secret.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = 'SP_SHEET_KEY'
    SP_SHEET = 'SP_SHEET'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet
    worksheet = auth()


df = pd.DataFrame(worksheet.get_all_records())

timestamp = datetime.now()
date = timestamp.strftime('%Y/%m/%d')
date

punch_in = timestamp.strftime('%H:%M')
punch_in

df = df.append({'日付': date, '出勤時間': punch_in,
               '退勤': '00:00'}, ignore_index=True)
df
worksheet.update([df.columuns.values.tolist()] + df.values.tolist())

# array(['日付','出勤','退勤時間'], dtype=object)
