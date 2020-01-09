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
        

    def load_cars(self, in_file):
        cars = {}
        
        with open(in_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            for row in reader:
                cars[row['car']] = Car(row['car'], row[' orientation'], row[' "x'], row['y"'], row[' length'])
        return cars

    def check_route(self, car, steps):
        for i in range(steps + 1):
            # loop over the cars and check their coords
            for car in self.cars:
                if self.cars[car].get_orientation:
                    if self.cars[car].x1 or self.cars[car].x2 == 
                        
                    if self.cars[car].length == 3:
                        self.cars[car].x3 != 

                if not self.cars[car].get_orientation:
                    if self.cars[car].y1 ==  or self.cars[car].y2

                    if self.cars[car].length == 3:
                        self.cars[car].y3 != 
        pass

    # This method allows a car to move and returns True if the move is possible
    # Otherwise it returns false.
    def move(self, carname, direction, steps):
        name = carname
        direction = direction
        steps = steps
        for car in self.cars:
            if self.cars[car].name == name:
                self.current_car = self.cars[car]
        if self.check_route(self.current_car, steps):
            if self.current_car.get_orientation() == True:
                if direction == "L":
                    steps = steps * -1
                    self.current_car.set_coords(steps)
                    return True 
                elif direction == "R":
                    self.current_car.set_coords(steps)
                    return True 
                else:
                    print("Not a valid direction!")
                    return False

            if direction == "U":
                steps = steps * -1
                car.set_coords(steps)
                return True 
            elif direction == "D":
                car.set_coords(steps)
                return True 
            else:
                print("Not a valid direction!")
                return False
        else:
            print ("A car is in the way!")
            return False
    
    def choose_car(self, name):
        pass