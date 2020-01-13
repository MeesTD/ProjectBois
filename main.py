import csv 
import os
from code.Objects import board, car, rushhour

if __name__ == "__main__":
    in_file = 'code/Data/Rushhour9x9_4.csv'
    board = board.Board(in_file)
    game = rushhour.RushHour(in_file)
    while True:
        game.print_game(board, game)
        game.move("G", "L", 1)
