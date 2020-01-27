###################################################################################################
# astar_lookahead.py
#
# Zeno Degenkamp, Mats Pijning, Mees Drissen
#
# This file contains the astar revers algorithm. The algorithm starts at start state and at the 
# final state until it finds eachother. The algorithm uses look ahead to find the move with the
# best f-value. The F value is based on the amount of overlapping cars, more overlapping cars 
# gives a higher f-value. The algorithm also stops searching for the solution when the red car 
# has a free path to the exit, due to x_checker. Because a free path implies that the red car 
# has a way to get to the exit. 
###################################################################################################
import copy
import queue
import random
from .breadthfirst import get_possibilities
from ..Algorithms import randomize, breadthfirst_prio
from ..Objects import board, car, rushhour, route, lookahead
from ..Objects.route import make_key


def make_children(current_state, all_options, final_state):
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

        # Updates the f attribute of the children 
        calc_f_value(all_children, final_state)

        return all_children


def calc_f_value(all_children, final_state):
        """
        Calculates all the f value for all the children
        """
                
        # Loops through all children 
        for child in all_children:
            
            # Counter that counts all the wrongly positioned cars
            wrong_cars = 0
            
            # Loops through through all cars of the child
            for car in child.cars.values(): 
            
                # Loops through all the cars of the final state
                for car2 in final_state.cars.values(): 
                    
                    # If the coords of the red car are the same only adds 0.5 wrong cars
                    if car.name == "X" and car2.name == "X":
                        if car.xy == car2.xy:
                            wrong_cars += 0.5
                    
                    # Adds 2 for every car that is positioned differently on the two states
                    else:
                        if car.xy != car2.xy:
                            wrong_cars += 2
            
            # Updates the f attribute of the child object           
            child.f = wrong_cars + child.archive.move_amount
     
        
class Astar(object):
    """
    Class for the A* algorithm with the reverse alternative. This algorithm starts both at the 
    start and at the end, and then works to each other with the moves. 
    """
    
    
    def __init__(self, infile):
        self.first_state = rushhour.RushHour(infile)
        self.final_state = randomize.run(self.first_state)
        self.open_list = []
        self.open_list_reversed = []
        self.closed_list = set()
        self.infile = infile
        self.moves = 0
        self.lookahead_amount = 4

        # Initialize the first state and the final state
        self.open_list.append(copy.deepcopy(self.first_state))
        self.open_list_reversed.append(copy.deepcopy(self.final_state))
        
   
    def get_best_child(self, current_state, goal_state):
        """
        Method gets the best child using the current state and the goal state and the look ahead method
        """
        
        # Gets all the best children of the current state
        all_children = lookahead.lookahead(current_state, self.lookahead_amount, goal_state)

        # Gets the child with the lowest f value
        best_child = self.choose_child(all_children, self.closed_list)
            
        # Prints the best child
        best_child.print_game(best_child.game, best_child)
            
        # Appends the best child to open list
        return best_child
            

    def choose_child(self, all_children, closed_list):
        """
        Method that chooses the best child with the best f value
        """
        
        # Randomily chooses one of the child states as best child
        length = len(all_children)
        index = random.randrange(1, length)
        best_child = all_children[index]

        # Loops through all the children
        for child in all_children:
            
            # Makes a string of the board of the child
            str_child = make_key(child)
            
            # If child already exists in list pass.
            if str_child in closed_list:
                pass 
                
            # Else if the child f value is better set child to be that
            elif child.f < best_child.f:
                best_child = copy.deepcopy(child)
            
        return best_child
        

    def functionality(self):
        """
        Method that contains all the logic for the A star algorithm
        """

        # Initializes the counts 
        count = 0
        self.favourite_count = 0

        # Loops while length of open list is more than zero and counts less than 1500
        while len(self.open_list) > 0 and count < 1500:
            count += 1
            
            current_index = 0
            
            # Gets the first states of both directions
            current_state = self.open_list.pop(current_index)
            current_state_reversed = self.open_list_reversed.pop(current_index)
            
            # Checks if the red car is able to move to winning position
            if breadthfirst_prio.x_checker(current_state):
                # Checks if the current state is winning state
                if current_state.check_win():
                    print(current_state.archive.move_amount, "Red car won ( ͡ʘ ͜ʖ ͡ʘ)")
                    break
            
            # Checks if the states overlap in state, in this case the winning state
            if make_key(current_state) == make_key(current_state_reversed):
                self.moves = current_state.archive.move_amount + current_state_reversed.archive.move_amount
                print(self.moves, "State found won( ͡ʘ ͜ʖ ͡ʘ)")
                break
              
            # Creates a str of the state and the reversed state
            str_current_state = make_key(current_state)
            str_current_state_reversed = make_key(current_state_reversed)
            
            self.closed_list.add(str_current_state)  

            # Updates the moves variable
            self.moves +=1 
            
            # Gets the best child for the normale route 
            best_child = self.get_best_child(current_state, current_state_reversed)
            self.open_list.append(best_child)
            
            # Gets the best child for the reversed route
            best_child_reversed = self.get_best_child(current_state_reversed, best_child)
            self.open_list_reversed.append(best_child_reversed)
            
            
