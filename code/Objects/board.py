###################################################################################################
# board.py
#
# Zeno Degenkamp, Mats Pijning, Mees Drissen
#
# The Board object will initiate a grid, which consists of a matrix, which consists of a list of lists.
# Upon this grid the algorithms will make calculations and “move” cars.
###################################################################################################
import os
import math


class Board(object):
    """
    The board class will initiate a grid which consists of a matrix which consists of a list of lists.
    The board size and win_location are based on the size of the board.
    """
    
    def __init__(self, input_file):
        self.size = self.load_grid(input_file)
        self.grid = []
        self.win_location = self.set_winlocation(self.size)
        
        # Creates the y-coords based on the size of the board
        for Y in range(self.size):
            
            coordsY = Y + 1
            X_axis = []
            
            # Creates the x-coords based on the size of the board
            for X in range(self.size):
                
                coordsX = X + 1
                
                # Creates the points with a X and a Y coord
                totalcords = [coordsY, coordsX] 
                
                # Appends all the coords in totalcords
                X_axis.append(totalcords)
            
            self.grid.append(X_axis)

  
    def load_grid(self, input_file):
        """
        Function that reads the title of the CSV file and retreives the board size
        """
        
        size = 0
        
        # Checks if appropriate size is in filename, if not gives error
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
        """
        This function sets the win location of the current board
        """
        
        win_coords = []
        
        # Retrieves the coords of the win location
        winX = self.size
        winY = math.floor(size / 2) + 1
        
        # Creates the win coords variable
        win_coords.append(winX)
        win_coords.append(winY)
        
        return win_coords

    
    def get_winloc(self):
        """
        Gets the win location of the board
        """
        return self.win_location

    
    def __repr__(self):
        return f"{self.win_location} {self.grid} {self.size}"
