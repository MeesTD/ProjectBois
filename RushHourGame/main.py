import csv 
import math
from objects import Car, Board


class RushHour(object):
    """
    This class holds all information relevant to the current game of Rush Hour.
    Including the board (grid) and its cars.
    """

    def __init__ (self):
        # size = game
        # board = Board(size)
        cars = self.get_cars()
        pass

    def get_cars(self):
        self.cars = []
        f = open("test3x3.csv")
        reader = csv.reader(f)
        next(reader)
        for car, orientation, x, y, length in reader:
            car = Car(car, orientation, x, y ,length)
            self.cars.append(car)
        return(f"{self.cars}")

    def load_cars(self):
        #TODO
        pass

    def move(self, carname, direction, steps):
        #TODO
        pass
    
    


if __name__ == "__main__":
    # game = argv[2]
    # rush_hour = RushHour(game)
    # board = Board(3)
    # game = RushHour()
    # print(board)
    f = open("test3x3.csv")
    reader = csv.reader(f)
    next(reader)
    cars = []
    for car, orientation, x, y, length in reader:
        car = Car(car, orientation, x, y ,length)
        cars.append(car)
    board = Board(3)
    name = None
    for i in range(board.size + 2):
        for j in range(board.size + 2):
            if i == 0 or i == board.size + 1:
                print("-", end=" ")
            elif j == board.size + 1 and i == math.ceil(board.size / 2):
                print(">", end=" ")
            elif j == 0 or j == board.size + 1:
                print("|", end=" ")
            elif i < board.size + 1 or j < board.size + 1:
                for car in cars:
                    if car.x == j and car.y == i:
                        name = car.name
                    if  name != None:
                        print(car.orientation == 'H')
                        print(car.orientation)
                        if car.orientation == 'H':
                            print(car.length * car.name, end=" ")
                        name = None
                        break
                else:
                    print (".", end=" ")
        print("")
    



