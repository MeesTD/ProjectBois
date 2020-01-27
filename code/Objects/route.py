###################################################################################################
# route.py
#
# Zeno Degenkamp, Mats Pijning, Mees Drissen
#
# This file contains the route object
###################################################################################################
from . import car, rushhour, board
import copy
import math


def make_key(rushhour):
    """
    This method makes a key based on the rush hour object it recieves as input.
    """
    # Initialize necessary values.
    key_build = []
    name = None
    
    #  Loop over the X and Y axis of the grid. 
    for Y in reversed(range(rushhour.game.size + 2)):
        for X in range(rushhour.game.size + 2):

            # Append the top and bottom of the board.
            if Y == 0 or Y == rushhour.game.size + 1:
                key_build.append("-")
            # Append the exit of the board.
            elif X == rushhour.game.size + 1 and Y == math.floor(rushhour.game.size / 2) + 1:
                key_build.append(">")
            # Append the sides.
            elif X == 0 or X == rushhour.game.size + 1:
                key_build.append("|")
            
            # Append the inside of the grid.
            elif X < rushhour.game.size + 1 or X < rushhour.game.size + 1:
                for car in rushhour.cars.values():

                    # Check if the current car matches the current coords.
                    for length in range(len(car.xy)):
                        if car.xy[length][0] == X and car.xy[length][1] == Y:
                            name = car.name
                # append the name of the car at these coords.
                if name != None:
                    key_build.append(name)
                    name = None
                
                # If there is no car print a ".".
                else:
                    key_build.append(".") 
        # Finished a X- axis.
        key_build.append("\n")
    separator = ','
    key_string = separator.join(key_build)
    return key_string.replace(',', '')


class Route(object):
    """
    The route object saves the moves and their relations to a state. 
    """

    def __init__ (self):
        # Initialize a move amount int, an archive for keys and list for moves made.
        self.move_amount = 0 
        self.archive = {}
        self.moves = []

    
    def add_move(self, carname, steps):
        """
        This method adds 1 to move_amount for a move made and also appends the car and it's steps to the list of moves
        """
        
        self.move_amount += 1
        move_list = []
        move_list.append(carname)
        move_list.append(steps)
        self.moves.append(move_list)


    def save_state(self, rushhour):
        """
        This method saves the current grid state to the archive
        """
        
        key = make_key(rushhour)
        self.archive[key] = key


    def get_state(self, rushhour):
        """
        This method returns true if a grid state exists in the archive, else false
        """
        
        key = make_key(rushhour)
        check = self.archive.get(key, None)
        if check != None:
            return True
        return False
