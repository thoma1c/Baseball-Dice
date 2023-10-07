# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 16:45:36 2023

@author: tyler
"""

class Cake:
    
    def __init__(self, kind, price,slices):
        self.kind = kind
        self.price = price
        self.slices = slices
        
    def describe(self):
        
        print("The " + self.kind + " cake costs $" + str(self.price) + " and is divided into " + str(self.slices) + " slices.")
        
cake1 = Cake("lemon", 24, 6)
cake1.describe()