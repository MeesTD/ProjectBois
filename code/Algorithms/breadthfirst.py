import copy
from ..Objects import board, car, rushhour, route

class Breadthfirst(object):
    """
    The Breadthfirst algorithm.
    """

    def __init__(self, infile):
        # Initialize variables to be used in the game
        # We need a rushhour and route object to access its methods
        self.first_state = rushhour.RushHour(infile)
        self.states = []
        self.archive = route.Route()

        # Initialize the first state.
        self.states.append(copy.deepcopy(self.first_state))
    
    def get_next_state(self):
        """
        Gets the next state from the list.
        """

        return self.states.pop(0)
    

    def get_possibilities(self, car, car_list, game):
        """
        Gets all the possible moves for the car.
        """
        # Initialize the variables necessary for this method.
        possibilities = []
        max_steps = self.first_state.game.size - car.length + 1
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

    def build_children(self, possibilities, state):
        """
        Build the possible children for a move.
        """
        for i in possibilities:
            new_game = copy.deepcopy(state)
            # Creates a new instance of rushhour.
            new_game.move(i[0], i[1], i[2])
            if not self.archive.get_state(new_game):
                self.archive.save_state(new_game, new_game.archive.moves)
                self.states.append(new_game)
        
    def run(self):
        i = 0
        while self.states and i < 10000:
            print(len(self.states))
            i += 1
            all_possibilities = []
            new_state = self.get_next_state()
            # new_state.print_game(new_state.game, new_state)
            # Loop over all cars.
            if not new_state.check_win():
                for car in new_state.cars.values():
                    # Creates variable to check possibilities.
                    check = self.get_possibilities(car, new_state.cars, new_state)
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
        print(f"Finished with {new_state.archive.moves} moves")
        if i > 9999:
            print("Couldn't finish the case within the time.")