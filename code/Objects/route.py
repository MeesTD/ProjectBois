###################################################################################################
# route.py
#
# Zeno Degenkamp, Mats pijning, Mees drissen
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
    
    key_build = []
    name = None
    
    
    for i in reversed(range(rushhour.game.size + 2)):
        for j in range(rushhour.game.size + 2):
            if i == 0 or i == rushhour.game.size + 1:
                key_build.append("-")
            elif j == rushhour.game.size + 1 and i == math.floor(rushhour.game.size / 2) + 1:
                key_build.append(">")
            elif j == 0 or j == rushhour.game.size + 1:
                key_build.append("|")
            elif j < rushhour.game.size + 1 or j < rushhour.game.size + 1:
                for car in rushhour.cars.values():
                    for l in range(len(car.xy)):
                        if car.xy[l][0] == j and car.xy[l][1] == i:
                            name = car.name
                if name != None:
                    key_build.append(name)
                    name = None
                else:
                    key_build.append(".")         
        key_build.append("\n")
    separator = ','
    key_string = separator.join(key_build)
    return key_string.replace(',', '')

class Route(object):
    """
    The route object saves the moves and their relations to a state. 
    """

    def __init__ (self):
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
