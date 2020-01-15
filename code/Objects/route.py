from . import car, rushhour, board
import copy
import uuid

class Route():

    def __init__ (self):
        self.moves = 0 
        self.states = {}

    def add_move(self):
        self.moves += 1
        return True

    # This method saves the current grid state to the states dictionary
    def save_state(self, car_list, key_string):
        # Try except to make sure nothing goes wrong.
        local_list = {}
        for car in car_list.values():
            local_list[car.name] = copy.deepcopy(car.xy)
        self.states[uuid.uuid4().hex] = local_list
        return True

    # This method returns true if a grid state exists in the states dictionary, else false.
    def get_state(self, car_list):
        check_list = {}
        for car in car_list.values():
            check_list[car.name] = copy.deepcopy(car.xy)
        for check in self.states.values():
            if check_list == check:
                return True
        return False