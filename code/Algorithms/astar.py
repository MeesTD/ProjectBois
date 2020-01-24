import copy
import queue
from .Heuristics.closethedistance import calc_h as closethedistance
from .Heuristics.pathfree import calc_h as pathfree
from ..Objects import board, car, rushhour, route, lookahead
from .breadthfirst import get_possibilities
from ..Objects.route import make_key
import random

def make_children(current_state, all_options, algorithm):
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
        calc_f_value(all_children, algorithm)

        return all_children

def calc_f_value(all_children, algorithm):
        """
        Calculates all the f value for all the children
        """ 

        


class Astar(object):
    """
    Class for the A* algorithm
    """
    def __init__(self, infile):
        self.first_state = rushhour.RushHour(infile)
        self.open_list = []
        self.closed_list = set()
        self.infile = infile
        self.moves = 0
        self.lookahead_amount = 5

        # Initialize the first state
        self.open_list.append(copy.deepcopy(self.first_state))

        
    def functionality(self):
        """
        Method that contains all the logic for the A star algorithm
        """

        # Runs while open list is not empty
        count = 0
        self.favourite_count = 0
        print("Which algorithm would you like to run?")
        algorithms = ["pathfree", "closethedistance"]
        for algorithm in algorithms:
            print(algorithms.index(algorithm),":", algorithm)
        print("Choose the number.")
        algorithm = input(">")


        while len(self.open_list) > 0 and count < 1500:
            count += 1

            # Gets the first state in the open list
            current_index = 0
            current_state = self.open_list.pop(current_index)

            # print("begin game")
            # current_state.print_game(current_state.game, current_state)


            X_from_exit = current_state.game.size - int(current_state.red_car.xy[1][1] - 1)
            print(X_from_exit)
            if current_state.check_route("X", "R", X_from_exit):
                print("Check done.")
                current_state.move("X", "R", X_from_exit)

             # Checks if the current state is winning state
            if current_state.check_win():
                print(current_state.archive.moves, "( ͡ʘ ͜ʖ ͡ʘ)")
                # print("Moves", self.moves)
                break

            # Removes the state from the open list and adds to closed list
            str_current_state = make_key(current_state)
            self.closed_list.add(str_current_state)
          

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
            all_children = lookahead.lookahead(current_state, self.lookahead_amount, algorithm)

            # Gets the child with the lowest f value and appends to open list
            best_child = self.choose_child(all_children, self.closed_list)

            best_child.print_game(best_child.game, best_child)
            self.open_list.append(best_child)

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

