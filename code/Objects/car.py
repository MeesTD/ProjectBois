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
        self.xy = []
        x = int(x.replace('"', ''))
        y = int(y.replace('"', ''))
        self.xy = self.make_coords(x, y)

    # This method returns the orientation of the car.
    def get_orientation(self):
        """ This method checks the orientation of the car, whether it's horizontal or vertical"""
        if self.orientation == " H":
            return True
        return False

    # This method returns the coordinates of the current car.
    def get_coords(self, name):
        """ This method gets the location of the car that is selected"""
        return name.x and name.y

    def make_coords(self, x, y):
        """ This method creates the car coordinates for its length"""
        xy = []
        for j in range(self.length):
            temp_coords = []
            temp_coords.append(x)
            temp_coords.append(y)
            xy.append(temp_coords)
            if self.get_orientation():
                x += 1
            else:
                y += 1
        return xy


    # This changes the coordinates of the car.
    def set_coords(self, steps):
        """ This method changes the coördinates for the selected car"""
        for i in range(len(self.xy)):
            if self.get_orientation:
                self.xy[i][0] += steps
            else:
                self.xy[i][1] += steps
        return True
                
    def __repr__(self):
        return f"{self.name} {self.orientation} {self.length} {self.xy}"