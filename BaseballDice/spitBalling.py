# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:50:14 2022

@author: tyler
"""

import random

roll = 0

class field:
    def __init__(self):
        
        self.bases = [0,0,0]

with open('rollResults.txt', 'r') as rollFile:
    for item in rollFile:
        rollList = item.split(',')
        
def parseRoll(roll, rollList, team):
    
    numberOfRunsToAdd = 0
    
    if roll == 'home run':
        print('Home run!')
        numberOfRunsToAdd = team.bases
        
        
        

    
    
    
    
    
parseRoll(rollList)

myBases = field()






#print(random.choice(rollList))

