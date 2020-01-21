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

    # Start to play the game
    while not game.check_win() and game.archive.moves < 100000:
        # Make a copy of the game to revert to if the move made already existed
        old_game = game

        # Randomize the car and make a random move with that car
        random_car = randomize.randomize_car(game.cars)

        # If the current state alreay exists in the archive, revert to the copy. Else save it.
        if game.move(random_car.name, randomize.randomize_direction(random_car), randomize.randomize_steps(game.game.size, random_car)):
            if archive.get_state(game):
                game = copy.deepcopy(old_game)
            else:
                archive.save_state(game)
    print(game.archive.moves)
    game.print_game(game.game, game)
    return game
