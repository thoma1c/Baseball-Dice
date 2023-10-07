# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:00:43 2022

@author: tyler
"""

#Clear the fucking screen
print(chr(27) + "[2J")

import random
from collections import deque
from itertools import cycle

"""

///////////////////////////////////////////

Read in the files. 

TODO: these should be functions, to make it cleaner and clean up 'items'


"""

#Read in the innings list - just names the frames

def getInningsFile():
    with open('innings.txt', 'r') as inningsFile:        
        for item in inningsFile:
            inningsList = item.split(',')            
    return inningsList

inningsList = getInningsFile()
        
#Read in the random teams list

def getTeamsFile():
    with open('teams.txt', 'r') as teamsFile:
        for item in teamsFile:
            teamsList = item.split(',')
    return teamsList

teamsList = getTeamsFile()
        
#Read in the roll results

def getRollResults():
    with open('rollResults.txt', 'r') as resultsFile:
        for item in resultsFile:
            resultsList = item.split(',')     
    return resultsList

resultsList = getRollResults()
        
        
"""
///////////////////////////////////////////

Function to handle the hits. Its first three arguments come from a field object,
the currentAtBatScore comes from a team objet

"""
        
def hitsHandler(roll, currentOuts, bases, currentAtBatScore):    
    
    bases = deque(bases) #Make the bases easier to handle in terms of pops and pushes
    
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

"""
///////////////////////////////////////////

handle the prining of the bases, 

TODO: this could be done easily in one of those new -> type functions. 

"""

def baseHandler(bases):
    firstBase, secondBase, thirdBase = ['□','■'], ['□','■'], ['□','■']
       
    manOnFirst = firstBase[bases[0]]
    
    manOnSecond = secondBase[bases[1]]
    
    manOnThird = thirdBase[bases[2]]     
  
    baseLayout = ('    ' + manOnSecond + " \n /     \ \n" + manOnThird + "       " 
            + manOnFirst + "\n \\     /" + "\n    ⯐")
    
    return baseLayout


"""
///////////////////////////////////////////

Set up the field.

"""

class field:
    
    def __init__(self, inningsList, resultsList):
        
        #////////////////////// This is now in the team class
        
        #self.homePlayer, self.visitingPlayer = players
        
        #self.homeTeam = self.homePlayer + "'s " + random.choice(teamsList)  #Here's where to add to a team class.
        
        #self.visitingTeam = self.visitingPlayer + "'s " + random.choice(teamsList)
        
        #self.homeTeamScore = 0
        
        #self.visitingTeamScore = 0
        
        #self.teams = (self.visitingTeam, self.homeTeam)
        
        self.frame = 0
        
        self.currentTeamAtBat = 0
        
        self.outs = 0
        
        self.bases = [0,0,0]
        
       
    #Pick a random 'roll' from the results.txt   
        
    def roll(self):
        return random.choice(resultsList)
    
    #gets a 'top of the first' type string of the frame called
    
    def currentFrame(self):
        return inningsList[self.frame]
    
#Initialize the field.
    
myField = field(inningsList,resultsList)    



"""
///////////////////////////////////////////

Set up the teams.

"""    

#Just for now, use these, but 
#TODO: add player name input

players = ['Mel', 'Tyler']

#Team class to handle the score a little easier

class Team:
    
    def __init__(self,teamName):
        
        #TODO: make a __string__ for the team name
        
        self.teamName = teamName
        
        self.score = 0
        
#Assign the team names
        
def assignTeams(players, teamsList):
    
    visitingPlayer, homePlayer = players
    
    visitingTeamName = visitingPlayer + "'s " + random.choice(teamsList)
    
    homeTeamName = homePlayer + "'s " + random.choice(teamsList)
    
    visitingTeam = Team(visitingTeamName)
    
    homeTeam = Team(homeTeamName)
    
    return visitingTeam, homeTeam
    
teams = assignTeams(players,teamsList)   



"""
///////////////////////////////////////////

Start a game with a preamble, of course. 

"""


def game(myField):
    
    '''
    # Initial crap
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
  
    def playBall(myField):     
        
        #Make a cycle to toggle between visting team (0) and home team (1)
        currentBattingTeamCycle = cycle(range(2))
        currentBattingTeam = next(currentBattingTeamCycle)
        
        #currentRoll = ''
        
        while (myField.frame) < 2:
            
            print("\nIt is the " + myField.currentFrame())
    
            while myField.outs != 3:
                
                
                
                '''
                Testing the hits handler in certain conditions.
                TODO: unit testing?
                '''
                #currentAtBat = 0
                #myField.bases = [1,0,0]
                #myField.outs = 2
    
                
                print(baseHandler(myField.bases))            
            
                print("\nRolling...")
                
                currentRoll = myField.roll()            
                #currentRoll = 'triple'
                
                print("\n" + teams[currentBattingTeam].teamName + ", you rolled a " + currentRoll +".\n")
                
                myField.bases, myField.outs, teams[currentBattingTeam].score = hitsHandler(currentRoll, myField.outs, myField.bases, teams[currentBattingTeam].score)
                
                print("New bases list: "+ str(myField.bases))
                print("Current outs: " + str(myField.outs))
                print("Batting team's score: " + str(teams[currentBattingTeam].score)) # TODO need to fix this so it's whoever is batting
                
                
            #Update the user   
            print("\nThat's all she wrote! Next frame up.")        
            print("\nScore: ")
            print(str(teams[0].teamName) + ": " + str(teams[0].score))
            print(str(teams[1].teamName) + ": " + str(teams[1].score))
            
            #get ready for the next frame
            myField.bases = (0,0,0)
            myField.outs = 0
            myField.frame += 1
            currentBattingTeam = next(currentBattingTeamCycle)
            
            
            
    playBall(myField)
    
    
    
#Just run the game function and send a field class as an argument
game(myField)













