###################################################################################################
# rushhour.py
#
# Zeno Degenkamp, Mats Pijning, Mees Drissen
#
# This file contains the rushhour object
###################################################################################################
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
        self.output_name = "6x6_3_output.csv"
            
    
    def load_cars(self, in_file):
        """
        This function will load the list of cars from the input file
        """
        
        cars = {}
        
        # Opens the file with the read option
        with open(in_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            
            # Loops through the file and gets all the information of the car and inserts it into cars
            for row in reader:
                cars[row['car']] = Car(row['car'], row[' orientation'], row[' "x'], row['y"'], row[' length'])
        
        return cars


    def check_route(self, carname, direction, steps):
        """
        This function will check wheter or not a move is actually possible, 
        returning True if it is and False if it is not
        """

        # Creates a deep copy of the car and steps so they are not changed
        cur_car_coords = copy.deepcopy(self.cars[carname].xy)
        loc_steps = int(steps)

        # Checks the coordinates of all cars for each step the user wants to take
        for step in range(abs(loc_steps)):
            
            # If a user goes left or down steps has to be negative, because of board index
            if direction == "R" or direction == "L":
                
                # Adds 1 to coordinates to check those coordinates
                for current in range(len(cur_car_coords)):
                    if direction == "L":
                        cur_car_coords[current][0] -= 1 
                    else:
                        cur_car_coords[current][0] += 1.

                    # Do not allow the car to go out of bounds
                    if cur_car_coords[current][0] < 1 or cur_car_coords[current][0] > self.game.size:
                        return False

            # Checks if the car goes up and down
            if direction == "U" or direction == "D":
                
                # Loops through the length of the car coords
                for current in range(len(cur_car_coords)):
                    
                    # Checks if the direction is down or up
                    if direction == "D":
                        cur_car_coords[current][1] -= 1
                    else:
                        cur_car_coords[current][1] += 1
                    
                    # Do not allow the car to go out of bounds
                    if cur_car_coords[current][1] < 1 or cur_car_coords[current][1] > self.game.size:
                        return False

            # Checks if the currently altered coords exist in other cars
            for check_car in self.cars.values():
                
                # Do not check the currently selected car
                if check_car == self.cars[carname]:
                    continue
                for test in cur_car_coords:
                    if test in check_car.xy:
                        return False
        return True


    def move(self, carname, direction, steps):
        """
        This method allows a car to move and returns True if the move is possible,
        otherwise it returns False
        """
        
        # Gets the direction and the current car
        direction = direction
        self.current_car = self.choose_car(carname)
        
        # Checks if orientation has the directions left or Rigth
        if self.current_car.get_orientation():
            if direction == "L" or direction == "R":
                pass
            else:
                return False
        
        # Checks if orientation has the directions up or down
        elif not self.current_car.get_orientation():
            if direction == "U" or direction == "D":
                pass
            else:
                return False
        
        # If the direction is down or left steps is negative
        if direction == "D" or direction == "L":
            steps = steps * -1
        
        # If direction si right or up steps steps is positive
        elif direction == "R" or direction == "U":
            steps = steps
        
        # If the move is possible via the check route method, make move
        if self.check_route(self.current_car.name, direction, steps):
            self.current_car.set_coords(steps)
            self.archive.save_state(self)
            self.archive.add_move(carname, steps)
            return True
            
        # If move is not possible return False
        else:
            return False


    def choose_car(self, name):
        """
        This function will set the current_car variable based on the input of
        a car name
        """
        
        # Loops through the dictionary of all the cars
        for car in self.cars:
            
            # Checks if the name of the chosen is the same as a name of car in the dictionary
            if self.cars[car].name == name:
                chosen_car = self.cars[car]
                break
        
        return chosen_car
    
    
    def check_win(self):
        """
        Method that checks if the game is won, if the game is won writes CSV file with moves
        """
        
        # Gets the coords of the red car
        red_car_coords = self.red_car.get_coords("X")
        
        # If the red car is on win location, write a CSV based on the archive.moves
        if red_car_coords[1] == self.game.get_winloc():
            self.write_output(self.archive)
            return True
        
        # If car is not on win location return False
        else:
            return False


    def print_game(self, board, game):
        """
        This method prints the game board based on the current locations of the cars
        """
        # Initialiaze a variable to be used later.
        name = None

        # Loop over the X and Y axis.
        for Y in reversed(range(board.size + 2)):
                for X in range(board.size + 2):
                    
                    # Print the top of the grid
                    if Y == 0 or Y == board.size + 1:
                        print("-", end="")
                    #  Print the exit.
                    elif X == board.size + 1 and X == math.floor(board.size / 2) + 1:
                        print(">", end="")
                    #  Print the sides of the grid.
                    elif X == 0 or X == board.size + 1:
                        print("|", end="")

                    # Print the inside of the grid.
                    elif X < board.size + 1 or X < board.size + 1:
                        # Check if the current coords match the ones of the cars.
                        for car in game.cars.values():
                            for length in range(len(car.xy)):
                                if car.xy[length][0] == X and car.xy[length][1] == Y:
                                    name = car.name
                        # If it matches one of the cars, print it.
                        if name != None:
                            print(name, end="")
                            name = None
                        # If it doesn't print an empty grid point
                        else:
                            print(".",end="") 
                # End the current X-axis. 
                print("")
    
    
    def write_output(self, archive):
        """
        This method writes a csv file which shows the moves made in the game
        """
        with open(self.output_name, 'w', newline = '') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["car", "steps"])
            for row in archive.moves:
                writer.writerow([row[0], row[1]])
        