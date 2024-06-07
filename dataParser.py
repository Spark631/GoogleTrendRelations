import json
import datetime


def dataParser(trendName):

    dataList = []

    with open(f"data/{trendName}.txt", 'r') as cheeseFile:
        data = cheeseFile.read()  

    dataJson = json.loads(data.replace("'", "\""))  
    iot = (dataJson['interest_over_time'])
    tld = (iot['timeline_data'])

    for stuff in tld:
        dataValue = stuff.get('values')[0].get('extracted_value')
        # print(dataValue)
        dataList.append(dataValue)
    return(dataList)
    # timestamp = 1685232000
    # dt = datetime.datetime.fromtimestamp(timestamp)
    # print(dt)