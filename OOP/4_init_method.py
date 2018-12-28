# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:21:35 2018

@author: Cosimo
"""

#Write an object oriented program to create a collection of precious stones.
#Not more than 5 precious stones can be held in possession at a
#given point of time. If there are more than 5 precious stones,
#delete the first stone and store the new one.


class PreciousStone:
    StoneNumber = 0
    StoneCollection = []
    def __init__(self, name):
        self.name = name
        PreciousStone.StoneNumber += 1
        if PreciousStone.StoneNumber <= 5:
            PreciousStone.StoneCollection.append(self)
        else:
            del PreciousStone.StoneCollection[0]
            PreciousStone.StoneCollection.append(self)
        
    @staticmethod
    def displayPreciousStones():
        for stone in PreciousStone.StoneCollection:
            print stone.name, end = ' '
        print " "
            
            
            
preciouseStoneOne = PreciousStone('Rubino')
preciouseStoneTwo = PreciousStone('Topazio')
preciouseStoneThree = PreciousStone('Diamante')
preciouseStoneFour = PreciousStone('Ambra')
preciouseStoneFive = PreciousStone('Smeraldo')

preciouseStoneFive.displayPreciousStones()

preciouseStoneSix = PreciousStone('Quarzo')

preciouseStoneOne.displayPreciousStones()


