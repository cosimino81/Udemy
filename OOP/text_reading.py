# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:21:35 2018

@author: Cosimo
"""

class TextManipuation:
    
    def __int__(self, path):
        self.testo = open(path, 'r')
        #self.extension = self.path[-3:]
        print (self.testo)
    def TextManipulation(self):
        #if self.extension == 'txt':
        with (open(self, 'r')) as f:
            text = f.read()
        print(text)
        
        
        
ts = TextManipuation('C:\\Users\\Cosimo\\Desktop\\github\\Udemy\\OOP\\testo.txt')

ts.TextReader('C:\\Users\\Cosimo\\Desktop\\github\\Udemy\\OOP\\testo.txt')





v = "Users-Cosimo-Desktop-github-Udemy-OOP"
print (v[-3:])












