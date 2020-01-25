import copy
from . import route, rushhour, car
from ..Algorithms import breadthfirst, breadfirst_prio

def get_next_state(states):
        """
        Gets the next state from the list.
        """

        return states.pop()

def lookahead (state, move_amount, final_state):
    """
    This method looks ahead for move_amount times to return a move which will lead to 
    the move with the lowest f value.
    """
    #  Initiate values
    states = []
    first_state = copy.deepcopy(state)
    states.append(first_state)

    # Go move_amount nodes deep into the tree.
    for i in range(len(states)):
        temp_state = states.pop()
        possible_moves = []
        for j in range(move_amount):

            # Make a new move for each possible move in state.
            for car in temp_state.cars.values():
                possible_moves.append(breadthfirst.get_possibilities(car, temp_state))

            new_states = make_children(temp_state, possible_moves, final_state)

            # Append the states 
            for state in new_states:
                states.append(state)

    return states