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