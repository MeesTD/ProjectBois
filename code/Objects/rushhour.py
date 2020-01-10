from .car import Car
from .board import Board
import csv

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

    # This function will check wheter or not a move is actually possible
    # It checks the route a car would take with the move function and returns True
    # if it is possible and False if it is not possible.
    def check_route(self, car, steps):
        cur_car_coords = self.current_car.xy
        for i in range(steps):
            for j in self.cars:
                if cur_car_coords[0] += steps == self.cars.get("xy").[0] or cur_car_coords[1] += steps == self.cars.get("xy").[2]:
                    return False
        return True

    # This method allows a car to move and returns True if the move is possible
    # Otherwise it returns false.
    def move(self, carname, direction, steps):
        direction = direction
        steps = steps
        self.current_car = self.choose_car(carname)
        if self.check_route(self.current_car, steps):
            if self.current_car.get_orientation() == True:
                # for coords in range(steps):
                #     if self.current_car.get_coords() + 1 != "." and 
                    steps = steps * -1
                    if self.check_route(self.current_car, steps):
                        self.current_car.set_coords(steps)
                        self.check_win()
                        return True
                    else:
                        return False 
                elif direction == "R":
                    if self.check_route(self.current_car, steps):
                        self.current_car.set_coords(steps)
                        self.check_win()
                        return True
                    else:
                        return False
                else:
                    print("Not a valid direction!")
                    return False

            if direction == "U" or if direction == "L":
                steps = steps * -1
            if self.check_route(self.current_car, steps):
                self.current_car.set_coords(steps)
                self.check_win()
                return True
            else:
                return False
            else:
                print("Not a valid direction!")
                return False
        else:
            print ("A car is in the way!")
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
        red_car_coords = self.red_car.get_coords()
        if red_car_coords == self.game.get_winloc:
            return True
        else:
            return False