# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 16:48:45 2019

@author: Cosimo
"""

class Apple:
    manifactured = "Apple Inc."
    contactWebSite = "www.apple.com/contacts"
    
    def contactDetails(self):
        print "To contact us log on {}".format(self.contactWebSite)

class MacBook(Apple):
    
    def __init__(self):
        self.yearOfManifacture = 2017
        
    def manifactureDetails(self):
        print "This MacBook was manifactured by {} in the year {}.".format(self.manifactured, self.yearOfManifacture)
        

company = MacBook()

company.contactDetails()
company.manifactureDetails()
    