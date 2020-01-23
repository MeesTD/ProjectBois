###################################################################################################
# randomize.py
#
# Zeno Degenkamp, Mats pijning, Mees drissen
#
# This file contains all the logic for random algorithm. It randomily chooses a car,
# orientation, and amount of steps. 
###################################################################################################
import random
import copy
from ..Objects import board, car, rushhour, route


def randomize_car(cars):
    """
    Randomly chooses a car out of the list with all the cars.  
    """
    
    random_car = cars[random.choice(list(cars))]

    return random_car


def randomize_direction(car):

    """
    This method returns a random direction for a move based on the direction
    of the car.
    """
    # Initaliaze variables
    orientation_h = ['L', 'R']
    orientation_v = ['U', 'D']

    # If the orientation of the car is horizontal gives directions left and right
    if car.get_orientation():
        random_direction = random.choice(orientation_h)
    
    # If the orientation of the car is vertical gives directions up and down  
    else:    
        random_direction = random.choice(orientation_v)

    return random_direction


def randomize_steps(board, car):
    """
    This method calculates amount of steps a car can take, and chooses a random amount.
    """
    
    # Calculates the maximal amount of steps via the board length and car length
    max_steps = board - car.length
    
    # Chooses a random step between 1 and maximal steps
    random_step = random.randrange(1, max_steps)

    return random_step
    
    
def run(game):
    """
    Method that contains all the functionality for the random algorithm.
    """

    # Create a copy of the game that will be returned later
    new_game = copy.deepcopy(game)

    # Checks if game is won or if game is passed 100000 moves
    while not new_game.check_win() and new_game.archive.moves < 100000:
        
        # Choose a random car
        random_car = randomize_car(new_game.cars)

        # Make move with that car
        new_game.move(random_car.name , randomize_direction(random_car), randomize_steps(game.game.size, random_car))
    
    # Prints the final board
    new_game.print_game(new_game.game, new_game)
    
    return new_game
    
