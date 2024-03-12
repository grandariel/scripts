#!/usr/bin/env python

import httplib2
import os
import datetime

from apiclient import discovery
from google.oauth2 import service_account

try:
    print("Saving weather...")

    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    secret_file = '/home/grand/scripts/client_secret.json'

    range_name = 'Sheet1!A1'
    sheet_id = '1dUFAWY5aM3p3AqM9FQwctufudNxj2466q9aTShLYfxA'

    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=SCOPES)
    service = discovery.build('sheets', 'v4', credentials=credentials)


    values = [
        ['a1', 'b1', 'c1', datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
    ]

    data = {
        'values': values
    }

    sheet = service.spreadsheets().values()
    sheet.append(spreadsheetId=sheet_id, body=data, range=range_name, valueInputOption='USER_ENTERED').execute()

    print("Saved.")
except OSError as e:
    print(e)
