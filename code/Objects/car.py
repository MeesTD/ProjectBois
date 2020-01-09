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
        self.length = int(length)
        self.x1 = int(x.replace('"', ''))
        self.y1 = int(y.replace('"', ''))
        if self.get_orientation():
            self.x2 = self.x1 + 1
            self.y2 = self.y1
            if self.length == 3:
                self.x3 = self.x2 + 1
                self.y3 = self.y1
            else:
                self.x3 = None 
        if self.get_orientation() == False:
            self.y2 = self.y1 + 1
            self.x2 = self.x1
            if self.length == 3:
                self.y3 = self.y2 + 1
                self.x3 = self.x1
            else:
                self.y3 = None 


    def get_orientation(self):
        """ This method checks the orientation of the car, whether it's horizontal or vertical"""
        if self.orientation == " H":
            return True
        return False

    def get_coords(self, name):
        """ This method gets the location of the car that is selected"""
        return name.x1 and name.y1

    def set_coords(self, steps):
        """ This method changes the coördinates for the selected car"""
        if  self.get_orientation:
            self.x1 += steps
            self.x2 += steps
            if self.length == 3:
                self.x3 += steps
        else:
            self.y1 += steps
            self.y2 += steps
            if self.length == 3:
                self.y3 += steps
    def __repr__(self):
        return f"{self.name} {self.orientation} {self.length}"