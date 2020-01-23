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
    limit = 15
    bound = 0
    algorithm = breadthfirst.Breadthfirst(game)
    solution_amount = 0
    solutions = []
    max_solutions = 55
    try:
        while algorithm.states and len(solutions) < max_solutions:
            # Initiate necessary values
            all_possibilities = []
            new_state = get_next_state_deep(algorithm.states)
            new_state.print_game(new_state.game, new_state)
            print("States: ", len(algorithm.states))
            print("Moves: ", new_state.archive.moves)

            # Keep making moves while you haven't won the game and reached the limit.
            if not new_state.check_win() and new_state.archive.moves < limit:
                for car in reversed(new_state.cars.values()):
                    
                    # Creates variable to check possibilities.
                    check = algorithm.get_possibilities(car, new_state.cars, new_state)

                    # Refuse cars that cannot make a move.
                    if check != []:
                        all_possibilities.append(check)

                # Loops over all possibilities and creates children based on them. 
                for possibility in all_possibilities:
                    algorithm.build_children(possibility, new_state)

            # If you win, check if you found a solution more quickly than the limit.
            elif new_state.check_win():
                solution_amount += 1
                solution = route.make_key(new_state)
                solution += str(new_state.archive.moves)
                solutions.append(solution)
                bound = new_state.archive.moves
                limit = new_state.archive.moves
                print(f"Found a solution with {new_state.archive.moves} moves.")

                #  Set the limit to the value of the # of moves so you can keep looking for better solutions.
            if new_state.archive.moves >= limit:
                print("Reached limit")

        #  Once finished print all found solutions
        for i in solutions:
            print("Solution \n", str(i))
        print(f"Lower bound is {bound}!")

    except (KeyboardInterrupt, SystemExit):
        print(solutions)
        print(bound)
            
