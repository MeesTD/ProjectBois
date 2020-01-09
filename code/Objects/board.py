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
        self.win_location = self.set_winlocation
        for i in range(self.size):
            coordsY = i + 1
            X_axis = []
            for j in range(self.size):
                
                coordsX = j + 1
                
                totalcords = [coordsY, coordsX] 
                
                X_axis.append(totalcords)
            self.grid.append(X_axis)
    
    def __str__(self):
        return f"{self.grid}"
        
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

    def set_winlocation(self, size):
        win = math.ceil(size / 2)
        return win
