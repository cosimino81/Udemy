# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 09:51:24 2018

@author: Cosimo
"""

import numpy as np
# 1
# Creo un array 3x3
def create_board():
    br = np.zeros((3,3))
    return br
    
board = create_board()

print (board)

# 2
# Creo una funzione che inserisce il numero del player se la posizione é = 0 
def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board
    else:
        return "Place occupied"

board = create_board()       
pp = place(board, 1, (0,0))
print pp

# 3
# Trovo tutte le posizioni non occupate (cioè = 0)
def possibilities(board):
    return list(zip(*np.where(board == 0)))

pos = possibilities(board)
print pos

# 4
# posiziono in maniera random il numero del player dove cè una posizione libera
def random_place(board, player):
    selection = possibilities(board)
    if len(selection) > 0:
        position = [selection[i] for i in np.random.choice(len(selection), 1)]
        position = position[0]
    place(board, player, position)
    return board
   
random_place(board, 2)

# 5
# faccio marcare 3 posizioni per ogni player
for i in range(3):
    for p in [1,2]:
        random_place(board, p)
print board

# 6
# 
def row_win(board, player):
    for row in board:
        if np.all(row == player):
            return True
            break
        else:
            return False

row_win(board, 2)

# 7 
def col_win(board, player):
    if np.any(np.all(board == player, axis= 0)):
        return True
    else:
        return False
        
col_win(board, 1)

# 8
def diag_win(board, player):
    first_dig = np.diag(board)
    second_dig = np.diag(np.fliplr(board))
    if np.all(first_dig == player) or np.all(second_dig == player):
        return True
    else:
        return False

diag_win(board, 1)

# 9
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply. 
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            # If so, store `player` as `winner`.
            winner = player
        if np.all(board != 0) and winner == 0:
            winner = -1
        return winner


# 10
# In this exercise, we will use all the functions we have made to simulate an entire game.
def play_game():
    winner = 0
    board = create_board()
    while winner == 0:
        for player in [1,2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner
    
play_game()       

# 11
import time

winnerlist =[]

start_time = time.time()
for i in range(1000):
    winnerlist.append(play_game()) 
end_time = time.time()

print (end_time - start_time)


# 12
def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            # use `random_place` to play a game, and store as `board`.
            board = random_place(board, player)
            # use `evaluate(board)`, and store as `winner`.
            winner = evaluate(board)
            if winner != 0:
                break
        
    return winner

play_strategic_game()  

