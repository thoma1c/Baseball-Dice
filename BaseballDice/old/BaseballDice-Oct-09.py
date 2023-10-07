# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:00:43 2022

@author: tyler
"""

import random

#Read in the innings list - just names the frames
with open('innings.txt', 'r') as inningsFile:
    
    for item in inningsFile:
        inningsList = item.split(',')
        
#Read in the random teams list
with open('teams.txt', 'r') as teamsFile:
    for item in teamsFile:
        teamsList = item.split(',')
        
#Read in the roll results
        
with open('rollResults.txt', 'r') as resultsFile:
    for item in resultsFile:
        resultsList = item.split(',')       

class field:
    
    def __init__(self, players, inningsList, teamsList, resultsList):
        
        self.homePlayer, self.visitingPlayer = players
        
        self.homeTeam = self.homePlayer + "'s " + random.choice(teamsList)
        
        self.visitingTeam = self.visitingPlayer + "'s " + random.choice(teamsList)
        
        self.homeTeamScore = 0
        
        self.visitingTeamScore = 0
        
        self.frame = 0
        
        self.outs = 0
        
        self.bases = [0,0,0]
        
        #self.resultsList = resultsList
        
    def roll(self):
        return random.choice(resultsList)
    
    def currentFrame(self):
        return inningsList[self.frame]
    
players = ['Mel', 'Tyler']

myGame = field(players,inningsList,teamsList,resultsList)        














