import csv 
from objects import Car, Board

# # initializes board
# bord = []
#
# # Creates the rows
# row1 = [1, 2, 3]
# row2 = [4, 5, 6]
# row3 = [7, 8, 9]
#
# # Appends the rows in the board
# bord.append(row1)
# bord.append(row2)
# bord.append(row3)

f = open("test3x3.csv")
reader = csv.reader(f)
next(reader)
board = Board(3)
for car, orientation, x, y, length in reader:
    car = Car(car, orientation, x, y, length)
    board.cars.append(car)
    board.grid = car.x - 1 
    board.grid = car.y - 1

print(car)

print(board)
