import csv 
import math
import os
from code.Objects import board, car, rushhour


if __name__ == "__main__":
    in_file = 'code/Data/Rushhour9x9_4.csv'
    board = board.Board(in_file)
    game = rushhour.RushHour(in_file)
    name = None
    print(game.red_car)
    for k in range (2):
        for i in reversed(range(board.size + 2)):
            for j in range(board.size + 2):
                if i == 0 or i == board.size + 1:
                    print("-", end="")
                elif j == board.size + 1 and i == math.ceil(board.size / 2):
                    print(">", end="")
                elif j == 0 or j == board.size + 1:
                    print("|", end="")
                elif j < board.size + 1 or j < board.size + 1:
                    for car in game.cars.values():
                        for l in range(len(car.xy)):
                            if car.xy[l][0] == j and car.xy[l][1] == i:
                                name = car.name
                    if name != None:
                        print(name, end="")
                        name = None
                    else:
                        print(".",end="")         
            print("")
        game.move("X", "R", 4)