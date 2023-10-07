# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 22:21:02 2022

@author: tyler
"""

import random

def roll(results): 
    return random.choice(list(results.values()))

#print(roll(results))

def playBall():
    
    innings = ['Top of the first', 'Bottom of the first','Top of the second','Bottom of the second',
               'Top of the third', 'bottom of the third','Top of the fourth','Bottom of the fourth',
               'Top of the fifth','Bottom of the fifth','Top of the sixth','bottom of the sixth',
               'Top of the seventh','Bottom of the seventh','Top of the eighth','bottom of the eitghth', 
               'Top of the ninth', 'Bottom of the ninth']
    
    currentInning = 0
    
    homeScore = 0
    
    visitorScore = 0
    
    results = {11:'home run', 12:'double', 13:'fly out', 14:'walk', 15:'pop out',
           16:'single', 22:'double play', 23:'ground out', 24:'strike out',
           25:'single', 26:'strike out', 33:'walk', 34:'triple', 35:'ground out',
           36:'ground out', 44:'walk', 45:'pop out', 46:'strike out', 55:'double',
           56:'scrifice fly', 66:'home run'        
        }

    teams = ['Blue Jays', 'Murderers', 'Nancies', 'Weirdos', 'Meowing Cats', 'Gun Wielders']
    
    def roll(results): 
        return random.choice(list(results.values()))
    
    print("LET'S PLAY BASEBALL!\n")
    
    visitor = input("Who's the visiting team? (Type the name and press Enter)\n>")
    
    visitor += "'s " + random.choice(teams)
    
    home = input("WGot it. Who's playing home? (Type the name and press Enter)\n>")
    
    home += "'s " + random.choice(teams)        
   

    print("\nAll Set!\nThe visiting team is " + visitor)
    print("\nThe home team is " + home)
    
    
    
    print("\nIt is the " + innings[currentInning])
    
    print("\nScore:\n" + visitor + ": " + str(homeScore) + '\n' + vis)
    
    print("\nVisiting team goes first.\n")
    
    input("Press Enter to roll...")
    
    
    
playBall()

