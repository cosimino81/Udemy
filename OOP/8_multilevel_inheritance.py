# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 17:51:48 2019

@author: Cosimo
"""

class MusicalInstrument:
    maxNumberOfKeys =12
    
class StringInstrument(MusicalInstrument):
    typeOfWood = "Cedro"
    
class Guitar(MusicalInstrument, StringInstrument):
    def __init__(self):
        self.numberOfString = 6
        print "The guitare has {} strings It's made of {} and it can play {} keys.".format(self.numberOfString,
                                self.typeOfWood, self.maxNumberOfKeys)
        
guitar = Guitar()

