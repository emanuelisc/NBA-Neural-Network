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

training_set_inputs = []
training_set_outputs = []
with open('scores.txt', 'w') as f:
    printData = ""
    for i in range(len(results)):
        if (i + 10) < len(results):
            arr = []
            for j in range(10):
                arr.append(results[i+j][26])
            training_set_outputs.append(results[i+10][26])
            training_set_inputs.append(arr)
        printData += str(results[i][26]) + "\t"
        if results[i][5] == "W":
            printData += str(results[i][26] - randint(0, 25))
        else:
            printData += str(results[i][26] + randint(0, 25))
        printData += "\n"
    f.write(printData)
