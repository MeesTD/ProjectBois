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

    def get_orientation(self):
        """ This method checks the orientation of the car, whether it's horizontal or vertical"""
        if self.orientation == " H":
            return True
        return False

    def get_coords(self, name):
        """ This method gets the location of the car that is selected"""
        return name.x and name.y

    def set_coords(self, name, steps):
        """ This method changes the coördinates for the selected car"""
        if  name.get_orientation:
            name.x += steps
        else:
            name.y += steps

    def __repr__(self):
        return f"{self.name} {self.orientation} {self.length} coords: {self.x},  {self.y}"