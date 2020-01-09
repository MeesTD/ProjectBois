class Board(object):
    """
    This class will initiate a grid which consists of a matrix which consists of a list of lists.
    """
    
    # Initializes a board object 
    def __init__(self, size):
        # Board properties
        self.size = size
        self.grid = []

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
        # TODO: Deze method zal een CSV file readen en op basis daarvan zal de init het bord starten.