import copy
import queue
from ..Objects import board, car, rushhour, route, lookahead
from .breadthfirst import get_possibilities
from ..Objects.route import make_key
from ..Algorithms import randomize
import random

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
                    
                    if car.name == "X" and car2.name == "X":
                        
                        if car.xy == car2.xy:
                            wrong_cars += 0.5
                    else:
                        
                        # Checks if the coords are not the same 
                        if car.xy != car2.xy:
                        
                            wrong_cars += 2
            
            # Updates the f attribute of the child object           
            child.f = wrong_cars + child.archive.move_amount
        
class Astar(object):
    """
    Class for the A* algorithm
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

        # Initialize the first state
        self.open_list.append(copy.deepcopy(self.first_state))
        self.open_list_reversed.append(copy.deepcopy(self.final_state))
        

        
    def functionality(self):
        """
        Method that contains all the logic for the A star algorithm
        """

        # Runs while open list is not empty
        count = 0
        self.favourite_count = 0

        while len(self.open_list) > 0 and count < 1500:
            count += 1

            # Gets the first state in the open list
            current_index = 0
            current_state = self.open_list.pop(current_index)
            current_state_reversed = self.open_list_reversed.pop(current_index)

       
             # Checks if the current state is winning state
            if make_key(current_state) == make_key(current_state_reversed):
                self.moves = current_state.archive.move_amount + current_state_reversed.archive.move_amount
                print(self.moves, "( ͡ʘ ͜ʖ ͡ʘ)")
                break
              

            # Removes the state from the open list and adds to closed list
            str_current_state = make_key(current_state)
            str_current_state_reversed = make_key(current_state_reversed)
            
            self.closed_list.add(str_current_state)
            #self.closed_list.add(str_current_state_reversed)
          
            

            # Updates the moves variable
            self.moves +=1 

            all_options = []
            
            # Loops through all the cars of the current state
            for car in current_state.cars.values():
                
                # Gets the possibilities per car 
                possibility = get_possibilities(car, current_state)

                # If the possiblities are not an empty list append to list for all options
                if possibility != []:
                    all_options.append(possibility)

            # Gets all the best children of the current state 
            all_children = lookahead.lookahead(current_state, self.lookahead_amount, current_state_reversed)

            # Gets the child with the lowest f value and appends to open list
            best_child = self.choose_child(all_children, self.closed_list)
            
            print("DIT IS DE NORMALE ROUTE")
            best_child.print_game(best_child.game, best_child)
            
            self.open_list.append(best_child)
            
            if best_child.check_win():
                print(f"You've won with{best_child.archive.move_amount} moves!")
                break
            
            
            # ALL FUNCTIONS FOR REVERSED
            
            
            for car in current_state_reversed.cars.values():
                
                # Gets the possibilities per car 
                possibility = get_possibilities(car, current_state_reversed)
                
                # If the possiblities are not an empty list append to list for all options
                if possibility != []:
                    all_options.append(possibility)
                
            # Gets all the best children of the current state 
            all_children = lookahead.lookahead(current_state_reversed, self.lookahead_amount, best_child)

            # Gets the child with the lowest f value and appends to open list
            best_child = self.choose_child(all_children, self.closed_list)
            
            print("DIT IS DE REVERSED ROUTE")
            best_child.print_game(best_child.game, best_child)
            
            self.open_list_reversed.append(best_child)
            

    def choose_child(self, all_children, closed_list):
        """
        Method that chooses the best child with the lowest f value
        """

        length = len(all_children)
        index = random.randrange(1, length)
        best_child = all_children[index]

        # Loops through all the children
        for child in all_children:

            str_child = make_key(child)
            
            # If child already exists in list pass.
            if str_child in closed_list:
                # print("VROOOOOM")
                pass 
                
            # Else if the child f value is better set child to be that
            elif child.f < best_child.f:
                best_child = copy.deepcopy(child)
            
        
        return best_child