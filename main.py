import csv 
import os
import hashlib
import copy
from code.Objects import board, car, rushhour, route
from code.Algorithms import breadthfirst, randomize, randomize_with_routes

def Average(lst):
    return sum(lst)/len(lst)

if __name__ == "__main__":

    # Initialize in_file
    source_folder = "code/Data/"
    source_file = "Rushhour12x12_7.csv"
    in_file = f"{source_folder}{source_file}"

    # Initialize both the board and the game based on the infile.
    board = board.Board(in_file)
    game = rushhour.RushHour(in_file)

    # Initialize counter, max & total to use when running algorithms:
    counter = 0
    max_count = 25
    total = []


    # #-----------------Regular random algorithm-----------------------------
    # # This algorithm may or may not solve the puzzle
    # while counter < max_count:
    #     result = randomize.run(game)
    #     total.append(result.archive.moves)
    #     counter += 1
    #     print("Won game.")


    

    # # ----------------Random algorithm with routes---------------------
    while counter < max_count:
        game = rushhour.RushHour(in_file)
        result = randomize_with_routes.run(game)
        total.append(result.archive.moves)
        counter += 1
        result = None
        game = None
        print(counter)
    

    # # ------------------Breadthfirst algorithm with archive ------------
    # while counter < max_count:
    #     breadth = breadthfirst.Breadthfirst(in_file)
    #     breadth.run()
    #     total.append(len(breadth.states))

    print(Average(total))
    print(min(total))
    print(max(total))
