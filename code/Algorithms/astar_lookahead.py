###################################################################################################
# astar_lookahead.py
#
# Zeno Degenkamp, Mats Pijning, Mees Drissen
#
# This file contains the astar look ahead algorithm
###################################################################################################
from . import astar


def run(in_file):
    astar_lookahead = astar.Astar(in_file)
    