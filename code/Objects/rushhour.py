from .car import Car
from .board import Board
import csv
import copy
import math
# key_string = str(archive.moves) + str(info_list[0].name) + str(info_list[1]) + str(info_list[2])


class RushHour():
    """
    This class holds all information relevant to the current game of Rush Hour.
    Including the board (grid) and its cars.
    """
    def __init__ (self, in_file):
        self.game = Board(in_file)
        self.cars = self.load_cars(in_file)
        self.current_car = None
        self.red_car = self.choose_car('X')
        
    # This function will load the list of cars from the input file.
    def load_cars(self, in_file):
        cars = {}
        with open(in_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                cars[row['car']] = Car(row['car'], row[' orientation'], row[' "x'], row['y"'], row[' length'])
        return cars

    # This function will check wheter or not a move is actually possible. 
    # Returning True if it is and False if it is not.
    def check_route(self, car, steps, direction):
        #  Create a deep copy of the car and steps so they are not changed.
        cur_car_coords = copy.deepcopy(self.current_car.xy)
        loc_steps = steps
        # Check the coordinates of all cars for each step the user wants to take.
        for i in range(abs(loc_steps)):
            # If a user goes left or down steps has to be negative. Because of board index
            if direction == "R" or direction == "L":
                # Add 1 to coordinates to check those coordinates
                for current in range(len(cur_car_coords)):
                    if direction == "L":
                        cur_car_coords[current][0] -= 1 
                    else:
                        cur_car_coords[current][0] += 1.
                    # Do not allow the car to go out of bounds.
                    if cur_car_coords[current][0] < 1 or cur_car_coords[current][0] > self.game.size:
                        return False
            if direction == "U" or direction == "D":
                for current in range(len(cur_car_coords)):
                    if direction == "U":
                        cur_car_coords[current][1] -= 1
                    else:
                        cur_car_coords[current][1] += 1
                    # Do not allow the car to go out of bounds.
                    if cur_car_coords[current][1] < 1 or cur_car_coords[current][1] > self.game.size:
                        return False
            # Check if the currently altered coords exist in other cars.
            for car in self.cars.values():
                # Do not check the currently selected car.
                if car == self.current_car:
                    continue
                for test in cur_car_coords:
                    if test in car.xy:
                        return False
        return True

    # This method allows a car to move and returns True if the move is possible
    # Otherwise it returns False.
    def move(self, carname, direction, steps):
        direction = direction
        self.current_car = self.choose_car(carname)
        if self.current_car.get_orientation():
            if direction == "L" or direction == "R":
                pass
            else:
                return False
        elif not self.current_car.get_orientation():
            if direction == "U" or direction == "D":
                pass
            else:
                return False
        if direction == "U" or direction == "L":
            steps = steps * -1
        elif direction == "R" or direction == "D":
            steps = steps
        if self.check_route(self.current_car, steps, direction):
            self.current_car.set_coords(steps)
            return True
        else:
            return False

    # This function will set the current_car variable based on the input of
    # a car name.
    def choose_car(self, name):
        for car in self.cars:
            if self.cars[car].name == name:
                car = self.cars[car]
                break
        return car

    def check_win(self):
        red_car_coords = self.red_car.get_coords("X")
        test = self.game.get_winloc()
        if red_car_coords[1] == test:
            return True
        else:
            return False

    def print_game(self, board, game):
        name = None
        for i in reversed(range(board.size + 2)):
                for j in range(board.size + 2):
                    if i == 0 or i == board.size + 1:
                        print("-", end="")
                    elif j == board.size + 1 and i == math.floor(board.size / 2) + 1:
                        print(">", end="")
                    elif j == 0 or j == board.size + 1:
                        print("|", end="")
                    elif j < board.size + 1 or j < board.size + 1:
                        for car in game.cars.values():
                            for l in range(len(car.xy)):
                                if car.xy[l][0] == j and car.xy[l][1] == i:
                                    name = car.name
                        if name != None:
                            print(name, end="")
                            name = None
                        else:
                            print(".",end="")         
                print("")