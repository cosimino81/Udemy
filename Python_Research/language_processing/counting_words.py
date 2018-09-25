# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 09:44:16 2018

@author: Cosimo

Questa esercitazione fa riferimanto al CASE STUDY 2: Natural Language Processing
L'esercitazione parte con la definizione di semplici funzioni per la conta delle
frequenze delle parole in un testo e della lunghezza del testo, si passa poi alla 
lettura di più file contemporanemaente fino al plotting della lunghezza del testo
e della frequenza parole per ogni testo.  



"""

text = "This is a sample text. I use, this text in 'order' to create a (function) that counts the words."


"""
# 1 
Counting words function.
Return a dictionary with the frequence of the words into a string.
"""

def count_word(text):
    """
    This function counts the frequency of the words into a text.
    """
    words_dict = {}
    text = text.lower()
    skip = [",",".","(",")", "'"]
    for ch in skip:
        if ch in text:
           text= text.replace(ch, "")
    for w in text.split(" "):
        if w in words_dict:
            words_dict[w] += 1
        else:
            words_dict[w] = 1
    return words_dict

count_word(text)



"""
# 2 
Counting words function with Counter module.
Return a dict with the frequence of the words into a string.
"""
from collections import Counter
def count_word2(text):
    """
    This function counts the frequency of the words into a text 
    by using the Counter method.
    """
    text = text.lower()
    skip = [",",".","(",")", "'"]
    for ch in skip:
        if ch in text:
           text= text.replace(ch, "")
    words_dict = Counter(text.split(" "))
    return words_dict

count_word2(text)


"""
# 3
Function that read a file in a specific directory. 
It returns plain text.
"""
def read_book(text_path):
    """
    This book read a book and return a string
    """
    with open(text_path, "r") as current_text:
        text = current_text.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

# Leggo il testo
testo = read_book(r"C:\Users\Cosimo\Desktop\Python_Research\language_processing\romeo_juliette.txt")

len(testo)

#Trovo l'indice di una specifica frase dentro il testo
ind = testo.find("Give me the letter")

# Trovo la parte del testo cha va dall'indice della frase fino a...
sample_text = testo[ind: 160000]

print sample_text


"""
# 4
Function i will use for statistic analysis.
It return the 1)Number of unique words, 2)Sum of all the words 
La funzione prende in input il dizionario creato dalla funzione count_word
"""
def word_stats(word_count):
    #numero di parole uniche
    numb_unique_words = len(word_count)
    #frequenza di tutte le parole
    counts = word_count.values()
    return (numb_unique_words, counts)

"""
# 5
Leggo il testo di romeo e julietta e conto il numero di parole uniche
e il numero di parole totali
"""

testo = read_book(r"C:\Users\Cosimo\Desktop\Python_Research\language_processing\romeo_juliette.txt")

# Passo il testo alla funzione word_count il quale restituisce un dizionario
word_count  = count_word(testo)

# Sul dizionario faccio le statistiche
(numbWords, countWords) = word_stats(word_count)

print (numbWords, sum(countWords))


"""
# 6
Questo è un esempio di come navigare in una directory e leggere più files contemporaneamente
"""

import os
# directory di partenza
book_dir = "C:\Users\Cosimo\Desktop\Python_Research\language_processing\Books"
os.listdir(book_dir)

# Ciclo sulla directory
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" +language):
        for title in os.listdir(book_dir + "/" +language+ "/"+author):
            inputfile = book_dir + "/" +language+ "/"+author+"/"+title
            print inputfile
            text = read_book(inputfile)
            (numb_unique, counts) = word_stats(count_word(text))

            print (numb_unique, sum(counts))


"""
# 6
Using of pandas in order to read multiple files and keep track of the words

"""
import os
import pandas as pd

table = pd.DataFrame(columns = ("language", "author", "title","unique", "lenght"))

# directory di partenza
books_dir = "C:\Users\Cosimo\Desktop\Python_Research\language_processing\Books"
os.listdir(books_dir)

# Ciclo sulla directory
row_numb = 1

for language in os.listdir(books_dir):
    for author in os.listdir(books_dir + "/" +language):
        for title in os.listdir(books_dir + "/" +language+ "/"+author):
            inputfile = books_dir + "/" +language+ "/"+author+"/"+title
            print inputfile
            text = read_book(inputfile)
            (numb_unique, counts) = word_stats(count_word(text))
            table.loc[row_numb] = language, author.capitalize(), title.replace(".txt", ""), numb_unique, sum(counts)
            
            row_numb +=1

print table

# Adding new column to the table




"""
# 7 
Plotting the table content
"""
import matplotlib.pyplot as plt

# statter plot
plt.plot(table.lenght,table.unique,  "bo")

#scatter log-log plot
plt.loglog(table.lenght, table.unique, "go")

"""
# 8
Scatter of all singular languages
"""
plt.figure(figsize=(6,5))
#Take a subset of the table
subset = table[table.language == "English"]
plt.loglog(subset.lenght, subset.unique, "o", label= "English", color="crimson")

subset = table[table.language == "French"]
plt.loglog(subset.lenght, subset.unique, "o", label= "French", color="blue")

subset = table[table.language == "Portuguese"]
plt.loglog(subset.lenght, subset.unique, "o", label= "Portuguese", color="green")

subset = table[table.language == "German"]
plt.loglog(subset.lenght, subset.unique, "o", label= "German", color="orange")

plt.legend()
plt.xlabel("Book Lenght")
plt.ylabel("Book Unique Words")

plt.savefig("books_stats.jpg")
plt.savefig("books_stats.pdf")


table[table.language == "English"]
















