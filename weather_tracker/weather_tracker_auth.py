import os
from apiclient import discovery
from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
secret_file = os.path.expanduser('~') + "/scripts/weather_tracker/.client_secret.json"

range_name = 'Sheet1!A1'
sheet_id = '1dUFAWY5aM3p3AqM9FQwctufudNxj2466q9aTShLYfxA'

credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=SCOPES)
service = discovery.build('sheets', 'v4', credentials=credentials)

sheet = service.spreadsheets()
