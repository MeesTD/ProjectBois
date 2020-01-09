###################################################################################################
# Board.py
#
# AUTHORS
#
# UITLEG
###################################################################################################
import os

class Board(object):
    """
    This class will initiate a grid which consists of a matrix which consists of a list of lists.
    """
    
    # Initializes a board object 
    def __init__(self, input_file):
        # Board properties
        self.size = load_grid(input_file)
        self.grid = []
        # self.win_location = ...
        
        # Loads the bord
        loadgrid("infile")
        
        for i in range(size):
            coordsY = i + 1
            X_axis = []
            for j in range(size):
                
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
        
        # Retreives all the filenames in de data folder
        for filename in os.listdir("/code/data"):
            # Double checks if file is a board
            if filename.endswith(".csv"):
                # Checks if appropriate size is in filename
                if char in filename == "6":
                    size = 6
                elif char in filename  == "9":
                    size = 9
                else:
                    size = 12
                        
                return size
            
            return "Cant't find board with given input, please try again!"
                    
                
              
             
        
        
        