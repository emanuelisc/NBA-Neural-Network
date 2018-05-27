import requests
import json
from random import randint
import urllib
import numpy as np
from urllib3.connectionpool import xrange
from numpy import exp, array, random, dot


def getDataFromApi():

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

    printData = ""

    for i in teamData:
        page = urllib.request.urlopen(
            'http://localhost/nba/php/index.php?teamId=' + str(i["teamId"]) + '&season=' + season)
        byte = page.read()
        text = byte.decode("utf-8")
        text = text[1:]
        text = text[0:len(text)-1]+text[len(text):]

        data = json.loads(text)

        results = data["resultSets"][0]["rowSet"]

        for i in range(len(results)):
            printData += str(teams[results[i][3][:3]]) + " "
            printData += str(teams[results[i][3][-3:]]) + " "
            printData += str(results[i][26]) + " "

            printData += " " + str(results[i][1])
            printData += "\n"

    with open('data.txt', 'w') as f:
        f.write(printData)


def getDataFromFile():
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

    with open('data.json') as f:
        data = json.load(f)

    results = data["resultSets"][0]["rowSet"]
    # print(len(results))php

    with open('dataFile.txt', 'w') as f:
        printData = ""
        for i in range(len(results)):
            printData += str(teams[results[i][3][:3]]) + " "
            printData += str(teams[results[i][3][-3:]]) + " "
            printData += str(results[i][26]) + " "
            if results[i][5] == "W":
                printData += str(results[i][26] - randint(0, 25))
            else:
                printData += str(results[i][26] + randint(0, 25))
            printData += "\n"
        f.write(printData)

def fixDuplicates():
    with open('data.txt', 'r') as f:
        array = [[int(x) for x in line.split()] for line in f]

    newArray = []
    for i in array:
        index = isInArray(i, newArray)
        if index > -1:
            newArray[index][4] = i[2]
        else:
            newArray.append([i[0], i[1], i[2], i[3], 0])

    # removing GameID
    # for i in newArray:
    #     i.pop(3)
    printData = ""
    for i in newArray:
        printData += str(i[0]) + " "
        printData += str(i[1]) + " "
        printData += str(i[2]) + " "
        printData += str(i[4]) + "\n"

    with open('allData.txt', 'w') as f:
        f.write(printData)


def isInArray(i, array):
    index = 0
    for j in array:
        if i[3] == j[3]:
            return index
        index = index + 1
    return -1

def reduceData(team1, team2):
    with open('allData.txt', 'r') as f:
        array = [[int(x) for x in line.split()] for line in f]

    print(team1)
    newArray = []
    for i in array:
        if i[0] == int(team1) or int(i[0]) == team2:
            newArray.append([i[0], i[1], i[2], i[3]])

    # removing GameID
    # for i in newArray:
    #     i.pop(3)
    printData = ""
    for i in newArray:
        printData += str(i[0]) + " "
        printData += str(i[1]) + " "
        printData += str(i[2]) + " "
        printData += str(i[3]) + "\n"

    with open('datat' + team1 + 't' + team2 + '.txt', 'w') as f:
        f.write(printData)