###################################################################################################
# smartcabby.py
#
# Zeno Degenkamp, Mats pijning, Mees drissen
#
# This file contains all the logic for the smart cabby algorithm. The smart cabby algorithm
# is an alternative of the randomize algorithm. The smart cabby algorithm uses the same 
# logic as the randomize, but the main difference is that the smart cabby uses an archive with 
# all the past states it has been to. Smart caby is able to skip states it has already been to 
# and therefore skip unnecessary moves. 
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
    game.print_game(game.game, game)
    print(game.archive.move_amount)
    
    return game
