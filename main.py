import requests
import json
from random import randint
import urllib
import numpy as np
from urllib3.connectionpool import xrange
from numpy import exp, array, random, dot
from random import randint

teamId = '1610612751'
season = '2014-15'

with open('teams.json') as f:
    teamData = json.load(f)

teams = dict()
counter = 1
for i in teamData:
    teams[i["abbreviation"]] = counter
    counter += 1
teams["NJN"] = counter
counter += 1
teams["NOH"] = counter
counter += 1
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

with open('scores.txt', 'w') as f:
    printData = ""
    for i in range(len(results)):
        printData += str(teams[results[i][3][:3]]) + "\t"
        printData += str(teams[results[i][3][-3:]]) + "\t"
        printData += str(results[i][26]) + "\t"
        if results[i][5] == "W":
            printData += str(results[i][26] - randint(0, 25))
        else:
            printData += str(results[i][26] + randint(0, 25))
        printData += "\n"
    f.write(printData)
