import queue
import copy
from code.Objects import board, car, rushhour

def make_nodes(board, cars):
    """
      
    """
    
    all_nodes = []

    
    # Loops until all values of state space are checked
    for move in range(1000000)
    
        # Iterates over every single car and checks possible moves
        for car in cars.keys():
        
            # Calculates the max steps for each car
            max_steps = (board.size - car.length) + 1
        
            # Checks car orientation
            if car.get_orientation: 
                directions = ['L', 'R']
            else:
                directions = ['U', 'D']
        
                # Loops through directions
                for i in directions:
                    
                    # Loops through all possible steps 
                    for j in range(1, max_steps):
                        
                        # Checks if move is possible 
                        if Rushhour.check_route(car, j, i):
                            
                            # Moves the car 
                            Rushhour.move(carname, j, i)
                            
                            
                            
                            move
                    
                    
                    
                
        
        
        Rushhour.check_route()
    
   
    
    
    
    
    
    
       def check_route(self, car, steps, direction):
           

    
    
                    

