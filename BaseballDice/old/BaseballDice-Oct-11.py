# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:00:43 2022

@author: tyler
"""

import random
from collections import deque
from itertools import cycle

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
        
def hitsHandler(roll, currentOuts, bases, currentAtBatScore):    
    
    bases = deque(bases)
    
    scoreToAdd = currentAtBatScore #TODO this should be score to append
    
    outsToAdd = currentOuts #This should be outs to append
    
    if roll == 'single':
        
        bases.appendleft(1)
        
        #print(bases)
        
        if len(bases) == 4:
            if bases[3] == 1:
                scoreToAdd +=1
                bases.pop()   
                
            else:
                bases.pop()
        
        #bases.pop()
        
        #print(bases)
                
    elif roll == 'home run':
        
        scoreToAdd += sum(bases) + 1
        
        bases = [0,0,0]
        
        #TODO add grand slam!
        
    elif roll == 'double':
                
        #Advance the first base, if any
    
        bases.appendleft(0)
        
        #print(bases)
        
        if len(bases) == 4:
            if bases[3] == 1:
                scoreToAdd +=1
                bases.pop()
            else:
                bases.pop()                
                
        #Advance the second base, if any
                
        bases.appendleft(0)
        
       #print(bases)
        
        if len(bases) == 4:
            if bases[3] == 1:
                scoreToAdd +=1
                bases.pop()
            else:
                bases.pop()
                
        #Put the hitter on second
                
        bases[1] = 1
    
    elif roll == 'fly out' or roll == 'pop out' or roll == 'ground out' or roll =='strike out' : 
        
        #print(roll == 'strike out')
    
        outsToAdd += 1
        
    elif roll == 'walk':
        
        bases.appendleft(1)
        
        if len(bases) == 4 and bases[3] == 1:
            
            scoreToAdd +=1
            bases.pop()
            
        else:
            bases.pop()    
            
    elif roll == 'triple':
        
        #print(outsToAdd)
        
        #Need to do this three times and YES, this should be a function. I'm on it. 
        
        bases.appendleft(0)
        
        #Advance first, tally score
        
        #print(bases)
        
        if len(bases) == 4 and bases[3] == 1:
            
            scoreToAdd +=1
            bases.pop()
            bases.appendleft(0)
            
        else:
            bases.pop() 
            bases.appendleft(0)
            
        #Advance second, tally score
            
        #print(bases)   
                    
        if len(bases) == 4 and bases[3] == 1:
            
            scoreToAdd +=1
            bases.pop()
            bases.appendleft(0)
            
        else:
            bases.appendleft(0)
            bases.pop() 
            
        #bases.appendleft(0)
            
        #print(bases)
            
        #Advance third, tally score
            
        if len(bases) == 4 and bases[3] == 1:
            
            scoreToAdd +=1
            bases.pop()   
            #bases.appendleft(0)
              
        else:
            bases.pop()
            
        #print(bases)
            
        # Add the person to third
            
        bases[2] = 1
        
    elif roll == 'sacrifice fly':
        
        #Advence the runners, with an out
        bases.appendleft(0)
        outsToAdd += 1
        
        #If there's a runner home, score +=1, take him off the board
        
        if len(bases) == 4 and bases[3] == 1:
            
            scoreToAdd +=1
            bases.pop()
            
        else:
            bases.pop()
            
    elif roll == 'double play':
        
        #No one on base, batter is out
        outsToAdd += 1
        
        if outsToAdd == 3:
            return list(bases), outsToAdd, scoreToAdd
        
        extraOutsToAdd = 1
        
        base = 0
        
        #If there's someone on base, first in the list of bases is out       
        #print("Bases: " + str(bases))
        
        if sum(bases) > 0:  
                        
            for runner in bases:
                #print("Bases: " + str(bases))
                
                if (runner == 1) and (extraOutsToAdd == 1):
                    extraOutsToAdd = 0
                    outsToAdd += 1
                    bases[base] = 0
                    base += 1
                else:
                    base += 1
                    
                if extraOutsToAdd == 0:
                    break
                    
                        
        elif sum(bases) == 0:
            print("No batters on base, batter is out.")
            
        elif outsToAdd == 3:
            return list(bases), outsToAdd, scoreToAdd
                        
    return list(bases), outsToAdd, scoreToAdd

def baseHandler(bases):
    firstBase = ['□','■']
    
    secondBase = ['□','■']
    
    thirdBase = ['□','■']    
    
    manOnFirst = firstBase[bases[0]]
    
    manOnSecond = secondBase[bases[1]]
    
    manOnThird = thirdBase[bases[2]]     
    
    #scoringRun = bases[3]
    
    """
    --------------------
    
    """
    
    
    baseLayout = ('    ' + manOnSecond + " \n /     \ \n" + manOnThird + "       " 
            + manOnFirst + "\n \\     /" + "\n    ⯐")
    
    return baseLayout

class field:
    
    def __init__(self, players, inningsList, teamsList, resultsList):
        
        self.homePlayer, self.visitingPlayer = players
        
        self.homeTeam = self.homePlayer + "'s " + random.choice(teamsList)  #Here's what to add to a team class.
        
        self.visitingTeam = self.visitingPlayer + "'s " + random.choice(teamsList)
        
        self.homeTeamScore = 0
        
        self.visitingTeamScore = 0
        
        self.frame = 0
        
        self.currentTeamAtBat = 0
        
        self.outs = 0
        
        self.bases = [0,0,0]
        
        self.teams = (self.visitingTeam, self.homeTeam)
        
    def roll(self):
        return random.choice(resultsList)
    
    def currentFrame(self):
        return inningsList[self.frame]
    
players = ['Mel', 'Tyler']

myField = field(players,inningsList,teamsList,resultsList)        


def game(myField):
    
    '''
    # Initial setup
    # '''    
    # print("\nWelcome to Baseball Dice, the random baseball game!.")  
    
    # print("\nThe visiting team is " + myField.visitingTeam)
    # print("The home team is " + myField.homeTeam)
    
    # print("\nIt is the "+ myField.currentFrame() + ", score is nill nill.")
    
    # print("\nLet's play ball!\n")
    
    # print(baseHandler(myField.bases) + '\n')
    
    # print(myField.visitingTeam + ", you go first.")   
    
    '''   
    Now lets play a frame
    
    '''
    
    #Make a cycle to toggle between visting team (0) and home team (1)
    currentBattingTeamCycle = clycle(range(2))
    currentBattingTeam = next(currentBattingTeamCycle)
    
    
    def playFrame(myField):       
        
        currentRoll = ''
    
        while myField.outs != 3:
            
            #currentAtBat = 0
            #myField.bases = [1,0,0]
            #myField.outs = 2
            
            #TODO add score
            
            print(baseHandler(myField.bases))            
        
            print("\nRolling...")
            
            currentRoll = myField.roll()            
            #currentRoll = 'triple'
            
            print("\n" + myField.visitingTeam + ", you rolled a " + currentRoll +".\n")
            
            myField.bases, myField.outs, myField.visitingTeamScore = hitsHandler(currentRoll, myField.outs, myField.bases, myField.visitingTeamScore)
            
            print("New bases list: "+ str(myField.bases))
            print("Current outs: " + str(myField.outs))
            print("Batting team's score: " + str(myField.visitingTeamScore)) # TODO need to fix this so it's whoever is batting
            #print(baseHandler(myField.bases))
            
            #myField.outs += 1 #TODO I don't think this is the way to do it
            
            #myField.outs = 3
            
            
        print("\nThat's all she wrote! Next frame up.")
        
        print("Batting team's score: " + str(myField.visitingTeamScore))
            
    playFrame(myField)
    
    
    

game(myField)











