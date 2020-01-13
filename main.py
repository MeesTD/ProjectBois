import csv 
import math
import os
from code.Objects import board, car, rushhour


if __name__ == "__main__":
    in_file = 'code/Data/Rushhour9x9_4.csv'
    board = board.Board(in_file)
    game = rushhour.RushHour(in_file)
    name = None
    for i in reversed(range(board.size + 2)):
        for j in range(board.size + 2):
            if i == 0 or i == board.size + 1:
                print("-", end="")
            elif j == board.size + 1 and i == math.ceil(board.size / 2):
                print(">", end="")
            elif j == 0 or j == board.size + 1:
                print("|", end="")
            elif j < board.size + 1 or j < board.size + 1:
                # for car in game.cars:
                #     if game.cars[car].x1 == j and game.cars[car].y1 == i:
                #         name = game.cars[car].name
                #     elif game.cars[car].x2 == j and game.cars[car].y2 == i:
                #         name = game.cars[car].name
                #     if game.cars[car].length == 3:    
                #         if game.cars[car].x3 == j and game.cars[car].y3 == i:
                #             name = game.cars[car].name
                # if name != None:
                #     print(name, end="")
                #     name = None
                # else:
                print(".",end="")         
        print("")