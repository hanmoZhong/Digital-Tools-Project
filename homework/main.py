import requests
import sqlite3
from datetime import datetime
from datetime import date
import json
import pandas as pd
import csv


ROOT_URL = "https://api.stlouisfed.org/fred/series/observations?series_id=DEXUSAL&api_key=4f7fcecc2234fbd09478ce8b8f0a3725&file_type=json"
response = requests.get(ROOT_URL).json()
crawl_list = []
# configure database
def config_db():
    global con, cur
    con = sqlite3.connect('currency_data.db')
    cur = con.cursor()
    # create table user
    sql = "CREATE TABLE IF NOT EXISTS currencydata(date TEXT PRIMARY KEY, currency TEXT)"
    cur.execute(sql)


for dict in response['observations']:
    # convert str to datetime
    date_object = datetime.strptime(dict.get('date'), '%Y-%m-%d').date()
    date_now = date.today()
    years_to_add = date_now.year - 1
    # date_1 means last year of totay, date2 means current date
    date_1 = date_now.strftime('%Y-%m-%d')
    d1 = datetime.strptime(date_1, '%Y-%m-%d').date()
    date_2 = date_now.replace(year=years_to_add).strftime('%Y-%m-%d')
    d2 = datetime.strptime(date_2, '%Y-%m-%d').date()
    if (date_object>=d2) and (date_object <= d1):
        currency=dict.get('value')
        d=str(date_object)
        tuple=(d,currency)
        crawl_list.append(tuple)


with open('crawl_list.txt', 'w') as f:
    for i in crawl_list:
        f.write(str(i))
        f.write('\n')

# open the file in the write mode
with open('crawl_list.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)
    for i in crawl_list:
    # write a row to the csv file
        writer.writerow(i)


config_db()
for i in crawl_list:
    sql = "replace into currencydata(date, currency) values (?, ?)"
    cur.execute(sql,(i[0],i[1]))
    con.commit()

# close the cursor
cur.close()
# disconnect the database connection
con.close()

