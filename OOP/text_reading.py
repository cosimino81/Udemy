# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:21:35 2018

@author: Cosimo
"""
import nltk
from nltk import word_tokenize

class TextManipuation():
    
    def __init__(self, path):
        self.testo = open(path, 'r')
        
    def TextReader(self):
        for line in self.testo.readlines():
            for word in line.split(" "):
                print word
                   
    def Tokenization(self):
        testo = word_tokenize(self.testo.read())
        print nltk.pos_tag(testo)
        
        
ts = TextManipuation(r'C:\Users\Cosimo\Desktop\github\Udemy\OOP\testo.txt')

ts.TextReader()

ts.Tokenization()













