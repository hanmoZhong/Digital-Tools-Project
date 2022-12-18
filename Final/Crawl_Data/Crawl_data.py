import requests
import sqlite3
from datetime import datetime
from datetime import date
import csv

ROOT_URL_DEXSDUS = "https://api.stlouisfed.org/fred/series/observations?series_id=DEXSDUS&api_key=4f7fcecc2234fbd09478ce8b8f0a3725&file_type=json"
ROOT_URL_DEXUSNZ = "https://api.stlouisfed.org/fred/series/observations?series_id=DEXUSNZ&api_key=4f7fcecc2234fbd09478ce8b8f0a3725&file_type=json"
ROOT_URL_DEXCAUS = "https://api.stlouisfed.org/fred/series/observations?series_id=DEXCAUS&api_key=4f7fcecc2234fbd09478ce8b8f0a3725&file_type=json"
ROOT_URL_DEXJPUS = "https://api.stlouisfed.org/fred/series/observations?series_id=DEXJPUS&api_key=4f7fcecc2234fbd09478ce8b8f0a3725&file_type=json"
ROOT_URL_DEXNOUS = "https://api.stlouisfed.org/fred/series/observations?series_id=DEXNOUS&api_key=4f7fcecc2234fbd09478ce8b8f0a3725&file_type=json"
ROOT_URL_DEXSZUS = "https://api.stlouisfed.org/fred/series/observations?series_id=DEXSZUS&api_key=4f7fcecc2234fbd09478ce8b8f0a3725&file_type=json"
ROOT_URL_DEXUSEU = "https://api.stlouisfed.org/fred/series/observations?series_id=DEXUSEU&api_key=4f7fcecc2234fbd09478ce8b8f0a3725&file_type=json"
ROOT_URL_DEXUSUK = "https://api.stlouisfed.org/fred/series/observations?series_id=DEXUSUK&api_key=4f7fcecc2234fbd09478ce8b8f0a3725&file_type=json"
ROOT_URL_DEXUSAL = "https://api.stlouisfed.org/fred/series/observations?series_id=DEXUSAL&api_key=4f7fcecc2234fbd09478ce8b8f0a3725&file_type=json"

response_DEXSDUS = requests.get(ROOT_URL_DEXSDUS).json()
response_DEXUSNZ = requests.get(ROOT_URL_DEXUSNZ).json()
response_DEXCAUS = requests.get(ROOT_URL_DEXCAUS).json()
response_DEXJPUS = requests.get(ROOT_URL_DEXJPUS).json()
response_DEXNOUS = requests.get(ROOT_URL_DEXNOUS).json()
response_DEXSZUS = requests.get(ROOT_URL_DEXUSEU).json()
response_DEXUSEU = requests.get(ROOT_URL_DEXUSEU).json()
response_DEXUSUK = requests.get(ROOT_URL_DEXUSUK).json()
response_DEXUSAL = requests.get(ROOT_URL_DEXUSAL).json()


crawl_list=[]
# configure database
def config_db():
    global con, cur
    con = sqlite3.connect('currency_data.db')
    cur = con.cursor()
    # create table user
    sql = "CREATE TABLE IF NOT EXISTS currencydata(date TEXT PRIMARY KEY, currencyal TEXT, currencyuk TEXT, " \
          "currencyeu TEXT, currencysz TEXT, currencyno TEXT, currencyjp TEXT, currencyca TEXT, currencynz TEXT, currencysd TEXT ) "
    cur.execute(sql)


for dict in response_DEXUSAL['observations']:
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
        try:
            currencyal=round(1/float(dict.get('value')),4)
        except:
            currencyal="."
        d=str(date_object)
        tuple=(d,currencyal)
        crawl_list.append(tuple)

for dict in response_DEXUSUK['observations']:
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
        try:
            currencyuk=round(1/float(dict.get('value')),4)
        except:
            currencyuk="."
        d=str(date_object)
        tuple=(d,currencyuk)
        crawl_list.append(tuple)


for dict in response_DEXUSEU['observations']:
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
        try:
            currencyeu=round(1/float(dict.get('value')),4)
        except:
            currencyeu="."
        d=str(date_object)
        tuple=(d,currencyeu)
        crawl_list.append(tuple)

for dict in response_DEXSZUS['observations']:
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
        currencysz=dict.get('value')
        d=str(date_object)
        tuple=(d,currencysz)
        crawl_list.append(tuple)


for dict in response_DEXNOUS['observations']:
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
        currencyno=dict.get('value')
        d=str(date_object)
        tuple=(d,currencyno)
        crawl_list.append(tuple)


for dict in response_DEXJPUS['observations']:
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
        currencyjp=dict.get('value')
        d=str(date_object)
        tuple=(d,currencyjp)
        crawl_list.append(tuple)

for dict in response_DEXCAUS['observations']:
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
        currencyca=dict.get('value')
        d=str(date_object)
        tuple=(d,currencyca)
        crawl_list.append(tuple)

for dict in response_DEXUSNZ['observations']:
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
        try:
            currencynz=round(1/float(dict.get('value')),4)
        except:
            currencynz="."
        d=str(date_object)
        tuple=(d,currencynz)
        crawl_list.append(tuple)

for dict in response_DEXSDUS['observations']:
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
        currencysd=dict.get('value')
        d=str(date_object)
        tuple=(d,currencysd)
        crawl_list.append(tuple)

crawl_dict ={}

for k_v in crawl_list:

    k, v = k_v

    crawl_dict.setdefault(k, []).append(v)


list = [(k, v) for k, v in crawl_dict.items()]
outputlist=[]
for i in list:
    tuple=(i[0],i[1][0],i[1][1],i[1][2],i[1][3],i[1][4],i[1][5],i[1][6],i[1][7],i[1][8])
    outputlist.append(tuple)

# open the file in the write mode
with open('crawl_list.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)
    writer.writerow(['date', 'currencyal', 'currencyuk', 'currencyeu', 'currencysz', 'currencyno', 'currencyjp', 'currencyca', 'currencynz', 'currencysd'])
    for i in outputlist:
        # write a row to the csv file
        writer.writerow(i)



config_db()
for i in list:
    sql = "replace into currencydata(date, currencyal, currencyuk, currencyeu, currencysz, currencyno, currencyjp, currencyca, currencynz, currencysd) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cur.execute(sql,(i[0],i[1][0],i[1][1],i[1][2],i[1][3],i[1][4],i[1][5],i[1][6],i[1][7],i[1][8]))
    con.commit()

# close the cursor
cur.close()
# disconnect the database connection
con.close()

