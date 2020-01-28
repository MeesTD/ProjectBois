###################################################################################################
# car.py
#
# Zeno Degenkamp, Mats Pijning, Mees Drissen
#
# The Car object is a representation of the cars on a game of Rushhour. 
# It contains all information relevant to the cars, such as size, orientation, location 
# and the type (is it a red car or not). All information is gathered from the csv file.
###################################################################################################
class Car(object):
    """
    This class holds the information that is relevant for cars.
    It will hold the name, orientation, starting (and later current)
    coördinates and its length
    """

    def __init__ (self, name, orientation, x, y, length):
        self.name = name
        self.orientation = orientation
        self.length = int(length)
        self.xy = []
        x = int(x.replace('"', ''))
        y = int(y.replace('"', ''))
        self.xy = self.make_coords(x, y)


    def get_orientation(self):
        """ 
        This method checks the orientation of the car, whether it's horizontal or vertical
        """
        
        if self.orientation == " H":
            return True
        return False


    def get_coords(self, name):
        """
        This method gets the location of the car that is selected
        """
        
        return self.xy

    
    def make_coords(self, x, y):
        """
        This method creates the car coordinates given its length
        """
        
        xy = []
        
        # Loops the amount the length of the car has
        for length in range(self.length):
            
            # Retreives the coords for the car
            temp_coords = []
            temp_coords.append(x)
            temp_coords.append(y)
            xy.append(temp_coords)
            
            # Modifies x or y depending on the orientation of the car
            if self.get_orientation():
                x += 1
            else:
                y += 1
        return xy


    def set_coords(self, steps):
        """
        This method changes the coördinates for the selected car
        """
        
        # Loops through the length of the coords
        for current in range(len(self.xy)):
            
            # Changes the coords depending on the orientation
            if self.get_orientation():
                self.xy[current][0] += steps
            else:
                self.xy[current][1] += steps
        
        return True
             
                
    def __repr__(self):
        return f"{self.name} {self.orientation} {self.length} {self.xy}"


    def __str__(self):
        return f"{self.name} {self.orientation} {self.length} {self.xy}"