from Objects import Board, Car
import csv

class RushHour():
    """
    This class holds all information relevant to the current game of Rush Hour.
    Including the board (grid) and its cars.
    """

    def __init__ (self, in_file):
        # size = game
        board = Board(in_file)
        self.cars = load_cards(in_file)
        self.current_car = None

    def load_cars(self, in_file):
        cars = {}
        with open(in_file, 'r') as reader:
            reader = csv.DictReader(infile)
            for row in reader:
                cars[row['name']] = Car(row['orientation'], row['x'], row['y'], row['length'])
            return cars

    # This method allows a car to move and returns True if the move is possible
    # Otherwise it returns false.
    def move(self, carname, direction, steps):
        name = carname
        direction = direction
        steps = steps
        for car in self.cars:
            if car.name == name:
                self.current_car = car
        if car.get_orientation() == True:
            if direction == "L":
                steps = steps * -1
                car.set_coords(car.name, steps)
                return True 
            elif direction == "R":
                car.set_coords(car.name, steps)
                return True 
            else:
                print("Not a valid direction!")
                return False

        if direction == "U":
            steps = steps * -1
            car.set_coords(car.name, steps)
            return True 
        elif direction == "D":
            car.set_coords(car.name, steps)
            return True 
        else:
            print("Not a valid direction!")
            return False
    
    def choose_car(self, name):

    