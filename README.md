# Bhavcopy BSE
Application for downloading bhavcopy from BSE at 6 pm and serving it to user for searching open,high,low,close data for scrips also they can export results that they have searched


## Demo

  <img width="200" src=demo.gif>

## Deployed application live Link
- [Go to live application ](http://3.143.224.198:8000/app/)


## Local setup

### clone repo
```
git clone https://github.com/joshiadvait8/bhavcopy-bse.git
```

### Install and setup redis server locally if you haven't already
follow download an setup instructions
```
https://redis.io/download
```

### Install dependencies
```
pip install requirements.txt
```

### setup a cronjob on linux or task scheduler on windows
```
crontab download.cron
```
### Run Django Application server locally
go into folder where mange.py file is there inside project and then run
```
python manage.py runserver
```
Your application will start running at 127.0.0.0.1:8000/app
:smiley:

### Technology Stack
  - python
  - Django
  - Redis
  - Vue
