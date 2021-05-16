import requests,sys, io
import datetime
import saveInRedis
def start():
    if sys.version_info >= (3, 6):
        import zipfile
    else:
        import zipfile36 as zipfile

    headers={
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
    }



    todays_date = datetime.datetime.now()

    print(todays_date.strftime('%d%m%y'))
    formattedDate = todays_date.strftime('%d%m%y')
    BhavCopyUrl = f"https://www.bseindia.com/download/BhavCopy/Equity/EQ{formattedDate}_CSV.zip"


    for i in range(7):
        while True:
            try:
                a=requests.get(BhavCopyUrl,headers=headers)
            except requests.ConnectionError:
                print('No connection, retrying')
            break
    print(a.status_code)

    if a.status_code==200:
            z = zipfile.ZipFile(io.BytesIO(a.content), 'r')
            z.extractall()
            z.close()

start()
print(saveInRedis.setUp('ACC'))
