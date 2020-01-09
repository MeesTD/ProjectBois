class RushHour(object):
    """
    This class holds all information relevant to the current game of Rush Hour.
    Including the board (grid) and its cars.
    """

    def __init__ (self):
        # size = game
        # board = Board(size)
        pass

    def load_cars(self):
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

    def move(self, carname, direction):
        name = carname
        direction = direction
        steps = 1
        for car in self.cars:
            if car.name == name:
                cur_car = car
        
        
    