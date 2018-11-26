# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:21:35 2018

@author: Cosimo
"""

class TextManipuation:
    
    def __int__(self, path, extension):
        self.path = path
        self.extension = extension
    
    def TextReader(self):
        with open(self.path, 'r') as f:
            text = f.read()
        print(text)
        