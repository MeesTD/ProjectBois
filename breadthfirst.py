import random
from .Objects import board

class Breadth_first(object):
    """
    The breadth first algorithm finds the solution by traversing through the nodes. It starts at 
    the root and explores all the neighbor nodes. When it finds a correct step it continues to the child
    nodes and continues to explore correct steps and related nodes.
    
    """
    
    def __init__(self, board):
        self.board = board
        self.nodes = []
        
        
        