from . import car, rushhour, board
import copy
import math

# This method makes a key based on the rush hour object it recieves as input.
def make_key(rushhour):
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

    def __init__ (self):
        self.moves = 0 
        self.archive = {}

    def add_move(self):
        self.moves += 1
        return True


    # This method saves the current grid state to the archive
    def save_state(self, rushhour):
        key = make_key(rushhour)
        self.archive[key] = key

    # This method returns true if a grid state exists in the archive, else false.
    def get_state(self, rushhour):
        key = make_key(rushhour)
        check = self.archive.get(key, None)
        if check != None:
            return True
        return False