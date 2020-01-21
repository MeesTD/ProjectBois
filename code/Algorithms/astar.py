import copy
import queue
from ..Objects import board, car, rushhour, route
from .breadthfirst_2 import Breadthfirst

class Astar(object):
    """
    Class for the A* algorithm
    """
    def __init__(self, infile):
        self.first_state = rushhour.RushHour(infile)
        self.open_list = []
        self.closed_list = []
        self.infile = infile
        self.moves = 0
    


        # Initialize the first state
        self.open_list.append(copy.deepcopy(self.first_state))
        
    def functionality(self):
        """
        Method that contains all the logic for the A star algorithm
        """

        # Creates a Breadthfirst instance to use the get possibilities method
        a = Breadthfirst(self.infile)

        # Runs while open list is not empty
        while len(self.open_list) > 0:
            
            

            # Gets the first state in the open list
            current_state = self.open_list[0]

            current_state.print_game(current_state.game, current_state)
            current_index = 0

            # Removes the state from the open list and adds to closed list
            self.open_list.pop(current_index)
            self.closed_list.append(current_state)

            # Updates the moves variable
            self.moves +=1 

            # Checks if the current state is winning state
            if current_state.check_win():
                print("Moves", self.moves)
                break
            
            all_options = []
            
            # Loops through all the cars of the current state
            for car in current_state.cars.values():
                
                # Gets the possibilities per car 
                possibility = a.get_possibilities(car, current_state)

                # If the possiblities are not an empty list append to list for all options
                if possibility != []:
                    all_options.append(possibility)

            # Gets all the children of the current state 
            all_children = self.make_children(current_state, all_options)

            # Updates the f attribute of the children 
            self.f_value(current_state, all_children, self.moves)

            # Gets the child with the lowest f value and appends to open list
            best_child = self.choose_child(all_children, self.closed_list)
            self.open_list.append(best_child)

        


    def make_children(self, current_state, all_options):
        """
        Makes the children for the current state
        """
        all_children = []

        # Goes through the options per car
        for options_car in all_options:
            # Moves the car and creates a new state
            for move in options_car:
                child_game = copy.deepcopy(current_state)
                child_game.move(move[0], move[1], move[2])
                all_children.append(child_game)

        return all_children

    def f_value(self, current_state, all_children, moves):
        """
        Calculates all the f value for all the children
        """
        blocking_cars = 0
        
        # Loops through all the children
        for child in all_children:

            blocking_cars = 0
            
            # Loops through all the cars of the child
            for car in child.cars.values():
                
                # Only check other cars than red car
                if not car.name == "X":
               
                    # Checks if cars are in the way of the red car and updates blocking car
                    if car.xy[0][1]  == current_state.red_car.xy[0][1] or car.xy[1][1] == current_state.red_car.xy[0][1]:
                        blocking_cars += 1
                    
            # Updates the f attribute of the child
            child.f = blocking_cars + self.moves
            
        return True

    def choose_child(self, all_children, closed_list):
        """
        Method that chooses the best child with the lowest f value
        """

        # Loops through all the children
        for child in all_children:
            print(child, closed_list)
            if not child in closed_list: 
                # Makes the first child the best child
                best_child = all_children[0]
            
                # Searches the best child 
                if child.f < best_child.f: 
                    best_child = child.f
    
        return best_child

