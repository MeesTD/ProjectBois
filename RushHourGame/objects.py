class Car(object):
    """
    This class holds the information that is relevant for cars.
    It will hold the name, orientation, starting (and later current)
    coördinates and its length.
    """

    # Initializes a car object. 
    def __init__ (self, name, orientation, x, y, length):
        # Car properties
        self.name = name
        self.orientation = orientation
        self.length = length
        self.x = int(x.replace('"', ''))
        self.y = int(y.replace('"', ''))
        
    def __str__(self):
        return f"{self.name} {self.orientation} {self.length} coords: {self.x},  {self.y}"
        
        
class Board(object):
    """
    This class ......
    """
    
    # Initializes a board object 
    def __init__(self, size):
        # Board properties
        self.grid = []
          
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
    
            
        

