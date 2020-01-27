###################################################################################################
# breadthfirst.py
#
# Zeno Degenkamp, Mats Pijning, Mees Drissen
#
# This is a breadthfirst algorithm. This means that it looks at all movements which can be made from
# the starting position and making children per layer. The algorithm first completes one layer of 
# children before continuing onto the next layer, which has more children. This algorithm will give
# the fastest solution possible, but it is extremely memory intensive, due to the amount of states 
# it has to account for. 
###################################################################################################
import copy
from ..Objects import board, car, rushhour, route


def get_possibilities(car, game):
        """
        Gets all the possible moves for the car.
        """
        
        # Initialize the variables necessary for this method.
        possibilities = []
        max_steps = game.game.size - car.length + 1
        
        # Check current car orientation.
        if car.get_orientation():
            directions = ['L', 'R']
        else:
            directions = ['U', 'D']

        # Loop over both possible directions and possible moves.
        for direction in directions:
            for step in range(1, max_steps):
                # Check if the move is possible before making it.
                if game.check_route(car.name, direction, step):
                    single_possibility = []
                    single_possibility = [str(car.name), str(direction), int(step)]
                    possibilities.append(single_possibility)
                
        return possibilities


class Breadthfirst(object):
    """
    THE Breadthfirst algorithm.
    """


    def __init__(self, infile):
        # We need a rushhour object to access its methods
        self.first_state = rushhour.RushHour(infile)
        self.states = []

        # Initialize the first state.
        self.states.append(copy.deepcopy(self.first_state))
    
    
    def get_next_state(self):
        """
        Gets the next state from the list.
        """

        return self.states.pop(0)


    def build_children(self, possibilities, state):
        """
        Build the possible children for a move.
        """
        for i in possibilities:
            new_game = copy.deepcopy(state)
            # Creates a new instance of rushhour.
            new_game.move(i[0], i[1], i[2])
            if not self.archive.get_state(new_game):
                self.archive.save_state(new_game)
                self.states.append(new_game)

    
    def run(self):
        """
        Run runs all the functionalities and methods for the breadthfirst algorithm
        """
        
        # Initializes variables
        self.archive = route.Route()
        i = 0
        
        # 
        while self.states:
            print(len(self.states))
            all_possibilities = []
            new_state = self.get_next_state()
            # new_state.print_game(new_state.game, new_state)
            # Loop over all cars.
            if not new_state.check_win():
                for car in new_state.cars.values():
                    # Creates variable to check possibilities.
                    check = get_possibilities(car, new_state)
                    # Refuse cars that cannot make a move.
                    if check != []:
                        all_possibilities.append(check)
                # Loops over all possibilities. 
                for possibility in all_possibilities:
                    self.build_children(possibility, new_state)
            else:
                new_state.print_game(new_state.game, new_state)
                print("Won!", len(self.states))
                break
        new_state.print_game(new_state.game, new_state)
        print(f"Finished with {new_state.archive.moves} moves")
