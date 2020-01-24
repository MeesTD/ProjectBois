from ...Objects import rushhour

def calc_h(self, all_children):
    
    # Calculate the new H value for each child
    for child in all_children:
        child.f = child.game.size - child.red_car.xy[1][1]
        
    return all_children