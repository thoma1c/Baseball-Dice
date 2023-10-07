# -*- coding: utf-8 -*-
"""
Cturnated on Fri Oct  7 13:48:40 2022

@author: tyler
"""

from collections import deque

class batter:
    
    def __init__(self):
        
        self.score = 0

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
        
    print(baseLayout)
    
def hitsHandler(roll, bases):
    
    bases = deque(bases)
    
    scoreToAdd = 0
    
    outsToAdd = 0
    
    if roll == 'single':
        
        bases.appendleft(1)
        
        print(bases)
        
        if len(bases) == 4:
            if bases[3] == 1:
                scoreToAdd +=1
                bases.pop()   
                
            else:
                bases.pop()
        
        #bases.pop()
        
        print(bases)
                
    elif roll == 'home run':
        
        scoreToAdd += sum(bases) +1
        
        bases = [0,0,0]
        
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
        
        #
            
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
        
        
        
            
        #print(bases)    
    
    bases = list(bases)
            
    print("Bases : " , bases)
    
    print("Score to add :  " + str(scoreToAdd))  
    
    print("Outs to add : " , outsToAdd)
    
    return bases
    
#Bases as they are
bases = [0,1,0]

#the current roll
roll = 'walk'

#This figures out who's on first, so to speak
currentBases = hitsHandler(roll, bases)

#This prints is out
baseHandler(currentBases)
    
    