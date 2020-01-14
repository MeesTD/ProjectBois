import csv 
import os
import hashlib
from code.Objects import board, car, rushhour, route

if __name__ == "__main__":
    in_file = 'code/Data/Rushhour6x6_2.csv'
    board = board.Board(in_file)
    game = rushhour.RushHour(in_file)
    while True:
        


