#!/usr/bin/env python

import httplib2
import os
import time

from datetime import datetime
from gpiozero import CPUTemperature

from weather_tracker_auth import sheet
from weather_tracker_auth import sheet_id

def main():
    try:        
        insertRow()
        pasteData(getWeather())
        print("Saved successfully.")
    except OSError as e:
        print(e)

def getWeather():
    temp = str(CPUTemperature().temperature)
    date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    values = [temp, 'b1', 'c1', date]
    print(values)
    return ','.join(values)

def insertRow():
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

def pasteData(data):
    body = {
        'requests': { 
            'pasteData': {
                "coordinate": {
                    "sheetId": 0,
                    "rowIndex": 1,
                    "columnIndex": 0
                },
                "data": data,
                "delimiter": ','
            }
        }
    }
    sheet.batchUpdate(spreadsheetId=sheet_id,body=body).execute()

if __name__ == "__main__":
    print("Saving weather...")
    start = time.time()
    
    main()
    
    end = time.time()
    print("Script took " + str(round(end - start, 2)) + "s")
