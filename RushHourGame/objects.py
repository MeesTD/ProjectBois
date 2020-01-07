class Car:
    """
    This class holds the information that is relevant for cars.
    It will hold the name, orientation, starting (and later current)
    coördinates and its length.
    """

    # Initializes a car object. 
    def __init__ (self, name, orientation, length, coordinates):
        # Car properties
        self.name = name
        self.orientation = orientation
        self.length = length
        self.coordinates = coordinates
