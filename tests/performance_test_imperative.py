""" Use cProfile to get runtime statistics for the imperative version of
Floyd_warshall Algorithm """

# Import sys and os packages
import os
import sys
# Import testing package
import cProfile

SCRIPT_DIR = os.path.dirname(__file__)
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import Floyd-Warshall function
from functions.floyd_warshall_imperative import floyd_warshall

# Import Floyd-Warshall test cases
from test_samples import (sample_1, sample_2, sample_3)

# Performance Tests
cProfile.run("floyd_warshall(sample_1)")

cProfile.run("floyd_warshall(sample_2)")

cProfile.run("floyd_warshall(sample_3)")
