import csv 
from objects import Car, Board


class RushHour(self):
    """
    This class holds all information relevant to the current game of Rush Hour.
    Including the board (grid) and its cars.
    """

    def __init__ (self, game):
        game = game
        if game[8] != "1":


if __name__ == "__main__":
    game = argv[2]
    rush_hour = RushHour(game)

    f = open("test3x3.csv")
    reader = csv.reader(f)
    next(reader)
    board = Board(3)
    for car, orientation, x, y, length in reader:
        car = Car(car, orientation, x, y ,length)
        board.cars.append(car)



    print(car)

    print(board)
