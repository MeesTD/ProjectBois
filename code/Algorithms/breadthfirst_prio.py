###################################################################################################################
# breadthfirst_prio.py
#
# Zeno Degenkamp, Mats Pijning, Mees Drissen
#
# This file contains the breadthfirst with priority queue algorithm. This algorithm creates children 
# and selects a child with the lowest F-value. The F-value of a child is based upon the amount of 
# moves already made (G) and the amount of vehicles that occupy space on the y-axis of the red car (H). G + H = F. 
# The child with the lowest F-value is then added to the openlist, or the priority queue. 
# These are the favourite children. The algorithm changes it's current state to the first entry 
# in the openlist and the process begins again until the puzzle has been completed.
####################################################################################################################
import copy
import queue
import random
from .breadthfirst import get_possibilities
from ..Algorithms import astarreverse
from ..Objects import board, car, rushhour, route, lookahead
from ..Objects.route import make_key


def make_children(current_state, all_options):
        """
        Makes the children for the current state
        """
        
        all_children = []
        
        # Goes through the options per car.
        for options_car in all_options:
            
            # Moves the car and creates a new state.
            for move in options_car:
                child_game = copy.deepcopy(current_state)
                child_game.move(move[0], move[1], move[2])
                all_children.append(child_game)

        # Updates the f attribute of the children.
        calc_f_value(all_children)

        return all_children


def calc_f_value(all_children):
        """
        Calculates all the f value for all the children
        """
        blocking_cars = 0
        
        # Loops through all the children.
        for child in all_children:

            blocking_cars = 0
            
            # Loops through all the cars of the child.
            for car in child.cars.values():
                
                # Only check other cars than red car.
                if not car.name == "X":
               
                    # Checks if cars are in the way of the red car and updates blocking car.
                    if car.xy[0][1]  == child.red_car.xy[0][1] or car.xy[1][1] == child.red_car.xy[0][1]:
                        blocking_cars += 1

                    # Checks if the car has a length of 3.
                    if car.length == 3:
                        # Checks if this car is blocking the red car.
                        if car.xy[2][1] == child.red_car.xy[0][1]:
                            blocking_cars += 1
                    
            # Updates the f attribute of the child.
            child.f = blocking_cars + child.archive.move_amount
            
            
def x_checker(current_state):
    """
    Method checks if red car is able to move to win location, returns True if possible else False
    """
    
    # Gets the x coords of the exit.
    X_from_exit = current_state.game.size - int(current_state.red_car.xy[1][0])
    
    # If the red car is able to move to the exit, move and return True, else return False.
    if current_state.check_route("X", "R", X_from_exit):
        current_state.move("X", "R", X_from_exit)
        return True
        
    return False
     
        
class Breadthfirst_prio(object):
    """
    Class breadthfirst with priority queue algorithm
    """
    
    
    def __init__(self, infile):

        # Initializes the necessary variables.
        self.first_state = rushhour.RushHour(infile)
        self.open_list = []
        self.closed_list = set()
        self.infile = infile
        self.moves = 0
        self.lookahead_amount = int(input= "How many steps would you like to look ahead? ")

        # Initializes the first state.
        self.open_list.append(copy.deepcopy(self.first_state))

        
    def functionality(self):
        """
        Method that contains all the logic for breadthfirst with priority queue algorithm
        """

        # Initializes the counts.
        count = 0
        self.favourite_count = 0
        
        # Runs while open list is not empty.
        while len(self.open_list) > 0 and count < 1500:
            
            count += 1

            # Gets the first state in the open list.
            current_index = 0
            current_state = self.open_list.pop(current_index)
            
            # Checks if red car is able to move to win location.
            if x_checker(current_state):
                pass
            
            # Checks if the current state is winning state.
            if current_state.check_win():
                return current_state
                    
            # Removes the state from the open list and adds to closed list.
            str_current_state = make_key(current_state)
            self.closed_list.add(str_current_state)
          
            # Updates the moves variable.
            self.moves +=1 

            all_options = []
            
            # Loops through all the cars of the current state.
            for car in current_state.cars.values():
                
                # Gets the possibilities per car.
                possibility = get_possibilities(car, current_state)

                # If the possiblities are not an empty list append to list for all options.
                if possibility != []:
                    all_options.append(possibility)

            # Gets all the best children of the current state.
            all_children = lookahead.lookahead(current_state, self.lookahead_amount)

            # Gets the child with the lowest f value and prints it and appends to open list.
            best_child = astarreverse.choose_child(all_children, self.closed_list)
            self.open_list.append(best_child)

        current_state.print_game(current_state.game, current_state)
        print(f"Finished with {len(current_state.archive.moves)} moves")

        return current_state
