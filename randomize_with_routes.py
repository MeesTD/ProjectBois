import random
from code.Objects import board, car, rushhour, route

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
    
    in_file = 'code/Data/Rushhour6x6_2.csv'
    board = board.Board(in_file)
    
    sum_counts = []
    sum_avg = []
    
    
    while len(sum_counts) < 50: 
        
        # Creates an instance of the board
        
        archive = route.Route()

        game = rushhour.RushHour(in_file)

        # Calls the randomize function 
        info_list = randomizer(board, game.cars)
        
        # Loop runs while solution is not found
        while True: 
            
            # Calls the randomize function
            info_list = randomizer(board, game.cars)

            # Checks if move is valid with random variables
            if game.move(info_list[0].name, info_list[1], info_list[2]) and archive.get_state(game.cars) == False:
                # Updates the counter 
                archive.add_move()

                # Add the current move to archive
                archive.save_state(game.cars)

                # Checks if the limit is reached 
                if archive.moves >= 1000000:
                    game.print_game(board,game)
                    break
        
            # Checks if the game is won and stops the loop
            if game.check_win():
                print(archive.states)
                game.print_game(board, game)
                sum_counts.append(archive.moves)
                break
    
    # Calculates the average of the solutions
    avg = sum(sum_counts)/len(sum_counts)
    sum_avg.append(avg)
    print(sum_avg)
        
    

    
    
    