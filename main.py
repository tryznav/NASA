import requests
from pprint import PrettyPrinter
from datetime import date
import sqlite3
import json

#Get data from NASA
pp = PrettyPrinter()
api_key = '697qN29kSf1FlGwDtj9fnDuPqUbvDGIC1JzPRlKY'
API_URL = "https://api.nasa.gov/planetary/apod"
DATA_BASE = 'test.db'

def fetchDailyData():
  today = date.today()
  print("Today's date:", today)
  params = {
      'api_key':api_key,
      'date':today,
      'hd':'True'
  }
  return today, requests.get(API_URL,params=params).json()

def putDataToDatabase(day, data):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS some_data(day date, data json)")
    cursor.execute("INSERT INTO some_data values(?,?)", [day, json.dumps(data)])
    conn.commit()
    conn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day, dailyData = fetchDailyData()
    putDataToDatabase(day, dailyData)
