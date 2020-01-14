from . import car, rushhour, board
import copy

def __init__ (self):
    self.moves = 0 
    self.states = {}

def add_move(self):
    self.moves += 1
    return True

# This method saves the current grid state to the states dictionary
def save_state(self, car_list):
    # Try except to make sure nothing goes wrong.
    try:
        local_list = tuple(copy.deepcopy(car_list))
        self.states[hash(local_list)] = local_list
        return True
    except:
        return False

# This method returns true if a grid state exists in the states dictionary, else false.
def get_state(self, car_list):
    hashed_newlist = hash(tuple(car_list))
    if self.states.get(hashed_newlist):
        return True
    else:
        return False