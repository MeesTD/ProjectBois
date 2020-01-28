import csv 
import os
import copy
from code.Objects import board, car, rushhour, route
from code.Algorithms import randomize, smartcabby, breadthfirst, breadthfirst_prio, astarreverse

def Average(lst):
    return sum(lst)/len(lst)

if __name__ == "__main__":

    user_file = str(input("Which puzzle would you like to run? Just type the boardsize and puzzle number IE: '6x6_1' \n"))
    # Initialize in_file
    source_folder = "data/"
    source_file = "RushHour"
    in_file = f"{source_folder}{source_file}{user_file}.csv"

    # Initialize both the board and the game based on the infile.
    board = board.Board(in_file)
    game = rushhour.RushHour(in_file)

    print("Random \nRandom with routes \nBreadthfirst \nBreadthfirst with priority queue \nA* reverse \n")

    user_algorithm = str(input("Which algorithm would you like to run? Type it as it's given in the line above. \n"))

    user_amount = int(input("How often would you like to run the algorithm?\n"))

    # Initialize counter, max & total to use when running algorithms:
    counter = 0
    max_count = user_amount
    total = []

    debug = input("Would you like to write the moves unto your HDD? Y/N")

    if debug == "Y":
        game.set_debug()
        game.set_output(str(input("What would you like the for the moves made output file  to be called?")))
        total_name = str(input("What would you like the total moves outputfile to be called?"))
        total_name += ".csv"

    #-----------------Regular random algorithm-----------------------------
    # This algorithm may or may not solve the puzzle
    if user_algorithm == "Random":
        while counter < max_count:
            random_game = copy.deepcopy(game)
            result = randomize.run(random_game)
            totalrow = []
            totalrow.append(counter)
            totalrow.append(result)
            total.append(totalrow)
            counter += 1
            print(f"Won game {counter}.")

    
    #-----------------Random with routes algorithm-----------------------------
    if user_algorithm == "Random with routes":
        while counter < max_count:
            game_randomroutes = copy.deepcopy(game)
            result = smartcabby.run(game_randomroutes)
            total.append(result.archive.moves)
            counter += 1
            print(f"Won game {counter}")
    

    # ------------------Breadthfirst algorithm with archive ------------
     
    if user_algorithm == "Breadthfirst":    
        while counter < max_count:
            result = copy.deepcopy(breadthfirst.Breadthfirst(in_file))
            result = result.run()
            totalrow = []
            totalrow.append(counter)
            totalrow.append(result.archive.move_amount)
            total.append(totalrow)
            counter += 1
            print(f"Won game {counter}.")

    # ------------------Breadthfirst algorithm with priority queue ------------

    if user_algorithm == "Breadthfirst with priority queue":
        while counter < max_count:
            result = copy.deepcopy(breadthfirst_prio.Breadthfirst_prio(in_file))
            result = result.functionality()
            totalrow = []
            totalrow.append(counter)
            totalrow.append(result.archive.move_amount)
            total.append(totalrow)
            counter += 1
            print(f"Won game {counter}.")
            

    # ------------------A* reverse ------------
    if user_algorithm == "A* reverse":    
        while counter < max_count:
            astar = copy.deepcopy(astarreverse.Astar(in_file))
            result = astar.functionality()

    if debug == "Y":
        # The writer used for the total moves of each iteration of an algorithm.
        with open(total_name, 'w', newline = '') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Run number", "result"])
                for row in total:
                    writer.writerow([row[0], row[1]])