# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 12:03:27 2018

@author: Cosimo
"""
# Questo è un esempio di come navigare in una directory e leggere più files contemporaneamente
import os

# directory di partenza
book_dir = r"C:\Users\Cosimo\Desktop\Python_Research\language_processing\language"

os.listdir(book_dir)

# Ciclo sulla directory
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" +language):
        for title in os.listdir(book_dir + "/" +language+ "/"+author):
            inputfile = os.listdir(book_dir + "/" +language+ "/"+author+"/"+title)
            print (inputfile)



