# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 18:19:37 2018

@author: Cosimo
"""

# Create a class that contains a collection of animals.
# The collection can contains maximum four animals and the
# sum of the legs has to be 14

class AnimalStable:
    CountAnimal = 0
    LegNumber = 0
    StableCollection = []
    
    def __init__ (self, name, legs):
        self.name = name
        self.legs = legs
        
        # First check of the number of legs
        if sum([pair[1] for pair in AnimalStable.StableCollection]) <= 14:
            pass
        else:
            del AnimalStable.StableCollection[:]

        if len(AnimalStable.StableCollection) < 4:
            AnimalStable.StableCollection.append((self.name, self.legs))
        else:
            del AnimalStable.StableCollection[0]
            AnimalStable.StableCollection.append((self.name, self.legs))
            
        # First check of the number of legs
        if sum([pair[1] for pair in AnimalStable.StableCollection]) <= 14:
            pass
        else:
            del AnimalStable.StableCollection[:]
            
    @staticmethod
    def DisplayStable():
        for animal in AnimalStable.StableCollection:
            print animal[0], animal[1]
        print "Total legs: ", sum([pair[1] for pair in AnimalStable.StableCollection])


stable_obj = AnimalStable("orso", 4)
stable_obj = AnimalStable("gatto", 4)
stable_obj = AnimalStable("gallina", 2)
stable_obj = AnimalStable("cavallo", 4)

stable_obj.DisplayStable()

stable_obj = AnimalStable("cane", 4)
stable_obj = AnimalStable("zebra", 4)
stable_obj = AnimalStable("mucca", 4)
stable_obj = AnimalStable("elefante", 4)


stable_obj.DisplayStable()


