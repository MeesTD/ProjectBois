from .car import Car
from .board import Board
from .route import Route
import csv
import copy
import math

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
        self.archive = Route()
        self.f = 0
        
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
    def check_route(self, carname, direction, steps):

        # Create a deep copy of the car and steps so they are not changed.
        cur_car_coords = copy.deepcopy(self.cars[carname].xy)
        loc_steps = int(steps)

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

            # Check up and down
            if direction == "U" or direction == "D":
                for current in range(len(cur_car_coords)):
                    if direction == "D":
                        cur_car_coords[current][1] -= 1
                    else:
                        cur_car_coords[current][1] += 1
                    # Do not allow the car to go out of bounds.
                    if cur_car_coords[current][1] < 1 or cur_car_coords[current][1] > self.game.size:
                        return False

            # Check if the currently altered coords exist in other cars.
            for check_car in self.cars.values():
                # Do not check the currently selected car.
                if check_car == self.cars[carname]:
                    continue
                for test in cur_car_coords:
                    if test in check_car.xy:
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
        if direction == "D" or direction == "L":
            steps = steps * -1
        elif direction == "R" or direction == "U":
            steps = steps
        if self.check_route(self.current_car.name, direction, steps):
            self.current_car.set_coords(steps)
            self.archive.add_move()
            return True
        else:
            return False

    # This function will set the current_car variable based on the input of
    # a car name.
    def choose_car(self, name):
        for car in self.cars:
            if self.cars[car].name == name:
                chosen_car = self.cars[car]
                break
        return chosen_car

    def check_win(self):
        red_car_coords = self.red_car.get_coords("X")
        if red_car_coords[1] == self.game.get_winloc():
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