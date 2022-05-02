""" Use cProfile to get runtime statistics for the recursive version of
Floyd_warshall Algorithm """

# Import sys and os packages

# Import cProfile package

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import Floyd-Warshall function

# Import Floyd-Warshall test cases

# Import cProfile package
import cProfile

# Performance Tests
cProfile.run("floyd_warshall(sample_1)")

cProfile.run("floyd_warshall(sample_2)")

cProfile.run("floyd_warshall(sample_3)")
