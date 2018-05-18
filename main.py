import requests
import json
import urllib.request

teamId = '1610612751'
season = '2014-15'


page = urllib.request.urlopen('https://nba.shop4dev.com/index.php?teamId=' + teamId + '&season=' + season)
byte = page.read()
text = byte.decode("utf-8")
text = text[1:]
text = text[0:len(text)-1]+text[len(text):]

# # with open('data.json') as f:
data = json.loads(text)

results = data["resultSets"][0]["rowSet"]
print(len(results))
with open('preparedData.txt', 'w') as f:
    printData = ""
    for i in results:
        printData += str(i[3]) + " "
        printData += str(i[4]) + " "
        printData += str(i[26])
        printData += "\n"
    f.write(printData)
