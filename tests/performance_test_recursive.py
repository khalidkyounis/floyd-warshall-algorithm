""" Use cProfile to get runtime statistics for the recursive version of
Floyd_warshall Algorithm """

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import Floyd-Warshall function
from functions.floyd_warshall_recursive import floyd_warshall

# Import Floyd-Warshall test cases
from tests.test_samples import (sample_1, sample_2)

# Import cProfile package
import cProfile

# Performance Tests
cProfile.run("floyd_warshall(sample_1)")

cProfile.run("floyd_warshall(sample_2)")
