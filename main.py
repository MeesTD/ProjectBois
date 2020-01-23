import csv 
import os
import hashlib
import copy
from code.Objects import board, car, rushhour, route
from code.Algorithms import randomize, randomize_with_routes, breadthfirst, astar

if __name__ == "__main__":

    source_folder = "code/Data/"
    source_file = "Rushhour6x6_2.csv"
from code.Algorithms import breadthfirst, randomize, randomize_with_routes

def Average(lst):
    return sum(lst)/len(lst)

if __name__ == "__main__":

    # Initialize in_file
    source_folder = "code/Data/"
    source_file = "RushHour6x6_2.csv"
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
    # routerandom_game = rushhour.RushHour(in_file)
    # archive_route = route.Route()
    # while True:
    #     if randomize.run(routerandom_game, board) and archive_route.get_state(routerandom_game.cars) == False:
    #         archive_route.add_move()
    #     if random_game.check_win() == True:
    #         routerandom_game.print_game(board, routerandom_game)
    #         print(archive_route.moves, "Random with route")
    #         break     
    #     if archive_route.moves > 20000:
    #         routerandom_game.print_game(board, routerandom_game)
    #         print(archive_route.moves, "Random with route")
    #         break
    #     archive_route.save_state(routerandom_game.cars)

    astarr = astar.Astar(in_file)
    astarr.functionality()
    # while counter < max_count:
    #     game = rushhour.RushHour(in_file)
    #     result = randomize_with_routes.run(game)
    #     total.append(result.archive.moves)
    #     counter += 1
    #     result = None
    #     game = None
    #     print(counter)
    

    # # ------------------Breadthfirst algorithm with archive ------------
    # while counter < max_count:
    #     breadth = breadthfirst.Breadthfirst(in_file)
    #     breadth.run()
    #     total.append(len(breadth.states))

    # print(Average(total))
    # print(min(total))
    # print(max(total))
