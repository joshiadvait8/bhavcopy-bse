import json
import redis
from django.http import JsonResponse
r = redis.Redis(host='localhost', port=6379, db=0)

def queryData(request):
    try:
        data = json.loads(request.body)
        searchKey = data['query'].upper()
        x = r.keys(pattern=searchKey+"*")
        simpleX = [i.decode('utf-8') for i in x]
        resultList=[]
        for i in simpleX:
            resultDict = {}
            # Converting
            for key, value in r.hgetall(i).items():
                resultDict[key.decode("utf-8")] = value.decode("utf-8")
            resultList.append(resultDict)
        return JsonResponse({'result':resultList})
    except Exception as e:
        import traceback
        print(e)
        print(traceback.format_exc())