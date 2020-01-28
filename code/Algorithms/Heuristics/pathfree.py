"""
This heuristic calculcates whether or not the path of the red car is free.
It returns the amount of cars that are in the way of the red car.
"""

def calc_h(all_children):
    # initialize blocking cars value
    blocking_cars = 0
    
    # Loops through all the children
    for child in all_children:

        blocking_cars = 0
        
        # Loops through all the cars of the child
        for car in child.cars.values():
            
            # Only check other cars than red car
            if not car.name == "X":
        
                # Checks if cars are in the way of the red car and updates blocking car
                if car.xy[0][1]  == child.red_car.xy[0][1] or car.xy[1][1] == child.red_car.xy[0][1]:
                    blocking_cars += 1

                # Check if the car has a length of 3
                if car.length == 3:
                    # Check if that car is blocking the red car
                    if car.xy[2][1] == child.red_car.xy[0][1]:
                        blocking_cars += 1
                
        # Updates the f attribute of the child
        child.f = blocking_cars + child.archive.moves
    return all_children