###################################################################################################
# Board.py
#
# AUTHORS
#
# UITLEG
###################################################################################################
import os
import math

class Board(object):
    """
    This class will initiate a grid which consists of a matrix which consists of a list of lists.
    """
    
    # Initializes a board object 
    def __init__(self, input_file):
        # Board properties
        self.size = self.load_grid(input_file)
        self.grid = []
        self.win_location = self.set_winlocation(self.size)
        for i in range(self.size):
            coordsY = i + 1
            X_axis = []
            for j in range(self.size):
                
                coordsX = j + 1
                
                totalcords = [coordsY, coordsX] 
                
                X_axis.append(totalcords)
            self.grid.append(X_axis)

    # This function sets the size based on the input file's filename. 
    def load_grid(self, input_file):
        """
        Function that reads the title of the CSV file and retreives the board size
        """
        size = 0
        
        # Checks if appropriate size is in filename (Kan dynamischer?)
        if "3x3" in input_file:
            size = 3
        elif "6x6" in input_file:
            size = 6
        elif "9x9" in input_file:
            size = 9
        elif "12x12" in input_file:
            size = 12
        else:   
            return ("Cant't find board with given input, please try again!")
        return size

    # This function sets the win location of the current board.
    def set_winlocation(self, size):
        win_coords = []
        winX = self.size
        winY = math.floor(size / 2) + 1
        win_coords.append(winX)
        win_coords.append(winY)
        return win_coords

    def get_winloc(self):
        return self.win_location

    def __repr__(self):
        return f"{self.win_location} {self.grid} {self.size}"
