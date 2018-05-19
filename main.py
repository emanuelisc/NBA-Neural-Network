import requests
import json
import urllib

teamId = '1610612751'
season = '2014-15'

# To use data from API (PHP project on local server) ->
# page = urllib.request.urlopen('http://localhost/nba/php/index.php?teamId=' + teamId + '&season=' + season)
# byte = page.read()
# text = byte.decode("utf-8")
# text = text[1:] 
# text = text[0:len(text)-1]+text[len(text):]
# data = json.loads(text)

# To use test data ->
with open('data.json') as f:
    data = json.load(f)

results = data["resultSets"][0]["rowSet"]
# print(len(results))php
with open('preparedData.txt', 'w') as f:
    printData = ""
    for i in results:
        printData += str(i[3]) + " "
        printData += str(i[4]) + " "
        printData += str(i[26])
        printData += "\n"
    f.write(printData)
