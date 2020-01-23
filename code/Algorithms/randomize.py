import random
import copy
from ..Objects import board, car, rushhour, route


def randomize_car(cars):
    """
    Randomly chooses the car out of the list of cars.  
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

    # Based on the direction of the car give random direction 1 of 2 lists
    if car.get_orientation():
        random_direction = random.choice(orientation_h)
        
    else:    
        random_direction = random.choice(orientation_v)

    return random_direction


def randomize_steps(board, car):
    """
    This method returns a random amount of steps a car can take.
    This is based on its length.
    """

    max_steps = board - car.length
    random_step = random.randrange(1, max_steps)

    return random_step
    
    
def run(game):
    """
    Algorithm that makes a random move based on the max steps of a random car.
    """

    # Create a copy of the game that will be returned later
    new_game = copy.deepcopy(game)

    while not new_game.check_win() and new_game.archive.moves < 100000:
        # Choose a random car
        random_car = randomize_car(new_game.cars)

        # Make move with that car
        new_game.move(random_car.name , randomize_direction(random_car), randomize_steps(game.game.size, random_car))
        
    new_game.print_game(new_game.game, new_game)
    return new_game