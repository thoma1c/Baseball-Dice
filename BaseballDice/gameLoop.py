# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 00:17:41 2022

@author: tyler
"""

#import csv

import random

inningsList = []
teamsList = []

home = "Tyler"

visitor = "Mel"

with open('innings.txt', 'r') as inningsFile:
    
    for item in inningsFile:
        inningsList = item.split(',')
        
with open('teams.txt', 'r') as teamsFile:
    for item in teamsFile:
        teamsList = item.split(',')
        

def gameDay(home, visitor, inningsList, teamsList):
    
    homeTeam = home + "'s" + random.choice(teamsList)
    visitingTeam = visitor + "'s" + random.choice(teamsList)
    
    playBall = True
    
    inning = 0
    
    def roll(teamsList): 
        return random.choice()

    while playBall == True:
        
        print("Let's play Ball!\n")
        
        print("Playing today are " + visitingTeam + " against " + homeTeam)
        
        print("It is the " + inningsList[inning] + '.' + visitingTeam + ' goes first.\n')       
        
        playBall = False
        
gameDay(home, visitor, inningsList, teamsList)
    
    







#print("Let's play Ball!\nIt is the " + str(inningsList[8]))
    
    
    
    # inningsList = list(inningsFile.split(','))
    
    # csvConvert = csv.writer(inningsFile)
    # inningsList = list(csvConvert)
    
    # csv_reader = csv.reader(inningsFile)
    # inningsList = list(csv_reader)
    
    
    
    # inningsList = list(csv.reader(inningsFile, delimeter","))
    #inningsList = list(inningsRaw, delimeter=",")
    
#inningsList[5]
    
    # for row in inningsRaw:
    #     inningsList = (','.join(row))
        


    

#innings = open("innings.txt", "r")

#print(innings.read())

#innings.close()

#while (inning < 18):
    
    