# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 23:10:25 2018

@author: Cosimo
"""
# Class => Library
# Layer of abstarction => display available book, lend a book, add a book

# Class => Customer
# Layer of abstraction => request for a book, return a book 

class Library:
    
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    
    def displayAvailableBook(self):
        print()
        print("Available books: ")
        for book in self.availableBooks:
            print (book)
        print()
         
    def lendBook(self, requestBook):
        if requestBook in self.availableBooks:
            print ("You have borrowed the book")
            self.availableBooks.remove(requestBook)
        else:
            print ("Sorry the book is not available")
    
    def addBook(self, returnBook):
        if returnBook not in self.availableBooks:
            self.availableBooks.append(returnBook)
            print ("You have returned the book, thanks!")
        else:
            print ("Book already exist")
        


class Customer:
    
    def requestBook(self):
        print("Type the name of the book you want to rent: ")
        self.book = input()
        return self.book
        
    def returnBook(self):
        print("Type the name of the book you want to return:")
        self.book = input()

library = Library(['Book One','Book Two','Book Three', 'Book Four'])
customer = Customer()

while True:
    print ("Press 1 to display available books")
    print ("Press 2 to borrow a book")
    print ("Press 3 to return a book")
    print ("Press 4 to exit")
    
    userChoice = int(input())
    if userChoice is 1:
        library.displayAvailableBook()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnBook = customer.returnBook()
        library.addBook(returnBook)
    elif userChoice is 4:
        quit()




    
