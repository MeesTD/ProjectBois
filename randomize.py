import random
from code.Objects import board, car, rushhour

def randomizer(cars, max_steps):
    """
    Randomly choses the car, the amount of steps and direction    
    """
    random_list = []
    
    # Randomily chooses car, steps and direction
    random_car = random.choice(cars)
    random_step = random.randrange(1, max_steps)
    random_direction = random.choice([H, V])
    
    random_list.extend((random_car, random_step, random_direction))
    
    return random_list
    
if __name__ == "__main__":  
    
    # Creates an instance of the board
    in_file = 'code/Data/Rushhour9x9_4.csv'
    board = board.Board(in_file)
    game = rushhour.RushHour(in_file)
    
    # Retreives the cars and the max steps
    all_cars = game.cars
    max_steps = board.size - random_car.length
    
    # Calls the randomize function 
    info_list = randomizer(game.cars, max_steps)
    
    game.move(info_list[0], random_step[1], random_direction[2])
    