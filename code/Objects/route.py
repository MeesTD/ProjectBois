from . import car, rushhour, board
import copy
import uuid

class Route(object):

    def __init__ (self):
        self.moves = 0 
        self.archive = {}

    def add_move(self):
        self.moves += 1
        return True

    # This method saves the current grid state to the archive
    def save_state(self, rushhour):
        local_list = copy.deepcopy(rushhour.cars)
        self.archive[hash(rushhour)] = local_list

        return True

    # This method returns true if a grid state exists in the archive, else false.
    def get_state(self, rushhour):
        local_check = rushhour.cars
        for i in self.archive.items():
            if str(local_check) == str(i[1]):
                return True
        return False
        # try:
        #     self.archive[hash(rushhour)]
        #     print("Already in dict")
        #     return True
        # except KeyError:
        #     print("Returning false")
        #     return False
        # for car in car_list.values():
        #     check_list[car.name] = copy.deepcopy(car.xy)
        # for check in self.archive.values():
        #     if check_list == check:
        #         return True
        # return False