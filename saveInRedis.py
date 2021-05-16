import csv, redis, json, glob, os
import sys
import datetime

def getLatestFile():
    list_of_files = glob.glob('*.CSV') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(type(list_of_files))
    return latest_file

def setUp(searchKey):
    r = redis.Redis(host='localhost', port=6379, db=0)
    
    csv_file = getLatestFile()
    #read csv data and store in redis hash
    read_csv_data(r,csv_file)
    #get json data of redis output
    return getJsonData(r,searchKey)


def read_csv_data(r,csv_file):
    r.flushdb()
    with open(csv_file) as csvf:
        csv_data = csv.reader(csvf)
        for row in csv_data:
            data = {
                "code":row[0],
                "name":(row[1]).strip(),
                "open":row[4],
                "high":row[5],
                "low":row[6],
                "close":row[7]
            }
            r.hmset((row[1]).strip(),data)
            # print(row[1].strip()+"knnknk")


def printData():
    
    r = redis.Redis(host='localhost', port=6379, db=0)
    print(r.hgetall("BHEL"))
    x = r.keys(pattern="LU*")
    x = [i.decode('utf-8') for i in x]
    # x = json.loads(r.hgetall("BHEL"))
    # print(x)
    print(x)

def getJsonData(r,searchKey):
    x = r.keys(pattern=searchKey+"*")
    simpleX = [i.decode('utf-8') for i in x]

    # print(r.hgetall(simpleX[0]).keys())
    resultList=[]
    for i in simpleX:
        resultDict = {}
        # Converting
        for key, value in r.hgetall(i).items():
            resultDict[key.decode("utf-8")] = value.decode("utf-8")
        resultList.append(resultDict)
    return json.dumps(resultList)
    



# print(setUp("ACC"))