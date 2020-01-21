import csv 
import os
import hashlib
from code.Objects import board, car, rushhour, route
from code.Algorithms import randomize, randomize_with_routes, breadthfirst_2, astar

if __name__ == "__main__":

    source_folder = "code/Data/"
    source_file = "Rushhour6x6_2.csv"
    # Initialize in_file
    in_file = f"{source_folder}{source_file}"
    # Initialize both the board and the game based on the infile.
    board = board.Board(in_file)


    # #-----------------Regular random algorithm-----------------------------
    # # This algorithm may or may not solve the puzzle
    # random_game = rushhour.RushHour(in_file)
    # archive = route.Route()
    # while True:
    #     random_game = randomize.run(random_game, board)
    #     archive.add_move()
    #     if random_game.check_win() == True:
    #         random_game.print_game(board, random_game)
    #         print(archive.moves, "Random")
    #         break     
    #     if archive.moves > 20000:
    #         random_game.print_game(board, random_game)
    #         print(archive.moves, "Random")
    #         break
    
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