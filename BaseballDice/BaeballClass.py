# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:00:43 2022

@author: tyler
"""

#Read in the innings list - just names the frames
with open('innings.txt', 'r') as inningsFile:
    
    for item in inningsFile:
        inningsList = item.split(',')
        
#Read in the random teams list
with open('teams.txt', 'r') as teamsFile:
    for item in teamsFile:
        teamsList = item.split(',')

class game:
    
    def __init__(self, players, inningsList, teamsList):
        self.homeTeam, self.visitingTeam = players
        
        self.homeTeamScore = 0
        
        self.visitingTeamScore = 0
        
        self.frame = 0
        
        self.outs = 0
        
        self.bases = [0,0,0]
        
        


players = ['Mel', 'Tyler']



myGame = game(players,inningsList,teamsList)        