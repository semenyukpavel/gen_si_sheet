import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = '/Users/semenyukpavel/Desktop/Generate SI Sheets-83a145682a5c.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

# spreadsheet = service.spreadsheets().create(body={
#     'properties': {'title': 'Таблица 1', 'locale': 'ru_RU'},
#     'sheets': [{'properties': {'sheetType': 'GRID',
#                                'sheetId': 0,
#                                'title': 'Лист 1',
#                                'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]}).execute()
#
# print(spreadsheet)



driveService = apiclient.discovery.build('drive', 'v3', http=httpAuth)
shareRes = driveService.permissions().create(
    fileId='13tDqPtQx8KL-tJY7h_Yc5NhSjuRvthYxgRmobFD9Msw',
    body={'type': 'user', 'role': 'writer', 'emailAddress': 'semenyukpavel@googlemail.com'},
    fields='id'
).execute()

