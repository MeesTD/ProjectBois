from .car import Car
from .board import Board
import csv
import copy

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

    # This function will check wheter or not a move is actually possible returning True if it is and False if it is not.
    # Achteruit collision doet het nog niet
    def check_route(self, car, steps, direction):
        cur_car_coords = copy.deepcopy(self.current_car.xy)
        if steps < 0:
            steps = abs(steps)
        for i in range(steps):
            for j in cur_car_coords:
                if direction == "R" or direction == "L":
                    for current in range(len(cur_car_coords)):
                        cur_car_coords[current][0] += 1
                if direction == "U" or direction == "D":
                    for current in range(len(cur_car_coords)):
                        cur_car_coords[current][1] += 1
            for car in self.cars.values():
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
                print("Not a valid direction")
                return False
        elif not self.current_car.get_orientation():
            if direction == "U" or direction == "D":
                pass
            else:
                print("Not a valid direction")
                return False
        if direction == "U" or direction == "L":
            steps = steps * -1
        elif direction == "R" or direction == "D":
            steps = steps
        if self.check_route(self.current_car, steps, direction):
            print("Making a move.")
            self.current_car.set_coords(steps)
            self.check_win()
            return True
        else:
            print("A car is in the way.")
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
        if red_car_coords == self.game.get_winloc:
            return True
        else:
            return False