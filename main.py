import requests
import json
import urllib

from urllib3.connectionpool import xrange
from numpy import exp, array, random, dot

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
    counter = 1
    for i in range(len(results)):
        if (i + 10) < len(results):
            arr = []
            for j in range(10):
                arr.append(results[i+j][26])
            training_set_outputs.append(results[i+10][26])
            training_set_inputs.append(arr)
        printData += str(counter) + "\t"
        printData += str(results[i][26])
        printData += "\n"
        counter += 1
    f.write(printData)

training_set_outputs = array(training_set_outputs).T
training_set_inputs = array(training_set_inputs)
random.seed(1)
synaptic_weights = 2 * random.random((10, 1)) - 1
for iteration in range(72):
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))

    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs[iteration]- output) * output * (1 - output))
print (1 / (1 + exp(-(dot(array([78, 100, 100,  81, 104,  85,  87, 110, 93, 100]), synaptic_weights)))))

# training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
# training_set_outputs = array([[0, 1, 1, 0]]).T
# random.seed(1)
# synaptic_weights = 2 * random.random((3, 1)) - 1
# for iteration in xrange(10000):
#     output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
#     synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
