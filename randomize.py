import random
from code.Objects import board, car, rushhour

def randomizer(board, cars):
    """
    Randomly choses the car, the amount of steps and direction    
    """
    
    # Initializes the variables
    random_list = []
    orientation_h = ['L', 'R']
    orientation_v = ['U', 'D']
    
    # Randomily chooses car, steps and direction
    random_car = cars[random.choice(list(cars))]
    
    
    max_steps = board.size - random_car.length
    random_step = random.randrange(1, max_steps)
    
    # Checks if the car is H or V
    if random_car.get_orientation():
        random_direction = random.choice(orientation_h)
        
    else:    
        random_direction = random.choice(orientation_v)
    
    random_list.extend((random_car, random_direction, random_step))
    
    return random_list
    
    
if __name__ == "__main__":  
    
    # Creates an instance of the board
    in_file = 'code/Data/Rushhour6x6_1.csv'
    board = board.Board(in_file)
    game = rushhour.RushHour(in_file)
    
    count = 0
    
    # Calls the randomize function 
    info_list = randomizer(board, game.cars)
    
    while True: 
        game.move(info_list[0].name, info_list[1], info_list[2])
        
        count += 1
        print(count)
        if count >= 100000:
            game.print_game(board,game)
            break
        info_list = randomizer(board, game.cars)
        
        # game.print_game(board, game)
        
        
        if game.check_win():
            game.print_game(board, game)
            break
            
    print(count)
   
   
    # game.print_game(board, game)
            
        
    

    
    
    