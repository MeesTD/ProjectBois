import csv 
import os
import copy
from code.Objects import board, car, rushhour, route
from code.Algorithms import randomize, smartcabby, breadthfirst, breadthfirst_prio, astarreverse

def Average(lst):
    return sum(lst)/len(lst)

if __name__ == "__main__":

    user_file = str(input("Which puzzle would you like to run? Just type the boardsize and puzzle number likeso:'6x6_1', if you type it in another way it won't work. (BE CAREFUL 12x12_7 MAY TAKE A LONG TIME TO RUN) \n> "))
    # Initialize in_file
    source_folder = "data/"
    source_file = "RushHour"
    in_file = f"{source_folder}{source_file}{user_file}.csv"

    # Initialize both the board and the game based on the infile.
    board = board.Board(in_file)
    game = rushhour.RushHour(in_file)

    print("Random (1) \nRandom with routes (2) \nBreadthfirst (3) \nBreadthfirst with priority queue (4) \nA* reverse (5) \n")

    user_algorithm = 6
    while user_algorithm > 5 or user_algorithm < 1:
        user_algorithm = int(input("Which algorithm would you like to run? Type the number besides the algorithm name. \n> "))

    user_amount = int(input("How often would you like to run the algorithm? \n> "))

    # Initialize counter, max & total to use when running algorithms:
    counter = 0
    max_count = user_amount
    total = []

    debug = input("Would you like to write the moves unto your HDD? Y/N \n> ")

    if debug == "Y":
        game.set_debug()
        game.set_output(str(input("What would you like the output file which shows the moves made to be called? \n> ")))
        total_name = str(input("What would you like the total moves outputfile to be called? \n> "))
        total_name += ".csv"

    #-----------------Regular random algorithm-----------------------------
    # This algorithm may or may not solve the puzzle
    if user_algorithm == 1:
        while counter < max_count:
            random_game = copy.deepcopy(game)
            result = randomize.run(random_game)
            totalrow = []
            totalrow.append(counter)
            totalrow.append(result.archive.move_amount)
            total.append(totalrow)
            counter += 1
            print(f"Won game {counter} with {result.archive.move_amount} moves")

    
    #-----------------Random with routes algorithm-----------------------------
    elif user_algorithm == 2:
        while counter < max_count:
            game_randomroutes = copy.deepcopy(game)
            result = smartcabby.run(game_randomroutes)
            total.append(result.archive.move_amount)
            counter += 1
            print(f"Won game {counter} with {result.archive.move_amount} moves")
    

    # ------------------Breadthfirst algorithm with archive ------------
     
    elif user_algorithm == 3:    
        while counter < max_count:
            result = copy.deepcopy(breadthfirst.Breadthfirst(in_file))
            result = result.run()
            totalrow = []
            totalrow.append(counter)
            totalrow.append(result.archive.move_amount)
            total.append(totalrow)
            counter += 1
            print(f"Won game {counter} with {result.archive.move_amount} moves")

    # ------------------Breadthfirst algorithm with priority queue ------------

    elif user_algorithm == 4:
        prio_game = breadthfirst_prio.Breadthfirst_prio(in_file)
        prio_game.lookahead_amount = int(input("How far would you like the algorithm to look ahead? \n> "))
        while counter < max_count:
            result = copy.deepcopy(prio_game)
            result = result.functionality()
            totalrow = []
            totalrow.append(counter)
            totalrow.append(result.archive.move_amount)
            total.append(totalrow)
            counter += 1
            result.print_game(result.game, result)
            print(f"Won game {counter} with {result.archive.move_amount} moves")
            

    # ------------------A* reverse ------------
    elif user_algorithm == 5:    
        while counter < max_count:
            astar = copy.deepcopy(astarreverse.Astar(in_file))
            result = astar.functionality()
            totalrow = []
            totalrow.append(counter)
            totalrow.append(result.archive.move_amount)
            total.append(totalrow)
            counter += 1
            result.print_game(result.game, result)
            print(f"Won game {counter} with {result.archive.move_amount} moves")

    if debug == "Y":
        # The writer used for the total moves of each iteration of an algorithm.
        with open("data/Output/" + total_name, 'w', newline = '') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Run number", "result"])
                for row in total:
                    writer.writerow([row[0], row[1]])