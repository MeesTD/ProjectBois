import csv 
import os
import copy
from code.Objects import board, car, rushhour, route
from code.Algorithms import randomize, randomize_with_routes, breadthfirst, breadthfirst_prio, astarreverse

def Average(lst):
    return sum(lst)/len(lst)

if __name__ == "__main__":

    # Initialize in_file
    source_folder = "data/"
    source_file = "RushHour6x6_1.csv"
    in_file = f"{source_folder}{source_file}"

    # Initialize both the board and the game based on the infile.
    board = board.Board(in_file)
    game = rushhour.RushHour(in_file)

    # Initialize counter, max & total to use when running algorithms:
    counter = 0
    max_count = 1000
    total = []


    # #-----------------Regular random algorithm-----------------------------
    # # This algorithm may or may not solve the puzzle
    #while counter < max_count:
        #result = randomize.run(game)
        #totalrow = []
        #totalrow.append(counter)
        #totalrow.append(result)
        #total.append(totalrow)
        #counter += 1
        #print("Won game.")

    #astarr = astarreverse.Astar(in_file)
    #astarr.functionality()



    # while counter < max_count:
    #     game = rushhour.RushHour(in_file)
    #     result = randomize_with_routes.run(game)
    #     total.append(result.archive.moves)
    #     counter += 1
    #     result = None
    #     game = None
    #     print(counter)
    

    # ------------------Breadthfirst algorithm with archive ------------
     
    
    while counter < max_count:
        game_random = copy.deepcopy(game)
        result = randomize_with_routes.run(game_random)
        totalrow = []
        totalrow.append(counter)
        totalrow.append(result.archive.move_amount)
        total.append(totalrow)
        counter += 1
        print("Won game.")
    
    with open("Random_with_routes6x6_1.csv", 'w', newline = '') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Run number", "result"])
            for row in total:
                writer.writerow([row[0], row[1]])
