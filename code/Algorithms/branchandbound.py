import copy
import pickle
from . import breadthfirst
from ..Objects import route, rushhour, car, board


def get_next_state_deep(states):
        """
        Gets the next state from the list.
        """

        return states.pop()


def run(game):
    #  Set a limit for the algorithm. Base this on a lower bound!
    limit = 763
    algorithm = breadthfirst.Breadthfirst(game)
    solution_amount = 0
    solutions = []
    while algorithm.states:
        # Initiate necessary values
        all_possibilities = []
        new_state = get_next_state_deep(algorithm.states)

        # Keep making moves while you haven't won the game and reached the limit.
        if not new_state.check_win() and new_state.archive.moves < limit:
            for car in new_state.cars.values():

                # Creates variable to check possibilities.
                check = algorithm.get_possibilities(car, new_state.cars, new_state)

                # Refuse cars that cannot make a move.
                if check != []:
                    all_possibilities.append(check)

            # Loops over all possibilities. 
            for possibility in all_possibilities:
                algorithm.build_children(possibility, new_state)
        # If you win, check if you found a solution more quickly than the limit.
        elif new_state.check_win():
            solution_amount += 1
            solution = route.make_key(new_state)
            solution += str(new_state.archive.moves)
            solutions.append(solution) 
            print(f"Found a solution with {new_state.archive.moves} moves.")
            #  Set the limit to the value of the # of moves so you can keep looking for better solutions.
            if new_state.archive.moves < limit :
                limit = copy.deepcopy(new_state.archive.moves)
        print(len(algorithm.states))
        print(new_state.archive.moves)
        if solution_amount < 50:
            print(f"Found{solution_amount} solutions")
            break
    print(solutions)
    print(f"Lower bound is {limit}!")
            
