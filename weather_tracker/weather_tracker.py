#!/usr/bin/env python

import httplib2
import os
import time

from datetime import datetime 
from apiclient import discovery
from google.oauth2 import service_account

try:
    start = time.time()
    print("Saving weather...")

    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    secret_file = os.path.expanduser('~') + "/scripts/weather_tracker/.client_secret.json"

    range_name = 'Sheet1!A1'
    sheet_id = '1dUFAWY5aM3p3AqM9FQwctufudNxj2466q9aTShLYfxA'

    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=SCOPES)
    service = discovery.build('sheets', 'v4', credentials=credentials)

    values = ['a1', 'b1', 'c1', datetime.now().strftime('%d/%m/%Y %H:%M:%S')]
    print(values)

    sheet = service.spreadsheets()
    
    body = {
        'requests': {
            'insertDimension': {
                "range": {
                "sheetId": 0,
                "dimension": "ROWS",
                "startIndex": 1,
                "endIndex": 2 
                },
                "inheritFromBefore": False
            },
        }
    }
    sheet.batchUpdate(spreadsheetId=sheet_id,body=body).execute()
    
    body = {
        'requests': { 
            'pasteData': {
                "coordinate": {
                    "sheetId": 0,
                    "rowIndex": 1,
                    "columnIndex": 0
                },
                "data": ','.join(values),
                "delimiter": ','
            }
        }
    }
    sheet.batchUpdate(spreadsheetId=sheet_id,body=body).execute()

    print("Saved successfully.")

    end = time.time()
    print("Script took " + str(round(end - start, 2)) + "s")
except OSError as e:
    print(e)
