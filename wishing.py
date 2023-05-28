#!/usr/bin/env python3

import sys, random
from banners import *

"""
Basic Wishing Functions
"""

invalidInput: str = "Invalid Input"
def warpString(results, pity, tenCount, guarantee):
    output = []
    output.append("You got...\n")
    output.append(results)
    output.append("\nYour current pity is {}".format(pity))
    output.append("Your G-4 star counter is at: {}".format(tenCount))
    output.append("Your 5 star guarantee status: {}".format(guarantee))
    output.append("\nWould you like to go again?\nY/N")

    return "\n".join(output)

# def wishOnce

"""
End of wishing functions
"""
class Wishing(object):

    def __init__(self):
        self.pity = 0
        self.tenCount = 0
        self.guarantee = False
        self.upTo = 29
    
    def wish(self, name):
        number = random.randint(1, 500)
        if  self.pity == 89 or (number >= 27 and number <= self.upTo):
            fifty50 = random.randint(1, 2)
            self.pity = 0

            if self.guarantee == True or fifty50 == 1:
                self.guarantee = False
                return "***** " + name
            else:
                self.guarantee = True
                return "***** " + random.choice(standard5Star)
        
        elif self.tenCount == 9 or (number >= 1 and number <= 26):

            self.pity += 1
            self.tenCount = 0

            fifty50 = random.randint(1, 2)
            coneOrChar = random.randint(1, 2)

            if coneOrChar == 1:
                return "****  " + random.choice(standard4Cones)
            
            else:
                if fifty50 == 1:
                    return "****  " + random.choice(eventBanners[name])
                else:
                    return "****  " + random.choice(standard4Star)
            
        else:
            self.pity += 1
            self.tenCount += 1
            return "***   " + random.choice(standard3Cones)
        
