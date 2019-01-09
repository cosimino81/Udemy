# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 17:11:56 2019

@author: Cosimo
"""

class OperativeSystem:
    multitasking = True
    name = "Mac OS"
    
    
class Apple:
    webSite = "www.apple.com"
    name = "Apple"

class MacBook(OperativeSystem, Apple):
    
    def __init__(self):
        if self.multitasking is True:
            print "This MacBokk is a multitasking pc. Visit our site {}".format(self.webSite)
            print "The operative system name is {}".format(self.name)
        else:
            print "This MacBook is not a multitasking pc."
            

macbook = MacBook()
