import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import datetime
import json


url = 'https://docs.google.com/spreadsheets/d/1XZAzKG8qKr9wD3xpN5_HsVulVlKAYrFzcLNzZPNOgk0/edit#gid=0'
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]

creds = ServiceAccountCredentials.from_json_keyfile_name('secrets.json', scopes=scopes)
client = gspread.authorize(credentials=creds)


# data = client.open_by_url(url)
# print(data.fetch_sheet_metadata().get('sheets'))
# student = data.sheet1
# print(student.get_all_values())

data = client.open_by_url(url)
workstem = data.sheet1
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
afterеtomorrow = today + datetime.timedelta(days=2)
workscheet2 = data.add_worksheet('dates', rows=100, cols=100)

Dates = ['Сьогодні', 'завтра', 'післязавтра']
Wdates =[today.strftime("%d.%m.%Y"), tomorrow.strftime("%d.%m.%Y"), afterеtomorrow.strftime("%d.%m%Y")]

df = pd.DataFrame(
    list(
        zip(
            Dates,
            Wdates,
        )
    ),
    columns=['День', 'Дата']
)
workscheet2.update(
    [df.columns.values.tolist()] + df.values.tolist()
)



# print(today)
# print(tomorrow.strftime('%d.%m'))
# print(afterеtomorrow.strftime('%d.%m'))