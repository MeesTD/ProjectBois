###################################################################################################
# randomize_with_routes.py
#
# Zeno Degenkamp, Mats pijning, Mees drissen
#
# This file contains all the logic for random algorithm with routes. It randomily chooses a car,
# orientation, and amount of steps. And it tracks the past states and skips a move when 
# it recreates a past state.
###################################################################################################
import random
import copy
from . import randomize
from ..Objects import board, car, rushhour, route


def run(input_game):
    """
    This algorithm will make random moves with random cars while keeping
    previous game states in mind with the archive
    """

    # Initialize variables
    archive = route.Route()
    game = input_game

    # Checks if game is won or if game is passed 100000 moves
    while not game.check_win() and game.archive.move_amount < 100000:
        
        # Make a copy of the game to revert to if the move made already existed
        old_game = game

        # Randomize the car and make a random move with that car
        random_car = randomize.randomize_car(game.cars)

        # If the current state alreay exists in the archive, revert to the copy, else save it
        if game.move(random_car.name, randomize.randomize_direction(random_car), randomize.randomize_steps(game.game.size, random_car)):
            if archive.get_state(game):
                game = copy.deepcopy(old_game)
            else:
                archive.save_state(game)
    
    # Prints the amount of moves and the final board
    #print(game.archive.moves)
    game.print_game(game.game, game)
    
    return game
