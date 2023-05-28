#!/usr/bin/env python3

""" Wishing Simulator """

"""
    Written by Smoodeazy, started May 28th 2023
    Feel free to edit this code
"""

import sys, random
from banners import *
from wishing import *

while True:
    results = Wishing()

    print("Would you like to roll on the event banner, weapon banner or the standard banner?")
    print("Options are E/L/S, not cap sensitive, respectively")
    choose = input("> ").lower()

    if choose != "e" and choose != "l" and choose != "s":
        print(invalidInput)
        print("Please try again")
    
    elif choose == "e":
        option = random.choice(fiveStars)

        while True:
            print("\nYou got {}'s banner!\nThe rate up characters are {}\n\nWould you like to roll for this banner or a different banner?\nY/diff\n\nPlease use the options given to you".format(option, ", ".join(eventBanners[option])))
            repeat = input("> ")

            if repeat.lower() == "diff":

                while True:
                    newOption = random.choice(fiveStars)

                    if newOption != option:
                        option = newOption
                        break
                    else:
                        pass

            elif repeat.lower() == "y":
                break
        
        while repeat.lower() == "y":
            print("\nWish once or 10 times?\nOnce/Ten\nPlease use the options provided\n")
            choosing = input("> ")

            if choosing.lower() == "once":
                
                while True:

                    print(warpString(results.wish(option), results.pity, results.tenCount, results.guarantee))

                    goAgain = input("> ")

                    if goAgain.lower() == "y":
                        pass
                    elif goAgain.lower() == "n":
                        break
                    else:
                        print(invalidInput)
                
            elif choosing.lower() == "ten":

                while True:
                    rolls = []

                    for i in range(10):
                        rolls.append(results.wish(option))

                    print(warpString("\n".join(rolls), results.pity, results.tenCount, results.guarantee))

                    goAgain = input("> ")

                    if goAgain.lower() == "y":
                        pass
                    elif goAgain.lower() == "n":
                        break
                    else:
                        print(invalidInput)         
            
            print("Would you like to wish again?\n Y/N")
            repeat = input("> ")

            while repeat.lower() != "y" and repeat.lower() != "n":
                repeat = input("> ")

    break
print("Thank you for using the Honkai Star Rail Warping Simulator")